let validateDataForAge = function(data){
  person = data()
  console.log(person)
  if(person.age < 1 || person.age > 99){
    return true;
  }
  else{
    return false;
  }
};

var generateDataForScientist = function() {
  return {
    name: "Albert Einstein",
    age : Math.floor(Math.random() * (100 - 1)) + 1,
  };
};
var generateDataForComposer = function() {
  return {
    name: "J S Bach",
    age : Math.floor(Math.random() * (100 - 1)) + 1,
    // age: 120,
  };
};


let errorHandler = function(error){
  console.log('An error has occurred');
}

let parseRequest = function(data, validate, handler){
  const error = validate(data)
  if(!error){
    console.log('no errors');
  }
  else{
    handler();
  }
}



parseRequest(generateDataForComposer, validateDataForAge, errorHandler);
parseRequest(generateDataForScientist, validateDataForAge, errorHandler)
