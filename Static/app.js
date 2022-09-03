"use strict";

class BoggleGame {
  //setting up standards for game - 60 seconds, 0 words, starting a new set of entries
    constructor() {

        this.time = 60;
        this.score = 0;
        this.words = new Set();

        this.countDown = setInterval(this.sec.bind(this), 1000);
        $("form").on("submit", this.handleSubmit.bind(this));
      }
     

        sec() {
            this.time--;
            $("#timer").html(this.time);
            this.stopTimer();
        }


async  handleSubmit(e) {
    e.preventDefault();
    //when user submits a word it is checked agains word file and if ok - adds word to session, ands score
    let word = $("input").val();

    if (!word) return;

    const res = await axios.get("/check-word", { params: {word:word}});

    let response = res.data.response;

    $("#response").html(response);
    $("form").trigger("reset");

    if (response === "ok") {
        if (this.words.has(word)) {
            return;
        }

        this.words.add(word);
        this.score += word.length;
        $("#score").html(`Score: ${this.score}`);

    }
}


stopTimer() {
    //if time runs out, stop  clock and replace form with  "GAME OVER"
    if (this.time < 1) {
      clearInterval(this.countDown);
      $("form").hide();
      $(".container").append($("<span>").html("GAME OVER!!!"));
      this.endGame();
    }
  }

async endGame() {
    //post score to server and update high score if needed 
    await axios.post("/end-game", { score: this.score });
   }
}
   

let game = new BoggleGame();

