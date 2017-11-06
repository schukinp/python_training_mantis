from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False


    def get_project_list(self, username='administrator', password='root'):
        project_list = []
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        response = client.service.mc_projects_get_user_accessible(username, password)
        for ProjectData in response:
            id = ProjectData.id
            name = ProjectData.name
            project_list.append(Project(id=id, name=name))
        return project_list














