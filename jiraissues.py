"""Gets the number of issues in the Jira backlog for Jempython"""

# Import the functions needed from the regency reports library

from library.datacollector import read_jira_with_login
from library.datacollector import tabulate
from library.datacollector import save
from library.datacollector import flatten_jira_issues

# Config with constants. Could be better in a separate file.

FIELDS = ('updated', 'id', 'summary', 'description', 'status', 'assignee', 'created', 'creator', 'url')
FILE = './output/prototype/backlog.tsv'
TARGET = 'https://jempython.atlassian.net/rest/api/2/search'

def main():
    "run the program"
    print('Starting Regency Reports ...')
    data = read_jira_with_login(TARGET, 0)   # get list containg feed (issues + other stuff)
    json_issues = flatten_jira_issues(data) # get 2d list containing jira issues
    tabulated_issues = tabulate(json_issues, FIELDS)
    save(tabulated_issues, 'output/prototype/issues.tsv')
    print('... Regency Reports finished')

if __name__ == "__main__":
    main()
