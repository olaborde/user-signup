from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),
    'templates')
    jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True

tasks = []

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('todos.html',title="Get It Done!", tasks=tasks)


app.run()