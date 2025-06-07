from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Kubernetes!"

<<<<<<< HEAD
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 40a1578 (Initial working Kubernetes deployment of Hello Python app)

