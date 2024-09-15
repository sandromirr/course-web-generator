class Link:
    def __init__(self, name, url):
        self.name = name
        self.url = url

class Assignment:
    def __init__(self, name, url):
        self.name = name
        self.url = url

class Lecture:
    def __init__(self, name):
        self.name = name
        self.links = []
        self.assignments = []

    def add_assignment(self, assignment):
        self.assignments.append(assignment)
    
    def add_link(self, link):
        self.links.append(link)
    
    def __str__(self):
        return f'{self.name}'