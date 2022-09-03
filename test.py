from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

   def setUp(self):
       """Stuff to do before each test"""
 
       self.client = app.test_client()
       app.config['TESTING'] = True
       
def test_homepage(self):
    """Check start up functionality"""

    with self.client:
        res = self.client.get("/")
        print(res.data)

        decoded = res.data.decode()
        self.assertIn("Score: 0", decoded)
        self.assertIn("Times Played: 0", decoded)
        self.assertIn("High Score: 0", decoded)
        
def test_valid_word(self):
    """Test if  word is a valid entry from a board in session"""
    
    with self.client as client:
        with client.session_transaction() as sess:
            sess['board'] = [["R", "O", "K", "R", "T"],
                            ["C", "C", "T", "T", "T"],
                            ["C", "A", "T", "T", "T"],
                            ["C", "A", "T", "T", "T"],
                            ["C", "A", "T", "T", "T"]]
    response = self.client.get('/check-word?word=rock')
    self.assertEqual(response.json['response'], 'ok')

def test_not_on_board(self):
    """test if word is not on board"""
      
    with self.client as client:
        with client.session_transaction() as sess:
            sess['board'] = [["R", "O", "K", "R", "T"],
                            ["C", "C", "T", "T", "T"],
                            ["C", "A", "T", "T", "T"],
                            ["C", "A", "T", "T", "T"],
                            ["C", "A", "T", "T", "T"]]
    response = self.client.get('/check-word?word=board')
    self.assertEqual(response.json['response'], 'not-on-board')
      
def test_not_word(self):
    """test if a non-english word is submitted"""
      
    with self.client as client:
        with client.session_transaction() as sess:
            sess['board'] = [["R", "O", "K", "R", "T"],
                            ["C", "C", "T", "T", "T"],
                            ["C", "A", "T", "T", "T"],
                            ["C", "A", "T", "T", "T"],
                            ["C", "A", "T", "T", "T"]]
    response = self.client.get('/check-word?word=leblanc')
    self.assertEqual(response.json['response'], 'not-word')
