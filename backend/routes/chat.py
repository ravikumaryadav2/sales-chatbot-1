from flask import Blueprint, request, jsonify
from inventory import inventory

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response_message = generate_response(user_message)
    return jsonify({"response": response_message})

def generate_response(message):
    # Simple keyword-based response generation
    if "buy" in message.lower():
        return "Sure! What would you like to buy?"
    elif "inventory" in message.lower():
        return f"We have the following items: {', '.join([item['name'] for item in inventory])}."
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"