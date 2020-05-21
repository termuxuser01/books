// an anonymous function can be assigned to an object property

let santa = {
  say: function(){
    console.log('ho ho ho!');
  }
}

santa.say()

// you can also create an array of functions and execute them in an iteration

let funcs = [
  function(){console.log("Veronica")},
  function(){console.log('Vianney')},
]

for(let i = 0; i < funcs.length; i++){
  funcs[i]();
}

// anonymous functions as parameters to other functions

function eventHandler(event){
  event();
}

eventHandler(function(){
  console.log('this is an event');
})

