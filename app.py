from flask import Flask, Response, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of application requests"
)


@app.before_request
def count_requests():
    REQUEST_COUNT.inc()


@app.route("/")
def home():
    return """
    <h1>DevOps Demo Application</h1>
    <p>Application deployed successfully!</p>
    <p>Monitoring: Prometheus and Grafana</p>
    """


@app.route("/health")
def health():
    return jsonify(status="healthy")


@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
