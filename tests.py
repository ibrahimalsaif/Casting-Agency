import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from database.models import setup_db, Movies, Actors


class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        self.Casting_Assistant = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdKUkJUa1YzdXhaaDQxdWR1cFFWLSJ9.eyJpc3MiOiJodHRwczovL2licmFoaW1hbHNhaWYudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMmM0OTY3NWM4NDhmMDAzN2M0OGM0MiIsImF1ZCI6IkNhc3RpbmcgQWdlbmN5IiwiaWF0IjoxNTk2OTQ1NjkxLCJleHAiOjE1OTcwMzIwOTEsImF6cCI6IlNPQzZZdFR5aGM0aTdmS3o2OHdqNjQ3MXExWjlCQTdvIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.kqrzkHpo9FHS_5AeqiYR_pelao8w8dEa1EGT4Qb0S1c9Q1320XEHXNo0vZPoDTP4zinBsfpktsW4jyUh466r53lGL_X8NTZk0szOJXjs0ifJO3MIFyOZ8Jc6J6VoCccYjI9QBTAgO2L7QpcmC0tuwM7db2xmk-lT5y7UjYMBae-URPoaZdEFA0wQ1hinvCi6KL-y-ct6iV5YAo-LD42t5kcfbUaRbshQakrVPvIkS_wNJoD622EM4_ZmXS-sakT6sm8imlO6PcQKTKg1PthUvHE7xL2jTZRcpd_RKgBSYnGzgez4ZdrAaZ9Tok4mySGf6RqFXlQu9180I6LjRy2eKA'
        self.Casting_Director = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdKUkJUa1YzdXhaaDQxdWR1cFFWLSJ9.eyJpc3MiOiJodHRwczovL2licmFoaW1hbHNhaWYudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMmM0OTk2MzJjZWEzMDIyMTE0NzlhMCIsImF1ZCI6IkNhc3RpbmcgQWdlbmN5IiwiaWF0IjoxNTk2OTQ1Nzc4LCJleHAiOjE1OTcwMzIxNzgsImF6cCI6IlNPQzZZdFR5aGM0aTdmS3o2OHdqNjQ3MXExWjlCQTdvIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIl19.r7SqGnkMa1Srf5uS7BZr9pvwUq0lIYqEbOesGY16-GH-AZhCuZB8uWpez0xb9LGkOMEaxe0qDiOWq5oKsribkYiB7W7Nl6mCzXy0HNVfDl3rTqem069F_X4VZQpD114BAz2vqExVHU5h3CzGdW0_DghS3_PBvlNCSIkbJx26ojLkXNlIp9VoxxzFr-XTo4j7iwUSvRzQwT8fi7rfiymANCn_eVWcRnJ5gm1fYocPpWYfLHVrBqXNqU1hpN_cuG24LVsv051PlGyUCupEvP-bfqSVeLjUoSPztJSYCEfskaJcBatv13MLdtrVT2gGRbn4E8JO5wM9-NA0hLB17bg6Xg'
        self.Executive_Producer = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdKUkJUa1YzdXhaaDQxdWR1cFFWLSJ9.eyJpc3MiOiJodHRwczovL2licmFoaW1hbHNhaWYudXMuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEyNTIwOTE2ODg0NTY2NjE1NjgxIiwiYXVkIjpbIkNhc3RpbmcgQWdlbmN5IiwiaHR0cHM6Ly9pYnJhaGltYWxzYWlmLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY5NDQ3MTYsImV4cCI6MTU5NzAzMTExNiwiYXpwIjoiU09DNll0VHloYzRpN2ZLejY4d2o2NDcxcTFaOUJBN28iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.OuPWpj6cSHfrjFMUrFjKUgNuJCHxIe4KnnoZptJHjbOwjg4mAc4uPLidxU1ZZOQwSkaXNGrLwCE9THJOJF1uYwXPVum5CyVHC91Gjf6YGS9qcNYqZRj4per8HVk6-KdNtrmZfzM680fZGt-SG6AAP1M1O2fMeuDsam8UuFrx1mXrgomGavAL6ywet3oXAFGfs84YZzQgrGmIpSLsndukRV9lN488rtnZzc3EdC5EiKhJlqRisP-YSlgAFJ9dr9UxgomsNlb53RsQmbXLQUPgtb3Qw5eUEXzG99ppA6KPD86YieRhy9xzZv4IxeV8XFaPjHh9FSrYmgl3BqYVj3rKwA'
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        self.database_path = "postgres://{}/{}".format(
            'postgres:7654321@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_actors(self):
        res = self.client().get('/actors', headers={
            'Authorization': "Bearer {}".format(self.Casting_Assistant)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_get_actors_no_token(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_get_movies(self):
        res = self.client().get('/movies', headers={
            'Authorization': "Bearer {}".format(self.Casting_Assistant)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_get_movies_no_token(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_actor_success(self):
        res = self.client().get('/actors/1', headers={
            'Authorization': "Bearer {}".format(self.Casting_Director)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_actor_id'], 1)

    def test_delete_actor_no_token(self):
        res = self.client().get('/actors/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_movie_success(self):
        res = self.client().get('/movies/3', headers={
            'Authorization': "Bearer {}".format(self.Executive_Producer)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_movie_id'], 3)

    def test_delete_movie_no_token(self):
        res = self.client().get('/movies/3')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_add_actor_success(self):
        mock_actor = {
            'name': 'Leonardo DiCaprio',
            'age': '45',
            'gender': 'Male'
        }

        res = self.client().get('/actors', headers={
            'Authorization': "Bearer {}".format(self.Casting_Director)
        }, json=mock_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_actor_no_token(self):
        mock_actor = {
            'name': 'Leonardo DiCaprio',
            'age': '45',
            'gender': 'Male'
        }

        res = self.client().get('/actors', json=mock_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_add_movie_success(self):
        mock_movie = {
            'title': 'Inception',
            'release_date': '16/7/2010'
        }

        res = self.client().get('/movies', headers={
            'Authorization': "Bearer {}".format(self.Executive_Producer)
        }, json=mock_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_movie_no_token(self):
        mock_movie = {
            'title': 'Inception',
            'release_date': '16/7/2010'
        }

        res = self.client().get('/movies', json=mock_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_edit_actor_success(self):
        mock_actor_edit = {
            'name': 'Christian Bale'
        }

        res = self.client().get('/actors/2', headers={
            'Authorization': "Bearer {}".format(self.Casting_Director)
        }, json=mock_actor_edit)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['edited_actor_id'], 2)

    def test_edit_actor_no_token(self):
        mock_actor_edit = {
            'name': 'Christian Bale'
        }

        res = self.client().get('/actors/2', json=mock_actor_edit)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_edit_movie_success(self):
        mock_movie_edit = {
            'title': 'The Dark Knight'
        }

        res = self.client().get('/movies/1', headers={
            'Authorization': "Bearer {}".format(self.Casting_Director)
        }, json=mock_movie_edit)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['edited_moive_id'], 1)

    def test_edit_movie_no_token(self):
        mock_movie_edit = {
            'title': 'The Dark Knight'
        }

        res = self.client().get('/movies/1', json=mock_movie_edit)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


if __name__ == "__main__":
    unittest.main()
