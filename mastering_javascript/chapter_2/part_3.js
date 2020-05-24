// map () is an es6 key-value system

let girlies = new Map();

girlies.set('girl1', 'betsy');
girlies.set('girl2', 'belle');
girlies.set('girl3', 'vianney');

// return value from key
console.log(girlies.get('girl3'));

// check for a key's existance

console.log(girlies.has('girl4'));

// iterate through Map object

for (var [key, value] of girlies){
  if (key === 'girl3'){
    console.log(key, 'is', value);
  }
  else{
    console.log(key, 'was', value);
  }
}

// Sets are collections of values and can be iterated in the order of the
// insertion of their elements. An important characteristic about sets is 
// that a value can occur only once in a set

let mySet = new Set();

mySet.add(1);
mySet.add('herro');
mySet.add('foo');

// check to see if item is in set

console.log(mySet.has(1))

// check size of set

console.log(mySet.size);

// remove item from set

console.log(mySet.delete('foo'));

for (let item of mySet){console.log(item)};

