# portfolio
A fully functional portfolio website. displaying all there's to know about my projects, career and skill,

# Object Oriented Software Design
This project is implemented with two Classes - Skill and Project 
These two classes are implemented in models.py
For this assignment the skills and the projects are in json files. However, in future assignments I will connect to a database. 

# class Skill:
Every Skill has the following attributes id, title, description, technology=None  
** Note - some skills are not technology based, so it defaults as None
Is connecting with skills.json, and also @app.route('/skill/<int:skill_id>') on app.py,

# class Project:
Every Project has the following attributes id, title, module, description, thumbnail, date, technologies
Connects with project.json, while connectining route can be found @app.route('/project/<int:project_id>') on app.py.
Also connecting the about but with a different route. listed @app.route('/about') on app.py

# static:
Is connecting templates containing all html files in a rootfile.
while connecting css with styles.css.
And all photos in images.
Also connecting js with script.js.
