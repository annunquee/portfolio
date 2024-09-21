import json
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


class Skill:
    def __init__(self, id, title, description, technology=None):
        self.id =id
        self.title = title
        self.description = description
        self.technology = technology

  
    @classmethod
    def load_from_json(cls, file_path):
        with open(file_path, 'r') as f:
            skills_data = json.load(f)
        return [cls(**skill) for skill in skills_data]