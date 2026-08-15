FROM python:latest
# Pull the python image from docker hub for the container.
 

WORKDIR /app
# Create a direcory 'app' inside the container if it isnot available and this is the working directory.
# Any following commands (COPY, RUN, CMD, etc.) will be executed from this directory.
 
COPY requirements.txt .
# requirements.txt is copied from your project folder to the current working directory (/app) inside the container.
# The . refers to the current directory, which is /app because of the WORKDIR command. 

RUN pip install --no-cache-dir -r requirements.txt 
# RUN executes a command while building the Docker image.
# pip install installs all Python libraries listed in requirements.txt.
# -r requirements.txt tells pip to read the package names from that file.
# --no-cache-dir prevents pip from storing downloaded packages in its cache, making the Docker image smaller.
 

COPY . .
# Copies all files and folders from your project into the container.
# The first . means the current folder on your computer.
# The second . means the current working directory (/app) inside the container.
 

EXPOSE 5000
# Tells Docker that the application inside the container listens on port 5000.
# This is mainly for documentation and networking; it does not automatically publish the port to your computer.
 

CMD ["python", "app.py"]
# CMD specifies the default command that runs when the container starts.
# This command starts the application by running:
