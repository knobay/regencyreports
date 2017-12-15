"""Basic functions for datacollection, manipulation and saving functions for Regency Reports"""

import requests # See http://docs.python-requests.org/en/master/user/install/#install"

def read(target_url):
    "Gets json data from a REST API and returns a list of json objects"
    my_request = requests.get(target_url)
    json_list = my_request.json()
    return json_list

def read_authenticated(target_url):
    "Gets json data from a REST API and returns a list of json objects"
    login = input('enter username for jira project')
    passw = input('enter password for jira project')
    my_request = requests.get(target_url, auth=(login, passw))
    json_list = my_request.json()
    return json_list

def tabulate(json_records, json_fields):
    "Converts list of json records into a table containing the fields requested"
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
    with open(file_name, 'w') as thefile:
        thefile.writelines('\t'.join(i) + '\n' for i in list_to_write)
    return True
