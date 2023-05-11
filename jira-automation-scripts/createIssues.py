from dotenv import load_dotenv
from jira import JIRA
import os

# load .env file
load_dotenv()

# Get JIRA credentials from environment variables
user = os.getenv("JIRA_USER")
api_token = os.getenv("JIRA_API_TOKEN")
server = "https://caphub.atlassian.net"

# Connect to JIRA
jira_options = {'server': server}
jira = JIRA(options=jira_options, basic_auth=(user, api_token))

# Define the project key
project_key = "AP"


def create_issue(project_key, summary, description, issue_type, epic_name=None, epic_link=None, parent=None):
    issue_dict = {
        'project': {'key': project_key},
        'summary': summary,
        'description': description,
        'issuetype': {'name': issue_type},
    }
    if parent:
        issue_dict['parent'] = {'id': parent}
    if epic_link:
        # 'customfield_10014' is usually the Epic Link field, but check your instance to be sure
        issue_dict['customfield_10014'] = epic_link
    if epic_name and issue_type == "Epic":
        # 'customfield_10011' is usually the Epic Name field, but check your instance to be sure
        issue_dict['customfield_10011'] = epic_name
    return jira.create_issue(issue_dict)


epics_data = [
    {"name": "User Registration",
        "description": "As a user, I want to create an account on the platform to access the services"},
    {"name": "User Dashboard", "description": "As a user, I want a dashboard to access funding options, view applications, and track funding request status"},
    {"name": "Application Form",
        "description": "As a user, I want an easy-to-use application form to apply for funding"},
    {"name": "Proprietary Algorithm",
        "description": "As a user, I want to be matched with the best funding options based on my data and goals"},
    {"name": "Security Measures",
        "description": "As a user, I want my information and data to be secure and confidential"},
    {"name": "Strategic Advisory Service",
        "description": "As a user, I want personalized guidance and support throughout the funding process"},
    {"name": "Compliance", "description": "As a user or admin, I want the platform to comply with relevant laws and regulations"},
    {"name": "Branded Company File",
        "description": "As a partner, I want a branded and customized company file for potential investments"},
    {"name": "Email Templates",
        "description": "As an admin, I want email templates for all stages of contact for both VDs and companies"},
    {"name": "Dashboard Tips", "description": "As a user, I want the dashboard to provide tips for small changes that will increase matching probability"}
]

tasks = [
    {"summary": "Define Registration Data Model",
     "description": "Define the schema for a User in the database", "type": "Task"},
    {"summary": "Create Registration API Endpoint",
     "description": "Implement an API endpoint to handle user registration requests.", "type": "Task"},
    {"summary": "Implement User Registration UI",
     "description": "Design the registration form in Figma.", "type": "Task"},
    {"summary": "Connect Registration UI to API",
     "description": "Implement functionality to make requests from the registration form to the backend API.", "type": "Task"},
    {"summary": "Implement Registration Confirmation Email",
     "description": "Implement a feature to send a confirmation email after a successful registration.", "type": "Task"},
    {"summary": "Testing and QA", "description": "Implement unit tests and integration tests for registration. Manual testing of the registration process.", "type": "Task"},
]

for epic_data in epics_data:
    epic = create_issue(
        project_key, epic_data["name"], epic_data["description"], "Epic", epic_name=epic_data["name"])

    for task_data in tasks:
        task = create_issue(
            project_key, task_data["summary"], task_data["description"], task_data["type"], epic_link=epic.key)
