Casting Agency API Backend

Description

This project demonstrates the backend of a simple Casting Agency Management portal, enabling profiles for Executive Producer, Casting Director, and Casting Assistant to post details of new movies and actors. The backend is designed to manage both actors and movies, along with some general information about them.

Executive Producers can post, update, and delete actors/movies, as well as view submitted details.

Casting Directors can post, update, and delete actor details, and Edit & view movie details.

Casting Assistants can view all details about movies and actors.

Users must be authorized to perform role-based API requests.

Authorization of users is enabled via Auth0, with three separate roles (Executive Producer, Casting Director, and Casting Assistant), each assigned specific permissions.

Project Dependencies

This project requires the latest version of Python 3.x. It is recommended to download and install Python from the official website and use a virtual environment to install all dependencies.

PIP Dependencies

After successfully installing Python, navigate to the root folder of the project (which must be forked to your local machine) and run the following command:

pip3 install -r requirements.txt

This will install all required packages in your virtual environment.

Database Setup

The models.py file contains connection instructions to the PostgreSQL database, which must be set up and running. Provide a valid username and password if applicable.

Create a database named fsnd using the PostgreSQL CLI:

create database fsnd;

Initiate and migrate the database with the following commands:

flask db init
flask db migrate
flask db upgrade

This will create all necessary tables and relationships for the project.

Data Modeling

The data model is provided in models.py. The project consists of two tables:

Movies: Managed by the Executive Producer to add, update, and delete movies. All users can retrieve movie information.

Actors: Stores information about actors and is managed by the Casting Director, who can create, update, and delete actor profiles.

Running the Local Development Server

All necessary credentials to run the project are provided in the setup.sh file. Enable the credentials by running:

source setup.sh

To start the API server in a local development environment:

On Linux/macOS:

export FLASK_APP=app.py
export FLASK_ENV=development

On Windows:

set FLASK_APP=app.py
set FLASK_ENV=development

Run the following command to start the local server:

flask run

RBAC Credentials and Roles

Auth0 is used to manage role-based access control (RBAC) for users. JWT tokens must be included in the request headers.

Permissions

Executive Producer: 

post:movies - Add movies to the database

patch:movies - Edit movie details

delete:movies - Delete movies

post:actors - Add actors to the database

patch:actor - Edit actor details

delete:actor - Delete actors

get:actor - Retrieve actors

get:movies - Retrieve movies

Casting Director:

patch:movies - Edit movie details

post:actors - Add actors

patch:actor - Edit actor details

delete:actor - Delete actors

get:actor - Retrieve actors

get:movies - Retrieve movies

Casting Assistant:

get:actor - Retrieve actors

get:movies - Retrieve movies

There are no publicly available endpoints that do not require authorization.

API Reference

Getting Started

Base URL: The app can only be run locally. The backend runs at http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.

Authentication: This application requires authentication.

Error Handling

Errors return JSON responses in the following format:

{
    "success": false,
    "error": 400,
    "message": "bad request"
}

Common Errors

400: Bad Request

404: Resource Not Found

422: Unprocessable Entity

Endpoints

GET /actors

Returns a list of actors and the total count.

Sample request:

curl http://127.0.0.1:5000/actors -H "Authorization: Bearer $USER_TOKEN"

Sample response:

{
    "actors": [
        {"id": 1, "name": "Leonardo DiCaprio", "age": 48, "gender": "Male"},
        {"id": 2, "name": "Scarlett Johansson", "age": 39, "gender": "Female"}
    ],
    "total_actors": 2
}

GET /movies

Retrieves all movies with ID, title, release date, actor ID, and genres.

Sample request:

curl http://127.0.0.1:5000/movies -H "Authorization: Bearer $USER_TOKEN"

Sample response:

{
  "movies": [
        {"id": 1, "title": "Inception", "release_date": "2010-07-16", "actor_id": 1, "genres": "Sci-Fi"},
        {"id": 2, "title": "Lucy", "release_date": "2014-07-25", "actor_id": 2, "genres": "Action"}
    ],
  "total_movies": 2
}

DELETE /actors/{actor_id}

Deletes an actor by ID.

Sample request:

curl -X DELETE http://127.0.0.1:5000/actors/1 -H "Authorization: Bearer $USER_TOKEN"

Sample response:

{"success": true}

DELETE /movies/{movie_id}

Deletes a movie by ID.

Sample request:

curl -X DELETE http://127.0.0.1:5000/movies/1 -H "Authorization: Bearer $USER_TOKEN"

Sample response:

{"success": true}

Testing

All endpoints are tested using unittest. Test cases include success and error scenarios. RBAC functionality is also tested.

Running Tests

Create a test database using PostgreSQL CLI:

create database fsnd;

Run the test file:

python3 test_app.py

Deployment

The backend is deployed on Render and can be accessed at:

https://capstone-mq9w.onrender.com

