# Casting Agency

## Capstone Project for Udacity's Full Stack Developer Nanodegree - Final project

This app help your casting agency when hiring actors for a movie.

Heroku Link: https://casting-agency-ibrahim.herokuapp.com

While running locally: http://localhost:5000

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

#### Virtual Enviornment

Recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

## Running the server

To run the server, execute:

```bash
export FLASK_APP=app.py
flask run --reload
```

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file to find the application. 

Using the `--reload` flag will detect file changes and restart the server automatically.

## Testing
For testing the backend, run the following commands (in the exact order):
```
dropdb casting_agency_test
createdb casting_agency_test
psql casting_agency_test < casting_agency.sql
python tests.py
```
The first time you run the tests, omit the dropdb command.

All tests are kept in that file and should be maintained as updates are made to app functionality.

## API Reference

## Getting Started
Base URL: This application can be run locally on the http://127.0.0.1:5000, or you can use the hosted version at `https://casting-agency-ibrahim.herokuapp.com`.

Authentication: All the endpoints in this application requires authentication.

The application has three roles:
- Casting Assistant
  - Can view actors and movies.
  - has `get:actors, get:movies` permissions.
- Casting Director
  - can perform all the actions that `Casting Assistant` can.
  - can also add or delete an actor from the database and also modify actors or movies.
  - has `post:actor, delete:actor, patch:actor, patch:movie` permissions in addition to all the permissions that `Casting Assistant` role has.
- Executive Producer
  - can perform all the actions that `Casting Director` can.
  - can also add or delete a movie from the database.
  - has `post:movie, delete:movie` permissions in addition to all the permissions that `Casting Director` role has.


## Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}
```

The API will return three error types when requests fail:

 - 400: Bad Request
 - 401: Unauthorized
 - 404: Not Found
 - 422: Unprocessable

## Endpoints

#### GET /actors
 - General
   - gets the list of all the actors
   - requires `get:actors` permission
 
 - Sample Request
   - `https://casting-agency-ibrahim.herokuapp.com/actors`

<details>
<summary>Response</summary>

```
{
    "actors": [
        {
            "age": 45,
            "gender": "Male",
            "id": 1,
            "name": "Leonardo DiCaprio"
        },
        {
            "age": 64,
            "gender": "Male",
            "id": 2,
            "name": "Tom Hanks"
        },
        {
            "age": 35,
            "gender": "Female",
            "id": 3,
            "name": "Scarlett Johansson"
        },
        {
            "age": 55,
            "gender": "Male",
            "id": 4,
            "name": "Robert Downey Jr"
        },
        {
            "age": 46,
            "gender": "Male",
            "id": 5,
            "name": "Christian Bale"
        },
        {
            "age": 49,
            "gender": "Male",
            "id": 6,
            "name": "Matt Damon"
        },
        {
            "age": 29,
            "gender": "Female",
            "id": 7,
            "name": "Emma Roberts"
        },
        {
            "age": 50,
            "gender": "Male",
            "id": 8,
            "name": "Matthew McConaughey"
        },
        {
            "age": 46,
            "gender": "Male",
            "id": 9,
            "name": "Mahershala Ali"
        },
        {
            "age": 59,
            "gender": "Male",
            "id": 10,
            "name": "Woody Harrelson"
        }
    ],
    "success": true
}
```

</details>

#### POST /actors
 - General
   - creates a new actor
   - requires `post:actor` permission
 
 - Request Body
   - name
   - age
   - gender
 
 - Sample Request
   - `https://casting-agency-ibrahim.herokuapp.com/actors`
   - Request Body
     ```
{
    "name":"Leonardo DiCaprio",
    "age": "45",
    "gender": "Male"
}
     ```

<details>
<summary>Response</summary>

```
{
    "success": true
}
```
  
</details>

#### PATCH /actors/{actor_id}
 - General
   - updates the info for an actor
   - requires `patch:actor` permission
 
 - Request Body (at least one of the following fields required)
   - name
   - age
   - gender
 
 - Sample Request
   - `https://casting-agency-ibrahim.herokuapp.com/actors/2`
   - Request Body
     ```
{
    "name":"Christian Bale"
}
     ```

<details>
<summary>Response</summary>

```
{
    "edited_actor_id": 2,
    "success": true
}
```
  
</details>

#### DELETE /actors/{actor_id}
 - General
   - deletes the actor
   - requires `delete:actor` permission
 
 - Sample Request
   - `https://casting-agency-ibrahim.herokuapp.com/actors/1`

<details>
<summary>Response</summary>

```
{
    "deleted_actor_id": 1,
    "success": true
}
```
  
</details>

#### GET /movies
 - General
   - gets the list of all the movies
   - requires `get:movies` permission
 
 - Sample Request
   - `https://casting-agency-ibrahim.herokuapp.com/movies`

<details>
<summary>Response</summary>

```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Tue, 02 Dec 1997 00:00:00 GMT",
            "title": "Good Will Hunting"
        },
        {
            "id": 2,
            "release_date": "Mon, 14 Jul 2008 00:00:00 GMT",
            "title": "The Dark Knight"
        },
        {
            "id": 3,
            "release_date": "Sun, 26 Oct 2014 00:00:00 GMT",
            "title": "Interstellar"
        },
        {
            "id": 4,
            "release_date": "Fri, 13 Aug 2010 00:00:00 GMT",
            "title": "Inception"
        },
        {
            "id": 5,
            "release_date": "Mon, 12 Mar 2012 00:00:00 GMT",
            "title": "The Hunger Games"
        },
        {
            "id": 6,
            "release_date": "Tue, 30 Apr 2002 00:00:00 GMT",
            "title": "Spider-Man"
        },
        {
            "id": 7,
            "release_date": "Fri, 08 Dec 2017 00:00:00 GMT",
            "title": "The Greatest Showman"
        },
        {
            "id": 8,
            "release_date": "Fri, 16 Nov 2001 00:00:00 GMT",
            "title": "Harry Potter and the Philosopher's Stone"
        },
        {
            "id": 9,
            "release_date": "Thu, 24 Nov 2016 00:00:00 GMT",
            "title": "The Founder"
        },
        {
            "id": 10,
            "release_date": "Fri, 08 Nov 2019 00:00:00 GMT",
            "title": "Klaus"
        }
    ],
    "success": true
}
```

</details>

#### POST /movies
 - General
   - creates a new movie
   - requires `post:movie` permission
 
 - Request Body
   - title
   - release_date
 
 - Sample Request
   - `https://casting-agency-ibrahim.herokuapp.com/movies`
   - Request Body
     ```
{
    "title":"Inception",
    "release_date": "16/7/2010"
}
     ```

<details>
<summary>Response</summary>

```
{
    "success": true
}
```
  
</details>

#### PATCH /movie/{movie_id}
 - General
   - updates the info for a movie
   - requires `patch:movie` permission
 
 - Request Body (at least one of the following fields required)
   - title
   - release_date
 
 - Sample Request
   - `https://casting-agency-ibrahim.herokuapp.com/movies/1`
   - Request Body
     ```
{
    "title":"The Dark Knight"
}
     ```

<details>
<summary>Response</summary>

```
{
    "edited_moive_id": 1,
    "success": true
}
```
  
</details>

#### DELETE /movies/{movie_id}
 - General
   - deletes the movie
   - requires `delete:movie` permission
 
 - Sample Request
   - `https://casting-agency-ibrahim.herokuapp.com/movies/3`

<details>
<summary>Sample Response</summary>

```
{
    "deleted_movie_id": 3,
    "success": true
}
```
  
</details>