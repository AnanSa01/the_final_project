from jira import JIRA


from final_project_of_them_all.logic.utilities import LoadCon


class JiraHandler:

    def __init__(self):
        self._jira_url = 'https://ansabek01.atlassian.net/'
        config = LoadCon.return_config()
        self._auth_jira = JIRA(
            basic_auth=('an.sabek01@gmail.com', config["jira_token"]),
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
