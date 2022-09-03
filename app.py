
from flask import Flask, request, render_template, session, jsonify

from boggle import Boggle




app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"


boggle_game = Boggle()

@app.route('/')
def show_main_page():
   """make the board, add to Session, render the gameboard in the DOM."""
   board = boggle_game.make_board()
   session['board'] = board
   """get the high score from  session so it can be displayed in  DOM. If no high score stored, show high score of 0"""
   highscore = session.get("highscore", 0)
   numplays = session.get("numplays", 0)

   return render_template('index.html', board=board, highscore=highscore, numplays=numplays)



@app.route('/check-word')
def check_word():
    """check word and generate response"""
    word = request.args['word']
    board = session['board']
    response_string = boggle_game.check_valid_word(board, word)

    return jsonify({'response': response_string})

@app.route("/end-game", methods=["POST"])
def end_game():
   """get axios (score) from the endgame function and update highscore"""
   score = request.json["score"]
   """get current high score, if there is no high score saved in session, set to zero."""
   highscore = session.get("highscore", 0)
   numplays = session.get("numplays", 0)
   """update high score in  session"""
   session["highscore"] = max(score, highscore)
   session["numplays"] = numplays + 1

   return "game over"
