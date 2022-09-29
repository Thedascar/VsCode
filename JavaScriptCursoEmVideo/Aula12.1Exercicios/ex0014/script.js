function carregar(){
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var horas = data.getHours()
    horas = 14
    msg.innerHTML = `Agora são ${horas} horas.`
    if (horas > 0 && horas < 12){
        img.src = "manha.png"
        document.body.style.background = '#e2cd9f'
    } else if (horas >= 12 && horas < 18){
        img.src = "tarde.png"
        document.body.style.background = '#b9846f'
    } else if (horas >=0 && horas < 5 ) {
        img.src = "madrugada.jpg"
        document.body.style.background = 'black'
    } else {
        img.src = "noite.png"
        document.body.style.background = '#515154'
    }
}
