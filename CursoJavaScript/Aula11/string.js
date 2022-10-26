//   indexado    01234567
let umaString = 'Um texto de novo';

console.log(umaString[4]);
console.log(umaString.charAt(4));
console.log(umaString.charCodeAt(4));
console.log(umaString + ' em um lindo dia.');
console.log(`${umaString} em um lindo dia.`);
console.log(umaString.indexOf('o', 3));
console.log(umaString.lastIndexOf('o'));
console.log(umaString.match(/[a-z]/));
console.log(umaString.replace(/um/, 'outra'));
console.log(umaString.length);
console.log(umaString.slice(2, 9));
console.log(umaString.split(''));
console.log(umaString.toUpperCase());
console.log(umaString.toLowerCase());
