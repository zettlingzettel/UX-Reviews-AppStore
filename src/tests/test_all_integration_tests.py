import unittest
import sys
import os
import pytest

sys.path.insert(0,
os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import app

@pytest.fixture(autouse=True)
def app_context():
    with app.app_context():
        yield

class TestDir(unittest.TestCase):
    def test_health_database(self):
        username = "user1",
        content = "content1"
        data = {}
        table_name_test = "TEST-TABLE-1"
        expected = "Database is not empty", 200
        mock_name = app.database_name

        self.assertTrue(app.app_health_checker(mock_name)==expected,
                        app.save_to_database(data, username, content, table_name_test)==None
                        )
    def test_application_metrics(self):
        self.assertTrue(app.app_metrics["requests"] == 0,
                        "Test Failed: There are some requests.")
        self.assertTrue(app.app_metrics["response_time"] == 0.0,
                        "Test Failed: Response Time shouldn't be 0.0.")
        self.assertTrue(app.app_metrics["requests_per_second"] == 0,
                        "Test Failed: Requests Per Second shouldn't be 0.")


if __name__ == '__main__':
    unittest.main()
