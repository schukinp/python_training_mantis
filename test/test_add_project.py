from data.project import testdata
from model.project import Project
import pytest

@pytest.mark.parametrize("project", testdata)
def test_add_project(app, project):
    old_project_list = app.soap.get_project_list()
    app.project.add_new_project(project)
    new_project_list = app.soap.get_project_list()
    assert len(old_project_list) + 1 == len(new_project_list)
    old_project_list.append(project)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)