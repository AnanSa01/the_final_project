from jira import JIRA

import logic.utilities


class JiraHandler:

    def __init__(self):
        self._jira_url = 'https://ansabek01.atlassian.net/'
        api_secret = logic.utilities.LoadConfig.return_file_secret()
        self._auth_jira = JIRA(
            basic_auth=('an.sabek01@gmail.com', api_secret["api_test_token"]),
            options={'server': self._jira_url}
        )

    def create_issue(self, project_key, summary, description, issue_type="Bug"):
        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type}
        }

        return self._auth_jira.create_issue(fields=issue_dict)
