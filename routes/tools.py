from flask import Blueprint, render_template
from routes.cache_file import cache


tools = Blueprint('tools', __name__, template_folder='../static/templates', static_folder='static')


@tools.route('/', methods=['GET'])
@cache.cached()
def home():
    response = render_template('index.html'), 200
    return response


@tools.route('/contact', methods=['GET'])
@cache.cached()
def contact():
    response = render_template('contact.html'), 200
    return response



@tools.route('/projects', methods=['GET'])
def projects():
    response = render_template('projects.html'), 200