from jira import JIRA
import os
from dotenv import load_dotenv

# Your JIRA instance URL


load_dotenv()


jira_username = os.getenv('USER')
jira_api_token = os.getenv('TOKEN')

# Replace the following variables with your JIRA instance information and API credentials
jira_url = 'https://caphub.atlassian.net'
# Replace with your admin email address
jira = JIRA(server=jira_url, basic_auth=(jira_username, jira_api_token))

# Replace the following variables with your project and team lead information
project_key = 'AP'


tasks = [
   {
        'name': 'Design and Implement User Model',
        'description': 'Design and implement the user model in the database.',
    },
    {
        'name': 'Design and Implement Registration API',
        'description': 'Develop the backend API for user registration.',
    },
    {
        'name': 'Develop User Registration UI',
        'description': 'Develop the frontend UI for user registration.',
    },
    {
        'name': 'Design and Implement Login API',
        'description': 'Develop the backend API for user login and authentication.',
    },
    {
        'name': 'Develop Login UI',
        'description': 'Develop the frontend UI for user login.',
    },
    {
        'name': 'Design and Implement Dashboard API',
        'description': 'Develop the backend API for the dashboard.',
    },
    {
        'name': 'Develop Dashboard UI',
        'description': 'Develop the frontend UI for the dashboard.',
    },
    {
        'name': 'Design and Implement Application Form API',
        'description': 'Develop the backend API for the application form.',
    },
    {
        'name': 'Develop Application Form UI',
        'description': 'Develop the frontend UI for the application form.',
    },
    {
        'name': 'Develop Proprietary Algorithm',
        'description': 'Develop the proprietary algorithm for matching funding options.',
    },
    {
        'name': 'Implement Security Measures',
        'description': 'Implement security measures such as encryption, sanitization, and validation.',
    },
]



for task in tasks:
    issue_dict = {
        'project': {'key': project_key},
        'summary': task['name'],
        'description': task['description'],
        'issuetype': {'name': 'Task'},
        'priority': {'name': 'Medium'},
    }
    new_issue = jira.create_issue(fields=issue_dict)
    print(f'JIRA issue created: {new_issue.key} - {task["name"]}')
