from flask import Blueprint, render_template
from routes.cache_file import cache


personal = Blueprint('personal', __name__, template_folder='../static/templates', static_folder='static')


@personal.route('/', methods=['GET'])
@cache.cached()
def home():
    response = render_template('index.html'), 200
    return response


@personal.route('/contact', methods=['GET'])
@cache.cached()
def contact():
    response = render_template('contact.html'), 200
    return response



@personal.route('/projects', methods=['GET'])
@cache.cached()
def projects():
    response = render_template('projects.html'), 200
    return response


@personal.route('/about', methods=['GET'])
@cache.cached()
def about():
    response = render_template('about.html'), 200
    return response