"""Gets the number of issues in the Jira backlog for Jempython"""

# Import the functions needed from the regency reports library

from library.datacollector import read_jira_issues
from library.datacollector import tabulate
from library.datacollector import save
from library.datacollector import flatten_jira_issues
from library.datacollector import login_jira
from library.datacollector import get_jira_pagingation_data
from library.firestore import saveissues

# Config with constants. Could be better in a separate file.

FIELDS = ('updated', 'id', 'summary', 'description', 'status', 'assignee', 'created', 'creator', 'url')
FILE = './output/prototype/backlog.tsv'
PROJECT = 'jempython'

def main():
    "run the program"
    print('Starting Regency Reports ...')
    session = login_jira(PROJECT)
    pagination_info = get_jira_pagingation_data(PROJECT, session)
    data = read_jira_issues(PROJECT, session, pagination_info)   # get feed (issues + other stuff)
    json_issues = flatten_jira_issues(data) # get 2d list containing jira issues
    saveissues(json_issues, '/Users/kimnobay/Documents/Code/fire/regency-reports-firebase-adminsdk-iowt4-30495c5560.json')
    tabulated_issues = tabulate(json_issues, FIELDS)
    save(tabulated_issues, 'output/prototype/issues.tsv')
    print('... Regency Reports finished')

if __name__ == "__main__":
    main()
