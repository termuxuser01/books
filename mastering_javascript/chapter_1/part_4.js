// create a variable in global scope
let outervar = 'I am outer!';

let copy;

// create a function in global scope
function outerP(){
  // inner variable cannot be accessed from the outside
  let inner = 'I am inner!';

  // create an inner function inside the outer scope
  function innerP(param){
    // can access both inner variable and variable in global scope
    console.log(outervar);
    console.log(inner);
    console.log(param);
    console.log(magic)

  }

  // store inner function in copy 
  // since copy was declared in a global context will be available outside
  copy = innerP;
  
  return;
}

// all variables in the outer scope will be available
// even if they are declared after the function is declared
let magic = "Magic!";
console.log(magic);

outerP();
// innerP cannot be accessed directly but it can through copy
copy('I am a copY!');

