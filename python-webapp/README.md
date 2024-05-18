
# Login Application

This is a simple login application built with Flask and Docker.

## Project Structure

```

login-app/

│

├── app.py

├── templates/

│   └── login.html
    └── second_level_auth.html
    └── welcome.html

├── static/

│   └── style.css

├── requirements.txt

└── Dockerfile

```

## Prerequisites

- Docker installed on your machine.

- Python and Flask installed for local testing (optional).

## Setup and Installation

### Local Setup

1\. **Navigate to the project directory:**

```
cd login-app
```

2\. **Create a virtual environment (optional but recommended):**

```
   python -m venv venv
```
```
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3\. **Install the required Python packages:**

   ```
  pip install Flask
   ```

4\. **Run the Flask application:**

```
   python app.py
```

5\. **Open a browser and go to `http://localhost:5000` to see the login page.**

### Docker Setup

1\. **Navigate to the project directory:**

```
   cd login-app
```

2\. **Create the `requirements.txt` file:**
```
echo "Flask==2.0.2" > requirements.txt
```
3\. **Build the Docker image:**
   
```
docker build -t login-app:latest .
```

4\. **Run the Docker container:**

```
docker run -p 5001:5001 --name login-app-container login-app:latest
```

5\. **Open a browser and go to `http://localhost:5001` to see the login page.**

6\. **Push image to Docker hub**
   
Check Image: Verify the correct image name using `docker image ls`.
Tag Image: Assign the image a new name with your Docker Hub repository information:

    ```
    docker tag <your_image_name> <your_dockerhub_username>/<repository_name>:<tag>

    ```

Login: Authenticate with Docker Hub:

    ```
    docker login

    ```

    (Enter your Docker Hub credentials when prompted.)
Push Image: Upload the tagged image to Docker Hub:

    ```
    docker push <your_dockerhub_username>/<repository_name>:<tag>

    ```

Verify: Check if the push was successful by visiting your Docker Hub repository. The image should be listed there.
Troubleshooting: If you encounter errors:
  -   Double-check credentials and repository permissions.
  -   Ensure the image name and tag are correct.
  -   Review the Docker documentation or seek further assistance if needed.

## Application Usage

- Use the default credentials to log in:

  - Username: `admin`

  - Password: `password`

- Upon successful login, you will see a success message.

- If the credentials are incorrect, an error message will be displayed.

## Notes

- The `app.secret_key` should be replaced with a real secret key in production.

- Ensure Docker is properly installed and running on your machine before building and running the Docker image.

### Helper commands
```
List all containers (only IDs)
docker ps -aq
Stop all running containers
docker stop $(docker ps -aq)
Remove all containers
docker rm $(docker ps -aq)
Remove all images
docker rmi $(docker images -q)
```
---

