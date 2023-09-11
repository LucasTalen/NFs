let posicao_camera = 0
let camera = []
let scanner = null


function IniciarScaner(){
    // Pede permissão para acessara câmera, ele gera um erro caso a permisão seja negada
    Instascan.Camera.getcameraList().then(cameraList => {
        if (cameraList.length > 0) {
            cameras = cameraList;
            scanner = new Instascan.Scanner({ video: document.getElementById('preview')})

            scanner.addEventListener('scan', (content) => {
                retornaScan(content)
            })

            trocaCamera()
        }
        else{
            alert("Nenhuma camera disponivel")
        }

    });
    
}

function trocaCamera(){
    if (cameras.length ===0){
        alert("Nenhuma camera disponivel")
        return;
    }
    if (scanner){
        scanner.stop(cameras[posicao_camera])
    }
    posicao_camera = (posicao_camera + 1) % camera.length

    scanner.start(cameras[posicao_camera])
}




function desligaCamera(){
    if (scanner){
    scanner.stop(cameras[posicao_camera])
    }
}





let desliga = document.getElementById("desligar")
desliga.addEventListener('click', () => {
    scanner.stop(cameraList[posicao_camera])
})




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

const trocaCameraButton = document.getElementById('trocaCamera')
trocaCameraButton.addEventListener('click', trocaCamera)

const desligaButton = document.getElementById('desliga')
desligaButton.addEventListener('click', desligaCamera)
