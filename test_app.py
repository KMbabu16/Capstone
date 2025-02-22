import os
import unittest
import json
from app import create_app
from models import setup_db, db
from flask_sqlalchemy import SQLAlchemy

# Environment variables for security
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN", "dev-om80m547hwxipo72.us.auth0.com")
ALGORITHMS = ['RS256']
API_AUDIENCE = "fsnd"

# Use environment variables for JWT tokens
JWT_EXEC_PROD = os.getenv("JWT_EXEC_PROD")

class FSNDTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """Executed after each test"""
        with self.app.app_context():
            db.session.remove()
        self.app_context.pop()

    def get_headers(self, token):
        """Set headers for authentication."""
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    # ---------------------- GET Tests ----------------------
    
    def test_get_actors(self):
        res = self.client.get("/actors", headers=self.get_headers(JWT_EXEC_PROD))
        data = res.get_json()
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertIn("actors", data)
    
    def test_get_movies_failure(self):
        res = self.client.get("/movies/100", headers=self.get_headers(JWT_EXEC_PROD))
        data = res.get_json()
        print(data)
        self.assertEqual(res.status_code, 405)

    def test_get_movies(self):
        res = self.client.get("/movies", headers=self.get_headers(JWT_EXEC_PROD))
        data = res.get_json()
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertIn("movies", data)
    
    # ---------------------- DELETE Tests ----------------------

    def test_delete_actor_failure(self):
        res = self.client.delete("/actors/9999", headers=self.get_headers(JWT_EXEC_PROD))
        data = res.get_json()
        print(data)
        self.assertEqual(res.status_code, 404)

    def test_delete_movie_failure(self):
        res = self.client.delete("/movies/9999", headers=self.get_headers(JWT_EXEC_PROD))
        data = res.get_json()
        print(data)
        self.assertEqual(res.status_code, 404)
    
    # ---------------------- PATCH Tests ----------------------

    def test_patch_actor(self):
        actor = {"name": "Mohan", "age": 30, "gender": "Male"}
        res = self.client.patch("/actors/1", json=actor, headers=self.get_headers(JWT_EXEC_PROD))
        data = res.get_json()
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_patch_movie(self):
        movie = {"title": "Anime Movie", "release_date": "2025-01-01", "genres": "Anime"}
        res = self.client.patch("/movies/1", json=movie, headers=self.get_headers(JWT_EXEC_PROD))
        data = res.get_json()
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    # ---------------------- POST Tests ----------------------

    def test_submit_actor(self):
        new_actor = {"name": "Mohan", "age": 30, "gender": "Male"}
        res = self.client.post("/actors", json=new_actor, headers=self.get_headers(JWT_EXEC_PROD))
        data = res.get_json()
        print(data)
        self.assertEqual(res.status_code, 201)
        self.assertTrue(data["success"])

    def test_submit_actor_failure(self):
        new_actor = {"name": "", "age": 7, "gender": "Male"}
        res = self.client.post("/actors", json=new_actor, headers=self.get_headers(JWT_EXEC_PROD))
        data = res.get_json()
        print(data)
        self.assertEqual(res.status_code, 400)

    def test_submit_movie(self):
        new_movie = {"title": "Anime Movie", "release_date": "2025-01-01", "genres": "Anime"}
        res = self.client.post("/movies", json=new_movie, headers=self.get_headers(JWT_EXEC_PROD))
        data = res.get_json()
        print(data)
        self.assertEqual(res.status_code, 201)
        self.assertTrue(data["success"])

    def test_submit_movie_failure(self):
        new_movie = {"release_date": "2025-01-01"}
        res = self.client.post("/movies", json=new_movie, headers=self.get_headers(JWT_EXEC_PROD))
        data = res.get_json()
        print(data)
        self.assertEqual(res.status_code, 400)
    
    
if __name__ == "__main__":
    unittest.main()
