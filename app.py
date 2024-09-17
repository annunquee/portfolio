from flask import Flask, render_template, jsonify, request
import json
from dotenv import load_dotenv
from models import Project  # Import the Project class
load_dotenv()

app = Flask(__name__)

def load_projects():
    with open('projects.json') as f:
        project_data = json.load(f)
        projects = [Project(**proj) for proj in project_data]
    return projects

@app.route('/')
def index():
    projects = load_projects()
    latest_projects = sorted(projects, key=lambda x: x.date, reverse=True)[:6] 
    return render_template('index.html', projects=latest_projects)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/project/<int:project_id>')
def project_details(project_id):
    projects = load_projects()
    project = next((proj for proj in projects if proj.id == project_id), None)
    if project is None:
        return "Project not found", 404
    return render_template('project_details.html', project=project)

if __name__ == '__main__':
    app.run(debug=True)