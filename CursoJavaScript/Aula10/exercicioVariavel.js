let varA = 'A'; //B
let varB = 'B'; // C
let varC = 'C'; // A

/*
let a = varA;
let soma = varA = varB;
let soma2 = varB = varC;
console.log(soma , soma2 , a)
*/


// Novo Metódo de resolução em J

[varA, varB , varC] = [varB , varC, varA];
console.log(varA,varB,varC);