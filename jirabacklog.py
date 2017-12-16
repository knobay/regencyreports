"""Gets the number of issues in the Jira backlog for Jempython"""

# Import the functions needed from the regency reports library

from library.datacollector import read_jira_with_login
from library.datacollector import tabulate
from library.datacollector import save

# Config with constants. Could be better in a separate file.
FIELDS = ('id', 'self')
FILE = './output/prototype/backlog.tsv'
TARGET = 'https://jempython.atlassian.net/rest/api/2/search?jql=issuetype=Bug&status=Backlog&fields=updated,self,summary'


def main():
    "run the program"
    print('Starting Regency Reports - backlog issues...')
    data = read_jira_with_login(TARGET)   # get list containg feed (issues + other stuff)
    json_issues = data['issues']   # get list containing just json issues
    tabulated_issues = tabulate(json_issues, FIELDS)
    save(tabulated_issues, FILE)
    print('Program finished')

if __name__ == "__main__":
    main()
