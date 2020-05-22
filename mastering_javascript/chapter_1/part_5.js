function delay(message){
  setTimeout(function () {console.log(message);}, 1000);
}

delay('Vianney');

// try to imitate private variables in javascript

function privTest(){
  // this variable is declared in the local scope of this function
  let score = 0;
  this.getScore = function () {
    // function to make the score variable accesible
    // from the outside
    return score;
  };

  this.scored = function () {
    // method that allows us to modify the score variable from outside
    score++;
  };
}

let private = new privTest();
private.scored();
console.log(private.score);
console.log(private.getScore());
