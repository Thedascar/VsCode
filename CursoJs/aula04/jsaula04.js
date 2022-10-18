// aula 04 array

let produtos = ['Arroz','Feijão','Leite']
var codigos = Array(10,20,30)
let meses = ['Jan','Fev','Mar','Abr']
var test = Array(10)
test[0] = "OI"
test[9] = "Tudo Bem?"
test[10] = "Opa!"

//ADICIONAR no final push = empurre
produtos.push('Açucar')
codigos.push(40,50,60,70)
meses.push('Mai','Jun','Ago','07')
meses[0] = 'Janeiro'

// REMOVER do final pop = estourar
produtos.pop()
codigos.pop()
meses.pop()

//ADICIONAR no inicio unshift
produtos.unshift('Uva','Maça')

// REMOVER do inicia shift
produtos.shift()

// REMOVER de uma posição espeficifica splice
// splice = emendar
// posicção inicial, quantos remover
codigos.splice(1,3)

//COPIAR array slice = fatiar porção
// posição inicial, quantos copiar
let meses1 = meses.slice()
let meses2 = meses.slice(0,3)

// VER TAMANHO DO ARRAY length comprimento
meses.length
meses1.length
meses2.lenght

//spreed operator(...) copiar o conteúdo todo de um array

let teste = [...produtos,'Ovo','Pera']