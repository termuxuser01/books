// an object contains properties in a key-value pair format

let obj1 = {
  'name': 'vic',
  'lastname': 'defar',
  'age': 21,
  'phone': 123456789,
  'email': 'hola@b.com',
  // you can skip the function keyword
  hello(){
    console.log('hello', obj1.name, obj1.lastname);
  }
}

// quotes can be omitted on property names
// you can also nest objects

let obj2 = {
  name: 'Viv',
  lastname: 'car',
  book: {
    fav: 'python power',
    author: 'matt teyes',
  }
};

// accessing properties

console.log(obj1['name']);
console.log(obj2.book.author);

// call a no existing property
console.log(obj1.height);

// fill in default values
console.log(obj2.book.pages || 'i don\'t know yet');

// methods are object properties that hold function values

obj1.sendMessage = function(message){
  console.log('To:', obj1.name);
  console.log('############start message###############');
  console.log(message);
  console.log('############end message###############');
  // return the instance of object for method changing
  return this;
}

obj1.sendMessage('hello there!');


obj1.hello();

// emulate classes

class Person{
  // create constructor function
  constructor(name, age){
    // this is run when an instance of the class is made
    this.name = name;
    this.age = age;
    console.log('A new person is born');
  }
  // create a class method
  sendMessage(message){
  console.log('To:', this.name);
  console.log('############start message###############');
  console.log(message);
  console.log('############end message###############');
  return this;
  }
  sayHi(){
    console.log('hi', this.name);
    return this;
  }
}

let vianney = new Person('veronica', 28);

console.log(vianney);
vianney.sendMessage('ily');

// chaining methods

vianney.sayHi().sendMessage('you know?');

// inheritance

class PersonWithEmail extends Person{
  constructor(name, age, email){
    super(name, age);
    this.email = email;
  }
  sendEmail(email){
    consoel.log('email sent!');
    return this;
  }
}

let bell = new PersonWithEmail('belle', 19, "belle@hello.com");

console.log(bell);
