# REST API Endpoints

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
users = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
]

# Get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Get a user by ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    return jsonify(user) if user else ('', 404)

# Add a new user
@app.route('/api/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
