
from flask import Blueprint

# Create a Blueprint for the main routes
main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    return "Hello i211226, Saaram Islam Cheema! This is a simple Flask application."