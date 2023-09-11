let posicao_camera = 1
let desliga = document.getElementById("desligar")
desliga.addEventListener('click', () => {
    scanner.stop(cameras[posicao_camera])
})

let trocaCamera = document.getElementById("trocaCamera")
trocaCamera.addEventListener('click', () => {
    scanner.stop(cameras[posicao_camera])
    if (cameras.length == posicao_camera){
        alert("Posição atual das cameras é o limite")
        posicao_camera = 1
        scanner.start(cameras[posicao_camera])
    }
    else{
        posicao_camera += 1
        scanner.start(cameras[posicao_camera])
        alert(`Posição atual das cameras é ${posicao_camera}`)
    }
})
// Pede permissão para acessara câmera, ele gera um erro caso a permisão seja negada
Instascan.Camera.getCameras().then(cameras => {
    if (cameras.length > 0) {
  
        alert(cameras.length)
        alert(posicao_camera)
        scanner.start(cameras[posicao_camera]);
    }
});


// Liga a câmera com o front-end, para a visualização do usuário
let scanner = new Instascan.Scanner({
    video: document.getElementById('preview')
});

// Verifica quando um QR code for escaneado
scanner.addListener('scan', function (content) {
    
    // alert('Escaneou o conteudo: ' + content);
    
    retornaScan(content);
    content = ""
});

// Função para passar o valor do código QR como uma função (retorna o valor do QR)

function retornaScan(codigoQr) {
    alert(codigoQr);
    consumirAPI(codigoQr)
}



function consumirAPI(url) {
    const apiUrl = `https://upright-filly-upward.ngrok-free.app/api?url=${url}`;

    
    fetch(apiUrl, {
        headers: {
            'ngrok-skip-browser-warning': 'true'
        }
    })
        .then(response => response.json())
        .then(data => {
            const dadosApi = document.getElementById('dados-api');
            dadosApi.innerHTML = `
                <p>Loja: ${data.loja}</p>
                <p>Preço: R$ ${data.preco}</p>
                
            `;
            console.log(data);
        })
        .catch(error => {
            console.error('Ocorreu um erro ao consumir a API:', error);
        });
}


const enviarBotao = document.getElementById('enviar');
enviarBotao.addEventListener('click', consumirAPI);
