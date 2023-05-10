from jira import JIRA
import os

# Your JIRA instance URL
jira_url = "https://caphub.atlassian.net"
jira_username = os.environ['USERNAME']
jira_api_token = os.environ['TOKEN']

# Authenticate with the JIRA REST API
jira = JIRA(server=jira_url, basic_auth=(jira_username, jira_api_token))

# Issues to be deleted
issues_to_delete = ["DEV-{i}" for i in range(60, 80)]

# Delete issues
for issue_key in issues_to_delete:
    try:
        issue = jira.issue(issue_key)
        issue.delete()
        print("Deleted issue {issue_key}")
    except Exception as e:
        print("Error deleting issue {issue_key}: {e}")
