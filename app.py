from flask import Flask, render_template, jsonify, request
import json
from models import Project  # Import the Project class
from dotenv import load_dotenv
import os

# load enviroment variable from .env
load_dotenv()

app = Flask(__name__)

# set the secret key from the .env file
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Load projects from the Json file
def load_projects():
    with open('projects.json') as f:
        project_data = json.load(f)
        projects = [Project(**proj) for proj in project_data]
    return projects

# Route for the index page
@app.route('/')
def index():
    projects = load_projects()
    latest_projects = sorted(projects, key=lambda x: x.date, reverse=True)[:6]  # Display at least 3 most recent projects
    return render_template('index.html', projects=latest_projects)

#Route for project details by ID
@app.route('/project/<int:project_id>')
def project_details(project_id):
    projects = load_projects()
    project = next((proj for proj in projects if proj.id == project_id), None)
    if project is None:
        return "Project not found", 404
    return render_template('project_details.html', project=project)

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for the projects page
@app.route('/projects')
def projects():
    return render_template('projects.html', projects=projects)

#Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)