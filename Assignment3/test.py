import subprocess
import time
import unittest
import pickle
from score import score
import pytest
import os
import requests

class TestScore(unittest.TestCase):
    def setUp(self):
        self.model = pickle.load(open("model.pkl", "rb")) # Load the trained model
        self.threshold = 0.5  # Threshold

    def test_smoke(self):
        # checks if function produces some output without crashing 
        text = "This is a test text."
        try: prediction, propensity = score(text, self.model, self.threshold)
        except Exception as e: pytest.fail(f"score function raised an exception: {e} (Smoke test failed)")
        self.assertIsNotNone(prediction)
        self.assertIsNotNone(propensity)


    def test_format(self):
        # Format test: check input/output formats/types
        text = "This is a test text."
        prediction, propensity = score(text, self.model, self.threshold)
        self.assertIsInstance(prediction, int) 
        self.assertIsInstance(propensity, float)

    def test_prediction_value(self):
        # Checks if prediction value is either 0 or 1
        text = "This is a test text."
        prediction, propensity = score(text, self.model, self.threshold)
        self.assertIn(prediction, [0, 1])

    def test_propensity_score(self):
        # Checks if propensity score is between 0 and 1
        text = "This is a test text."
        prediction, propensity = score(text, self.model, self.threshold)
        self.assertGreaterEqual(propensity, 0)
        self.assertLessEqual(propensity, 1)

    def test_threshold_0(self):
        # Check if setting threshold to 0 always predicts 1
        text = "This is a test text."
        prediction, propensity = score(text, self.model, 0)
        self.assertEqual(prediction, 1)

    def test_threshold_1(self):
        # Check if setting threshold to 1 always predicts 0
        text = "This is a test text."
        prediction, propensity = score(text, self.model, 1)
        self.assertEqual(prediction, 0)

    def test_spam_input(self):
        # Check prediction on obvious spam input text
        spam_text = "Buy cheap cookware now!"
        prediction, propensity = score(spam_text, self.model, self.threshold)
        self.assertEqual(prediction, 1)

    def test_non_spam_input(self):
        # Check prediction on obvious non-spam input text
        non_spam_text = "Meet you there tonight"
        prediction, propensity = score(non_spam_text, self.model, self.threshold)
        self.assertEqual(prediction, 0)
        
class TestFlask(unittest.TestCase):
    def setUp(self):
        # Launches the flask app using command line
        os.system('python3 app.py &')
        time.sleep(5)

    def test_integration(self):
        # Test the response from the localhost endpoint
        url = 'http://127.0.0.1:5000/'
        text = {'text': 'This is a test text.'}
        response = requests.post(url, data=text) #Fill text into the flask page
        self.assertEqual(response.status_code, 200) #Ensure that it returns a succesful response
        json_response = response.json() #response in json format
        #checks if final response has 'prediction' and 'propensity"
        self.assertIn('prediction', json_response)
        self.assertIn('propensity', json_response)

    def tearDown(self):
        # Close the Flask app
        os.system('pkill -f "python3 app.py"')    

if __name__ == '__main__':
    unittest.main()