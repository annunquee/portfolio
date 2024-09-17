from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/')
def index():
    projects = load_projects()
    latest_projects = sorted(projects, key=lambda x: x.date, reverse=True)[:6] 
    return render_template('index.html', projects=latest_projects)

if __name__ == '__main__':
    app.run(debug=True)