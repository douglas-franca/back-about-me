from flask import Blueprint
from flask import request
from app.controllers import answers_controller

# Create a Blueprint instance
routes_bp = Blueprint('routes_bp', __name__)

@routes_bp.route('/')
def home():
    return "Welcome to the home page!"

@routes_bp.route('/answer')
def question():
  query_param = request.args.get('question', default=None)
  print(query_param)
  return answers_controller.get_answer(query_param)