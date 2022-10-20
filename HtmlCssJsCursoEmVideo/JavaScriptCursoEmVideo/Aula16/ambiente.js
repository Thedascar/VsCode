let num = [5,8,2,9,3]
num[3] = 6
num.push(7)
num.push(1)
num.sort()
console.log(num)
console.log(`O vetor tem ${num.length} posições `)
console.log(`O primeiro valor do vetor é ${num[0]}`)

for(let i=0; i < num.length; i+= 1){
    console.log(`O numero ${num[i]} esta na posição ${i}`)
}