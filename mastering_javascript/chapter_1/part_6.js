// modules are used to mimic clases and focus on public and private access
// to variables

// the general structure is 
// Var moduleName=function() {
//   //private state
//   //private functions
//   return {
//      //public state
//      //public variables
//   }
// }

// the defined variables will remain private because they are in scope of the function

let superModule = (function (){
  let secret = "topsecret";
  let pass = 'nuke123';

  function getSecret(){
    console.log(secret);
  }

  function getPass(){
    console.log(pass)
  }

  return{
    getSecret: getSecret,
    getPass: getPass,
  }

})();


superModule.getSecret();
superModule.getPass();
