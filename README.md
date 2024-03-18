# Mini project

This project requires Docker and Docker Compose to be installed. It might be needed to aso have a venv

## Installation

To set up the project, please follow these steps:

1. Navigate to the prueba directory.
2. Run the following command to start the Docker container and install Python and Django dependencies:

```bash
docker-compose up
```

This will create and start the necessary containers defined in the docker-compose.yml file, and set up the Python environment with all required dependencies.

# Making Requests

You can make requests to the project endpoints using tools like Postman or Insomnia:

    Launch Postman or Insomnia.
    Set the request method (POST) and enter the URL http://localhost:8000/analyze
    Add request body.
    Send request to the server.
![image](https://github.com/Barbie-44/psychic-spoon/assets/85578415/fddcdbad-e4ee-4bfd-a714-efc8f22ead0d)


# Usage

After setting up the environment and running the containers with docker-compose up, you can access the project at http://localhost:8000/analyze in your web browser.

