let posicao_camera = 1
let cameraDisponivel;
let cameraSelecionada = 0;
// Pede permissão para acessara câmera, ele gera um erro caso a permisão seja negada
Instascan.Camera.getCameras().then(cameras => {
    if (cameras.length > 0) {
        var cameraDisponivel = cameras.filter(camera => camera.id)
        console.log(cameraDisponivel)
        
        scanner.start(cameraDisponivel[1]);
        console.log(cameraSelecionada)
    }
});

let trocaCamera = document.getElementById("trocaCamera")
trocaCamera.addEventListener('click', () => {
 
   cameraSelecionada = (cameraSelecionada + 1) % cameraDisponivel
   console.log(cameraDisponivel)
   console.log(cameraSelecionada)

    scanner.start(cameraDisponivel[cameraSelecionada]);

})


let desliga = document.getElementById("desligar")
desliga.addEventListener('click', () => {
    scanner.stop(cameras[posicao_camera])
})



// Liga a câmera com o front-end, para a visualização do usuário
let scanner = new Instascan.Scanner({
    video: document.getElementById('preview')
});

// Verifica quando um QR code for escaneado
scanner.addListener('scan', function (content) {

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


