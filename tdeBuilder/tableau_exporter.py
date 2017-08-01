from tableau_tools.tableau_rest_api import *


def publish_tde(server, login, password, site, full_local_path, project_name, ds_name):
    connection = TableauRestApiConnection(server=unicode(server), username=unicode(login), password=unicode(password), site_content_url=unicode(site))
    connection.signin()
    project_obj = connection.query_project(unicode(project_name))
    print full_local_path
    print ds_name
    print project_name
    connection.publish_datasource(unicode(full_local_path), unicode(ds_name), project_obj)

