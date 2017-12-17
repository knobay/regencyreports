"""Basic functions for datacollection, manipulation and saving functions for Regency Reports"""

import getpass
import requests # See http://docs.python-requests.org/en/master/user/install/#install"

def read(target_url):
    "Gets json data from a REST API and returns a list of json objects"
    my_request = requests.get(target_url)
    json_list = my_request.json()
    return json_list

def login_jira(target_project):
    "Login to a Jira project and return a session object"
    print('connecting to Jira project {0}\nNeed account details...'.format(target_project))
    login = input('Username: ')
    pswd = getpass.getpass('Password:')
    jira_session = requests.Session()
    jira_session.auth = (login, pswd)
    jira_response = jira_session.get('https://{0}.atlassian.net/rest/auth/1/session'.format(target_project))
    if jira_response.status_code == 200:
        return jira_session
    else:
        return False

def read_jira_issues(target_project, current_session, startpage):
    "Gets Jira issues from the requested project at the requested start page"
    target_url = 'https://{0}.atlassian.net/rest/api/2/search?startAt={1}'.format(target_project, startpage)
    my_request = current_session.get(target_url)
    json_list = my_request.json()
    return json_list
    # HANDLE PAGINATION - STILL TO DO

def flatten_jira_issues(issueslist):
    "Extract useful properties issues and put in 2d list of issues"
    json_issues = issueslist['issues']
    issues_list = []
    for issue in json_issues:
        issue_fields = {}

        issue_fields['url'] = issue['self']
        issue_fields['id'] = issue['key']
        issue_fields['summary'] = issue['fields']['summary']
        issue_fields['created'] = issue['fields']['created']
        issue_fields['updated'] = issue['fields']['updated']
        issue_fields['creator'] = issue['fields']['creator']['emailAddress']
        issue_fields['reporter'] = issue['fields']['reporter']['emailAddress']
        issue_fields['priority'] = issue['fields']['priority']['name']
        issue_fields['type'] = issue['fields']['issuetype']['name']
        issue_fields['project'] = issue['fields']['project']['name']
        issue_fields['status'] = issue['fields']['status']['name']

        if issue['fields']['assignee'] != None:
            issue_fields['assignee'] = issue['fields']['assignee']['emailAddress']
        else:
            issue_fields['assignee'] = 'Not assigned'

        if issue['fields']['description']:
            issue_fields['description'] = issue['fields']['description'].replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')
        else:
            issue_fields['description'] = 'No description'

        issues_list.append(issue_fields)

    return issues_list

def tabulate(json_records, json_fields):
    "Converts list of json records into a 2d array containing the fields requested"
    table = []
    row = []
    # Add headings in the first row of the table using the field names requested
    for heading in json_fields:
        row.append(heading)
    table.append(row)
    # Iterate through each record and the required elements
    for record in json_records:
        row = []
        for j in range(0, len(json_fields)):
            row.append(record[json_fields[j]])
        table.append(row)
    return table

def save(list_to_write, file_name):
    "Writes a 2D list to a tab delimited file"
    print('Saving data to {0}...'.format(file_name))
    with open(file_name, 'w') as thefile:
        thefile.writelines('\t'.join(i) + '\n' for i in list_to_write)
    print('Done!')
    return True
