import logging
import re
import json
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a real secret key in production

# Define a custom JSON formatter
class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "level": record.levelname,
            "message": record.msg,
            "time": self.formatTime(record, self.datefmt),
            "logger": record.name,
            "pathname": record.pathname,
            "lineno": record.lineno,
            "funcname": record.funcName,
            "request": {
                "method": request.method,
                "url": request.url,
                "remote_addr": request.remote_addr,
                "user_agent": str(request.user_agent)
            }
        }
        if record.args:
            log_record['message'] = log_record['message'] % record.args
        return json.dumps(log_record)

# Configure logging
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

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
    logger.info(f"Request received")

@app.after_request
def log_response_info(response):
    logger.info(f"Response sent with status: {response.status_code}")
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