from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app


    def add_new_project(self, project_data):
        wd = self.app.wd
        self.open_project_list()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        wd.find_element_by_css_selector("input[name='name']").clear()
        wd.find_element_by_css_selector("input[name='name']").send_keys(project_data.name)
        wd.find_element_by_css_selector("textarea[name='description']").clear()
        wd.find_element_by_css_selector("textarea[name='description']").send_keys(project_data.description)
        wd.find_element_by_css_selector("input[value='Add Project']").click()

    def delete_any_project(self, index):
        wd = self.app.wd
        self.open_project_list()
        wd.find_elements_by_css_selector("td > a[href*='manage_proj_edit_page.php?project_id']")[index].click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()


    def get_project_list(self):
        wd = self.app.wd
        self.open_project_list()
        project_list = []
        for el in wd.find_elements_by_css_selector("td > a[href*='manage_proj_edit_page.php?project_id']"):
            id = el.get_attribute('search')[12:]
            name = el.text
            project_list.append(Project(name=name, id=id))
        return project_list


    def open_project_list(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()




