from flask import Flask
# Imports the Flask class from the Flask framework so we can create a web application.
import os

# Imports Python's os module, which is used here to read environment variables.

app = Flask(__name__)

# Creates a Flask application instance. __name__ tells Flask where the application is located.

@app.route("/")
# Defines the URL route /, which represents the application's home page.
def home():

 # Defines the Python function that will execute when a user accesses /.

    app_name = os.getenv("APP_NAME", "Default App")

 # Reads the APP_NAME environment variable. If it isn't set, "Default App" is used as the default value.

    environment = os.getenv("APP_ENV", "Development")

 # Reads the APP_ENV environment variable. If it isn't set, "Development" is used.

    return f"""

    <h1>{app_name}</h1>

    <h2>Environment : {environment}</h2>

    """

 # Returns an HTML response to the browser. The f allows Python variables such as app_name and environment to be inserted into the HTML.
# '<h1>{app_name}</h1>' Displays the application name as a large heading.
# <h2>Environment : {environment}</h2> Displays the current application environment, such as Development or Production.
if __name__ == "__main__":

# Checks whether this Python file is being executed directly rather than imported as a module.
# app.run(host="0.0.0.0", port=5000)
# Starts the Flask development server on port 5000. 0.0.0.0 makes the application listen on all network interfaces, which is important when running inside a container.

    app.run(host="0.0.0.0", port=5000)
