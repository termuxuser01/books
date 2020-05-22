// match a text exactly

let pattern = /test/;

// or we can make an instance of a reg ex using the constructor

let pattern1 = new RegExp('test');

// case insensetive

let pattern2 = new RegExp('test', 'i');

// match all occurrances, not just first

let pattern3 = new RegExp('test', 'g');

// combining attributes

let comb_pattern = /test/ig;

// testing out
console.log(pattern.test('test'));
console.log(pattern.test('Test'));
console.log(pattern2.test('Test'));
console.log(pattern2.test('Testing testing 123'));
console.log(comb_pattern.test('Testing testing 123'));

console.log(pattern2);

// match against a set of characters

let set1 = /[abc]/;

console.log(set1.test('a'));
console.log(set1.test('f'));

// match anything but pattern

let set2 = /[^abc]/

console.log(set2.test('a'));
console.log(set2.test('f'));

// match in a sequence

let set3 = /[0-5]/;

console.log(set3.test(3)); 
console.log(set3.test(12345)); 
console.log(set3.test(9)); 
console.log(set3.test(6789)); 
console.log(/[0123456789]/.test("This is year 2015"));

// The exec() method takes a string as an argument and returns an array containing all matches

let str1 = 'A Toyota! Race fast, safe car! A Toyota!';
let str1_pat = /Toy/g;
let matches = str1_pat.exec(str1);
console.log(matches);

// the match method is similar
let matches2 = str1.match(str1_pat);
console.log(matches2);

let str2 = 'I like Vianney';
let str2_pat = /vianney/i;
console.log(str2.replace(str2_pat, 'Veronica'));

// replace also takes functions as arguments
console.log(str2.replace(str2_pat, function (){
  return 'veronica vianney';
}));

// split divides upon a regex and returns an array
let str3 = 'veronica,vianney,contreras';
let str3_pat = /\,/g;
let str3_arr = str3.split(str3_pat);
console.log(str3_arr);

// matching different kinds of patterns
// eg fat cat and bat
let multi_pat = /[fcb]at/gi;
let str4 = 'wooden bat, smelly Cat,a fat cat';
let multi_arr = str4.match(multi_pat);
console.log(multi_arr);

let nums = 'i1,i2,i3,i4,i5,i6,i7,i8,i9';
let num_re = /i[0-5]/g;
let num_arr = nums.match(num_re);
console.log(num_arr);

// some shorthand notations
// \d
	
// Any digit character

// \w
	
// An alphanumeric character (word character)

// \s
	
// Any whitespace character (space, tab, newline, and similar)

// \D
	
// A character that is not a digit

// \W
	
// A non-alphanumeric character

// \S
	
// A non-whitespace character

// .
	
// Any character except for newline

let try1 = '123-456-7890';
let try1_re = /\d\d\d\-\d\d\d/;
console.log(try1.match(try1_re)[0]);

// quantifiers
    //  ?: Either 0 or 1 occurrence (marks the occurrence as optional)

    // *: 0 or more occurrences

    // +: 1 or more occurrences

    // {n}: Exactly n occurrences

    // {n,m}: Occurrences between n and m

    // {n,}: At least an n occurrence

    // {,n}: 0 to n occurrences

// eg make u optional
let opt_re = /behaviou?r/;
console.log(opt_re.test('behaviour'));
console.log(opt_re.test('behavior'));

// repetition
let cow = "'moooooo'";
let cow_re = /o+/g;
console.log(cow_re.test(cow));

