from flask import Blueprint

app_health = Blueprint('app_health', __name__)


@app_health.route("/health")
def hello():
    return "Health is working!"
