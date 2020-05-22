// if you define a variable without a statement it is by default placed in the 
// global scope

function varieator(){
  a = 5;
  return;
}

varieator();
console.log(a);

// js doesnt have a block level scope, instead it has a function level scope

var scope_name = 'Global';

console.log(scope_name);

(function scoper(){
  var scope_name = 'Local';
  console.log(scope_name);
})()

console.log(scope_name);

// // we cant do this because it is enclosed and not included in the global scope
// scoper()

// this is know as IIFE (imediatly invoked function expresion) and most programmers ommit naming the function as it is unecesary

let x = 1;

(function(){
  let x = 2;
  console.log(x); 
})()
console.log(x);

// passing parameters to IIFEs

(function foo(b){
  let a = 1;
  console.log(a + b);
})(3)

// a popular usage of inline function expressions is to use that as parameters of a function
function tab_switch(handler, tab){
  // call the handler function
  handler();
  console.log("current tab is now: " + tab);
}

// use inline function as parameter (in this case handler)
tab_switch((function(){
  console.log('switching tab...');
}), 2)

// java script uses hoisting which means that declaration is done in the compile phase and assignment in the execution phase

m = 1;
var m;
console.log(m);


bar();
function bar(){
  console.log('magic')
}

// with anonymous functions we have to declare the befor we call them

// // this will produce error
// functionOne();

// var functionOne = function(){
//   console.log('helo')
// }

// anonymous functions wont be hoisted and will be defined when reached by step by step execution

// // Never do this - different browsers will behave differently
// if (true) {
//   function sayMoo() {
//     return 'trueMoo';
//   }
// }
// else {
//   function sayMoo() {
//     return 'falseMoo';
//   }
// }

// the correct way
var sayMoo;
if(true){
  sayMoo = function(){
    return 'TrueMoo';
  }
}
else{
  sayMoo = function(){
    return 'FalseMoo'
  }
}

console.log(sayMoo());

// the argument parameter is a collection of all arguments passed to the function

// add a variable number of argument to a function and iterate through them

function summation(){
  let i, total = 0;
  for(i = 0; i < arguments.length; i++){
    total += arguments[i];
  }
  return total;
  // convert arguments into array
  let args = Array.prototype.slice.call(arguments);
  console.log(args);
}

console.log(summation(1,5,3,543,56,5));
console.log(summation(1,2,3,4,5));

// the this keyword refers to the parent object, in this case the global object

(function(){
  console.log(this.a);
})()

