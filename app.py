from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "DevOpsGuard Flask App: Healthy"

@app.route('/fail')
def fail():
    # Intentional crash endpoint
    raise ValueError("Simulated failure for DevOps testing")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
