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



function consumirAPI() {
    const apiUrl = 'https://upright-filly-upward.ngrok-free.app/api?url=https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml?p=31230713574594030508650010005249781378283311|2|1|1|9CB061C0D016DBEDA8D27E6E20F4BA26025FF4A9';

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
           
            const dadosApi = document.getElementById('dados-api');
            dadosApi.innerHTML = `
                <p>Loja: ${data.loja}</p>
                <p>Preço: R$ ${data.preco.toFixed(2)}</p>
            `;
        })
        .catch(error => {
            console.error('Ocorreu um erro ao consumir a API:', error);
        });
}


const enviarBotao = document.getElementById('enviar');
enviarBotao.addEventListener('click', consumirAPI);
