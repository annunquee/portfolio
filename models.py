# models.py 
class Project:
    def __init__(self, id, title, module, description, thumbnail, date, technologies):
        self.id = id
        self.title = title
        self.module = module
        self.description = description
        self.thumbnail = thumbnail
        self.date = date
        self.technologies = technologies