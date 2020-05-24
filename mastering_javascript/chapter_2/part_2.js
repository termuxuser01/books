// populate array

let names = [];
names[0] = 'Veronica';
names[1] = 'Vianney';
names[2] = 'Contreras';

console.log(names);

// length property
console.log(names.length);

// assign length value
names.length = 10;
console.log(names);

// most common itteration of array
for(i = 0; i < names.length; i++){
  console.log(names[i]);
}

// you can also use forEach

names.forEach(function(name){
  console.log(name);
})

// concat combines two arrays and returns a new one
both_names = names.concat('belle', 'delphine');
console.log(both_names);

// join adds each element of an array to a string

let girls = both_names.join(' ');
console.log(girls);

// push adds one or more element to end of array
// and returns the resaulting length

console.log(both_names.push('tamy', 'betsy'));
console.log(both_names)

// pop removes the last element and returns its value
gone = [];
gone.push(both_names.pop());
gone.push(both_names.pop());
console.log(gone.join(' '));
console.log('now i have: \n');
console.log(both_names);

// shift removes first element and returns it

let fn = names.shift();

console.log('her first name is:', fn);
console.log(names);

//unshitf add one or more names to the front of array
// and returns new length

let new_lenght = both_names.unshift('stephy', 'andrea');
console.log(new_lenght);
console.log(both_names);

let also_gone = [];

also_gone.unshift(both_names.shift());
also_gone.unshift(both_names.shift());

console.log(also_gone);
console.log(both_names);

// the reverse method is a thing

let rev = both_names.reverse();
console.log(rev);

//  indexOf(searchElement[, fromIndex]): This searches the array for searchElement and returns the index of the first match:

var a = ['a', 'b', 'a', 'b', 'a','c','a'];

console.log(a.indexOf('b'));

// non existing returns -1

console.log(a.indexOf('v'));

// start from index 2

console.log(a.indexOf('b', 2));

// backwards search

console.log(a.lastIndexOf('b'));

// starting from befor last match

console.log(a.lastIndexOf('b', 2));
