import logging
import re
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a real secret key in production

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Default credentials
USERNAME = 'admin'
PASSWORD = 'password'

def is_weak_password(password):
    if len(password) < 8:
        return True
    if not re.search("[a-zA-Z]", password) or not re.search("[0-9]", password):
        return True
    return False

@app.before_request
def log_request_info():
    logger.info(f"Request method: {request.method}")
    logger.info(f"User Agent: {request.user_agent}")
    logger.info(f"Client IP: {request.remote_addr}")

@app.after_request
def log_response_info(response):
    logger.info(f"Response status: {response.status}")
    return response

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        flash('Login successful!', 'success')
        logger.info('Login successful for user: %s', username)
        if is_weak_password(password):
            logger.warning('Weak password used by user: %s', username)
        return redirect(url_for('welcome'))
    else:
        flash('Invalid credentials. Please try again.', 'danger')
        logger.warning('Login failed for user: %s', username)
        return redirect(url_for('second_level_auth'))

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/second_level_auth')
def second_level_auth():
    return render_template('second_level_auth.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
