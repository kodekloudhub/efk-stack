from flask import Flask
import logging

app = Flask(__name__)

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def hello_world():
    logging.info('Page refreshed')
    return 'Hello, Simple Flask application'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)
