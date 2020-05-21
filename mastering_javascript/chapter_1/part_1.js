// this is the basic declaration of a function
// the function is compiled to an object with the same name as it
// this is called function statement
function addition(a, b){
  return a + b;
}

c = addition(1, 2);
console.log(c);

// here we create an anonymous function and assign it to a variable
// the con with using this method is that it does not allow recursion
let add = function(a, b){
  return a + b;
}

c = add(1,3);
console.log(c);

// you can also create a self invoking function
(function sayHello(){
  console.log('hello');
})()

// you can also pass functions as parameters for other functions
function changeCase(val){
  return val.toUpperCase();
}

function func(a, passfunction){
  console.log(passfunction(a));
}

func('smallcase', changeCase);

// you can use return to force a return from a function
function looper(x){
  if(x%5===0){
    return;
  }
  console.log(x);
}

// this wont print a 5 because we force the function to return if x%5=0
for(var i = 0; i < 10; i++){
  looper(i);
}

// we can treat functions as data and assign them to viariables
let say = console.log
say('what up!')




