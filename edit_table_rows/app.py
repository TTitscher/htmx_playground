from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Local storage for users
users = [
    {"id": 1, "first_name": "John", "last_name": "Doe", "tags": "developer, python"},
    {"id": 2, "first_name": "Jane", "last_name": "Smith", "tags": "designer, ui/ux"}
]

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/users')
def get_users():
    return render_template('user_table.html', users=users)

@app.route('/user', methods=['POST'])
def add_user():
    new_user = {
        "id": len(users) + 1,
        "first_name": request.form.get('first_name'),
        "last_name": request.form.get('last_name'),
        "tags": request.form.get('tags')
    }
    users.append(new_user)
    return render_template('user_row.html', user=new_user)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return render_template('user_row.html', user=user)
    return "User not found", 404


@app.route('/user_edit/<int:user_id>', methods=['GET'])
def edit_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return render_template('user_edit_form.html', user=user)
    return "User not found", 404

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        user['first_name'] = request.form.get('first_name')
        user['last_name'] = request.form.get('last_name')
        user['tags'] = request.form.get('tags')
        return render_template('user_row.html', user=user)
    return "User not found", 404

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    users.remove(user)
    return ""
    # return render_template('user_table.html', users=users)
    


if __name__ == '__main__':
    app.run(debug=True)

