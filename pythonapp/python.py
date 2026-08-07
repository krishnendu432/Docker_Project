from flask import Flask

 

app = Flask(__name__)

 

@app.route("/")

def home():

    return "<h1>🚀 Welcome to Docker + Python</h1><h2>DevOps Batch</h2>"

 

@app.route("/about")

def about():

    return "This application is running inside a Docker Container."

 

if __name__ == "__main__":
# the traffic can reach from any where because host ='0.0.0.0' and the port mapping done with '5000'
    app.run(host="0.0.0.0", port=5000)
