from django.test import TestCase

class StatusAPITests(TestCase):

    def test_status_code(self):
        response = self.client.get("/api/status/")
        self.assertEqual(response.status_code, 200)

    def test_status_message(self):
        response = self.client.get("/api/status/")
        self.assertEqual(response.json()["status"], "ok")