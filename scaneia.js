let posicao_camera = 1

function trocaCamera(){

    // Pede permissão para acessara câmera, ele gera um erro caso a permisão seja negada
    Instascan.Camera.getCameras().then(cameras => {
        if (cameras.length > 0) {
            alert(cameras)
            if (!cameras.length > posicao_camera){
                posicao_camera += 1
            }
            else{
                posicao_camera -= 1
            }
            console.log(scanner.activeCameraId = cameras[0].id)
            scanner.start(cameras[posicao_camera]);
        }
    });
    console.log(cameras.length)
    console.log(posicao_camera)

}

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
}


const fetch = require('fetch');

// Faz a chamada à API
const response = await fetch('https://upright-filly-upward.ngrok-free.app/api');

// Espera até que a resposta seja recebida
response.then(res => {
    if (res.status === 200) {
        // Decodifica o JSON
        const data = await res.json();

        // Exibe o JSON
        console.log(data);
    } else {
        console.log('Erro: ', res.status);
    }
});

    


