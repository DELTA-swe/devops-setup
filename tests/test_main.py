import unittest
from fastapi.testclient import TestClient
from main import app

class TestOperationsEndpoint(unittest.TestCase):
    def setUp(self):
        """
        Sets up the test fixture for the FastAPI application.

        This method initializes a TestClient to interact with the FastAPI app,
        allowing HTTP requests to be made to test the operations endpoint.
        """
        self.client = TestClient(app)

    def test_add(self):
        
        """
        Tests the "add" operation of the operations endpoint.

        Verifies that sending a GET request to "/operations/add/2/3" returns a 200
        status code and a JSON response containing the result of the addition,
        which is 5.
        """
        response = self.client.get("/operations/add/2/3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 5})

    def test_subtract(self):
        """
        Tests the "subtract" operation of the operations endpoint.

        Verifies that sending a GET request to "/operations/subtract/5/3" returns a 200
        status code and a JSON response containing the result of the subtraction,
        which is 2.
        """
        
        response = self.client.get("/operations/subtract/5/3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 2})

    def test_multiply(self):
        """
        Tests the "multiply" operation of the operations endpoint.

        Verifies that sending a GET request to "/operations/multiply/2/3" returns a 200
        status code and a JSON response containing the result of the multiplication,
        which is 6.
        """
        
        response = self.client.get("/operations/multiply/2/3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 6})

    def test_divide(self):
        """
        Tests the "divide" operation of the operations endpoint.

        Verifies that sending a GET request to "/operations/divide/6/3" returns a 200
        status code and a JSON response containing the result of the division,
        which is 2.
        """
        response = self.client.get("/operations/divide/6/3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 2})

    def test_invalid_operation(self):
        """
        Tests the "invalid operation" case of the operations endpoint.

        Verifies that sending a GET request to "/operations/invalid/1/1" returns a 200
        status code and a JSON response containing an error message.
        """
        response = self.client.get("/operations/invalid/1/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"error": "Invalid operation"})

if __name__ == "__main__":
    unittest.main()