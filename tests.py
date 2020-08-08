import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from database.models import setup_db, Movies, Actors

class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        self.Casting_Assistant = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdKUkJUa1YzdXhaaDQxdWR1cFFWLSJ9.eyJpc3MiOiJodHRwczovL2licmFoaW1hbHNhaWYudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMmM0OTY3NWM4NDhmMDAzN2M0OGM0MiIsImF1ZCI6IkNhc3RpbmcgQWdlbmN5IiwiaWF0IjoxNTk2ODE4MTQ5LCJleHAiOjE1OTY5MDQ1NDksImF6cCI6IlNPQzZZdFR5aGM0aTdmS3o2OHdqNjQ3MXExWjlCQTdvIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.kzgRYa9O3owxhPHkhKkYQwhmkaMvHc59PSQPuPOINzc7_X6KjV3eD5ERgyCKFT4P_ExkIde2XKi7YxgREiYa2DrlQM8v21kwSNXpImC4z5csWrKdCt54UUUvvQr_zOtRlw8htGeFbgLG_h7W3Y2on-LRHYzjMYjgjeoMgoZZnf5YNyNW8eUZt8jSPipz2KAE8IThuU7aRSXywUSAubmaJB4HRWpgcUqhjS3dqZIYkznXr6ewfuKJ8j9gjdJiDOtnZFpC7VDODWmG_m4hCosCN7tGRC6DjZ6rgXz1jaufBZAlwU1cp9N2KcW93Q8rcvqXfI4qjiNjaVf0LGgyEGPAng'
        self.Casting_Director = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdKUkJUa1YzdXhaaDQxdWR1cFFWLSJ9.eyJpc3MiOiJodHRwczovL2licmFoaW1hbHNhaWYudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMmM0OTk2MzJjZWEzMDIyMTE0NzlhMCIsImF1ZCI6IkNhc3RpbmcgQWdlbmN5IiwiaWF0IjoxNTk2ODE4MjcwLCJleHAiOjE1OTY5MDQ2NzAsImF6cCI6IlNPQzZZdFR5aGM0aTdmS3o2OHdqNjQ3MXExWjlCQTdvIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIl19.Ngv9RZ8V30ZqKV03slDf2JG84hFi8yVe_QvPYUd_x6YBZPbtP_TE_W3MkbBMoMUjj4xs349bmv6G3QH4m53mA53-VDXY5eBoZpz1W7EgoTep2qgLFXPHBSd02hnZixYEVsgO77KOr96mSZ_MxKg0uv3k_zV37eHy9R95rfN1fCzU2Xh8O18NhG86GPz7gnw5wNp1IkDhLd7z9-jvAQ8z5KuPxAbVmGTTomtIs7ZMmTw9iqFFQ0iWOWNvOaAoQ9gcWHEQHmfCEHW9QU4cKe7Znd20FZojWAlo1O21u-nvAOseO-g_a6bj8-MQXlotC4j2I1FWuu-e8f1zm2_oblIZbQ'
        self.Executive_Producer = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdKUkJUa1YzdXhaaDQxdWR1cFFWLSJ9.eyJpc3MiOiJodHRwczovL2licmFoaW1hbHNhaWYudXMuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEyNTIwOTE2ODg0NTY2NjE1NjgxIiwiYXVkIjpbIkNhc3RpbmcgQWdlbmN5IiwiaHR0cHM6Ly9pYnJhaGltYWxzYWlmLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MTgwMTQsImV4cCI6MTU5NjkwNDQxNCwiYXpwIjoiU09DNll0VHloYzRpN2ZLejY4d2o2NDcxcTFaOUJBN28iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.u9rKhNM9F_QwJzBwNBXolP80Z70EceiYf9-LtJ7wM4ww1_jJ61jCO984YB7hFLt68XcEVfFab97zHJ6MV951ieZ-u82ahtJ3YN689Ph1CEB9kDKIzU9bnknIo9hbpwc9Kzsw1bRwdQ66sPl91fUU4p0ctkOGx0y3v65o1827b7Vebio3LLMhxJQ_SDSzYnNlY6Lhxc_s1jNlQ6owqZZS0UfXK4AIROWYeeYTYgH99irIgB1jFs5leG1yED7Ux43Igk5e7bbBf_0DWInCl3V8VWxVSRBO7X6Xu0TrPf9__VBVl3XLHuE_ZhF1idHbrmrPrYBebcZaNXf4nJwGZh7GhA'
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "agency_test"
        self.database_path = "postgres://{}/{}".format('postgres:7654321@localhost:5432', self.database_name)
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
    
    # def test_delete_actor_no_token(self):
    #     res = self.client().get('/actors/100')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 401)
    #     self.assertEqual(data['success'], False)
    
    def test_delete_movie_success(self):
        res = self.client().get('/movies/3', headers={
            'Authorization': "Bearer {}".format(self.Executive_Producer)
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_movie_id'], 3)
    
    def test_delete_movies_no_token(self):
        res = self.client().get('/movies/50')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
    
    def test_add_actor_success(self):
        mock_actor = {
            'name':'Leonardo DiCaprio',
            'age': '45' ,
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
            'name':'Leonardo DiCaprio',
            'age': '45' ,
            'gender': 'Male'
        }

        res = self.client().get('/actors', json=mock_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
    
    def test_add_movie_success(self):
        mock_movie = {
            'title':'Inception',
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
            'title':'Inception',
            'release_date': '16/7/2010' 
        }

        res = self.client().get('/movies', json=mock_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
    
    def test_edit_actor_success(self):
        mock_actor_edit = {
            'name':'Christian Bale'
        }

        res = self.client().get('/actors/1', headers={
            'Authorization': "Bearer {}".format(self.Casting_Director)
        }, json=mock_actor_edit)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['edited_actor_id'], 1)
    
    def test_edit_actor_no_token(self):
        mock_actor_edit = {
            'name':'Christian Bale'
        }

        res = self.client().get('/actors/2', json=mock_actor_edit)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
    
    def test_edit_movie_success(self):
        mock_movie_edit = {
            'title':'The Dark Knight'
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
            'title':'The Dark Knight'
        }

        res = self.client().get('/movies/2', json=mock_movie_edit)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


if __name__ == "__main__":
    unittest.main()