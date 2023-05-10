from jira import JIRA
import os


# Replace the following variables with your JIRA instance information and API credentials
jira_url = 'https://caphub.atlassian.net'
# Replace with your admin email address
jira_username = os.environ['USERNAME']
jira_api_token = os.environ['TOKEN']
jira = JIRA(server=jira_url, basic_auth=(jira_username, jira_api_token))

# Replace the following variables with your project and team lead information
project_key = 'DEV'
team_lead = 'michael@caphub-group.com'


tasks = [
    {
        'name': 'User Registration',
        'description': 'As a user, I want to create an account on the platform to access the services.',
        'importance': 'HIGH',
        'jira_issue': 'DEMO-1',
    },
    {
        'name': 'Dashboard',
        'description': 'As a user, I want a dashboard to access funding options, view applications, and track funding request status.',
        'importance': 'HIGH',
        'jira_issue': 'DEMO-2',
    },
    {
        'name': 'Application Form',
        'description': 'As a user, I want an easy-to-use application form to apply for funding.',
        'importance': 'HIGH',
        'jira_issue': 'DEMO-3',
    },
    {
        'name': 'Proprietary Algorithm',
        'description': 'As a user, I want to be matched with the best funding options based on my data and goals.',
        'importance': 'HIGH',
        'jira_issue': 'DEMO-4',
    },
    {
        'name': 'Security Measures',
        'description': 'As a user, I want my information and data to be secure and confidential.',
        'importance': 'HIGH',
        'jira_issue': 'DEMO-5',
    },
    {
        'name': 'Strategic Advisory Service',
        'description': 'As a user, I want personalized guidance and support throughout the funding process.',
        'importance': 'HIGH',
        'jira_issue': 'DEMO-6',
    },
    {
        'name': 'Compliance',
        'description': 'As a user or admin, I want the platform to comply with relevant laws and regulations.',
        'importance': 'HIGH',
        'jira_issue': 'DEMO-7',
    },
    {
        'name': 'Branded Company File',
        'description': 'As a partner, I want a branded and customized company file for potential investments.',
        'importance': 'MEDIUM',
        'jira_issue': 'DEMO-8',
    },
    {
        'name': 'Email Templates',
        'description': 'As an admin, I want email templates for all stages of contact for both VDs and companies.',
        'importance': 'MEDIUM',
        'jira_issue': 'DEMO-9',
    },
    {
        'name': 'Dashboard Tips (Nice to have)',
        'description': 'As a user, I want the dashboard to provide tips for small changes that will increase matching probability.',
        'importance': 'LOW',
        'jira_issue': 'DEMO-10',
    },
]


for task in tasks:
    issue_dict = {
        'project': {'key': project_key},
        'summary': task['name'],
        'description': task['description'],
        'issuetype': {'name': 'Task'},
        'assignee': {'name': team_lead},
    }
    new_issue = jira.create_issue(fields=issue_dict)
    print(f'JIRA issue created: {new_issue.key} - {task["name"]}')
