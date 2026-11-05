from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        tiedot = tomli.loads(content)
        project = tiedot["project"]

        authors =[author["name"] for author in project["authors"]]
   
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            project["name"], 
            project["description"],
            project["license"],
            authors,
            project["dependencies"], 
            tiedot["dependency-groups"]["dev"])
