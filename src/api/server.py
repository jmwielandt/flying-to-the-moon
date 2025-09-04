import logging
import time

from flask import Flask, g, request

from src.api import flights

app = Flask(__name__)

app.register_blueprint(flights.app)


@app.before_request
def log_request_info():
    """Logs information about the incoming request."""
    g.start_time = time.time()  # Store start time for response time calculation
    logging.info(f"Incoming Request: {request.method} {request.path}")


@app.after_request
def log_response_info(response):
    """Logs information about the outgoing response."""
    response_time = time.time() - g.start_time
    logging.info(
        f"Outgoing Response: {request.method} {request.path} {response.status_code} - Response Time: {response_time:.4f}s"
    )
    return response


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
