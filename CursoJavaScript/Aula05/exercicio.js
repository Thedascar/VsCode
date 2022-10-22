//Lucas Ramon tem 27 anos, pesa 84kg
// tem 1.8 de altura e seu IMC é de 25.90

let nome = 'Lucas Ramon';
let idade = 27;
let peso = 76;
let altura = 1.65;

let imc = peso / (altura * altura);
let imc2 = imc.toFixed('2')

console.log(`Meu nome é ${nome}`);
console.log(`Minha idade é ${idade}`);
console.log(`Eu peso ${peso}`);
console.log(`Minha altura é de ${altura}`);
console.log(`Minha faixa de IMC é ${imc2}`);
