import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from database.models import setup_db, Movies, Actors
from auth.auth import AuthError, requires_auth

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(token):
        actors = Actors.query.all()

        if not actors:
            abort(404)

        return jsonify({
            'success': True,
            'actors': [actor.format() for actor in actors]
        })

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(token):
        movies = Movies.query.all()

        if not movies:
            abort(404)

        return jsonify({
            'success': True,
            'movies': [movie.format() for movie in movies]
        })

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(token,actor_id):
        try:
            actor = Actors.query.filter(Actors.id==actor_id).one_or_none()

            if not actor:
                abort(404)

            actor.delete()

            return jsonify({
                'success': True,
                'deleted_actor_id': actor_id
            })

        except:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(token,movie_id):
        try:
            movie = Movies.query.filter(Movies.id==movie_id).one_or_none()

            if not movie:
                abort(404)

            movie.delete()

            return jsonify({
                'success': True,
                'deleted_movie_id': movie_id
            })

        except:
            abort(422)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actor')
    def add_actor(token):
        data = request.get_json()

        name = data.get('name', None)
        age = data.get('age', None)
        gender = data.get('gender', None)

        try:
            actor = Actors(name=name, age=age, gender=gender)
            actor.insert()

            return jsonify({
                'success': True
            })
        except:
            abort(422)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movie')
    def add_movie(token):
        data = request.get_json()

        title = data.get('title', None)
        release_date = data.get('release_date', None)

        try:
            movie = Movies(title=title, release_date=release_date)
            movie.insert()

            return jsonify({
                'success': True
            })
        except:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def edit_actor(token,actor_id):
        data = request.get_json()
        
        name = data.get('name', None)
        age = data.get('age', None)
        gender = data.get('gender', None)

        try:
            actor = Actors.query.filter(Actors.id==actor_id).one_or_none()

            if not actor:
                abort(404)

            if name:
                actor.name = name

            if age:
                actor.age = age
            
            if gender:
                actor.gender = gender

            actor.update()

            return jsonify({
               'success': True,
               'edited_actor_id': actor_id
             })

        except:
            abort(422)
    
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def edit_movie(token,movie_id):
        data = request.get_json()
        
        title = data.get('title', None)
        release_date = data.get('release_date', None)

        try:
            moive = Movies.query.filter(Movies.id==movie_id).one_or_none()

            if not moive:
                abort(404)

            if title:
                moive.title = title

            if release_date:
                moive.release_date = release_date

            moive.update()

            return jsonify({
               'success': True,
               'edited_moive_id': movie_id
             })

        except:
            abort(422)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422
    
    @app.errorhandler(AuthError)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code
        
    return app

APP = create_app()

if __name__ == '__main__':
    APP.run(debug=True)