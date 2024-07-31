from flask import jsonify
from ..models.Answer import Answer

def get_answer(query_param):
  answer = Answer().get_answer(query_param)
  return jsonify({ 'answer': answer }), 200