# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        # TODO Add more tests relating to the home page
        assert "Portfolio" in html
        assert "about me" in html


    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 2
         # TODO Add more tests relating to the /api/timeline_post GET and POST apis
        post_response = self.client.post("/api/timeline_post", data={
            "name": "Test User",
            "email": "test@example.com",
            "content": "This is a test post!"
        })
        assert post_response.status_code == 200
        post_json = post_response.get_json()
        assert post_json["name"] == "Test User"
        assert post_json["email"] == "test@example.com"
        assert post_json["content"] == "This is a test post!"

        get_response = self.client.get("/api/timeline_post")
        assert get_response.status_code == 200
        json = get_response.get_json()
        assert len(json["timeline_posts"]) == 3
        assert json["timeline_posts"][0]["name"] == "Test User"

        # TODO Add more tests relating to the timeline page
        timeline_page = self.client.get("/timeline")
        assert timeline_page.status_code == 200
        html = timeline_page.get_data(as_text=True)
        assert "<form" in html
        assert "Submit" in html or "submit" in html


if __name__ == "__main__":
    unittest.main()
