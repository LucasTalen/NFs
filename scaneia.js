let posicao_camera = 1
let cameraDisponivel;
let cameraSelecionada = 0;
let cameraLivre;
// Pede permissão para acessara câmera, ele gera um erro caso a permisão seja negada
Instascan.Camera.getCameras().then(cameras => {
    if (cameras.length > 0) {
        cameraDisponivel = cameras.filter(camera => camera.id)

        scanner.start(cameras[cameraSelecionada]);
        cameraDisponivel = cameras.filter(camera => camera.id)
        cameraLivre = cameraDisponivel.length
        
    }
});

let trocaCamera = document.getElementById("trocaCamera")
trocaCamera.addEventListener('click', () => {
    scanner.stop()
   cameraSelecionada = (cameraSelecionada + 1) % cameraLivre

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

    consumirAPI(content)
    content = ""
});



//----------------------------------------------------------



















function consumirAPI(url) {
    const apiUrl = `https://upright-filly-upward.ngrok-free.app/api?url=${url}`;

    
    fetch(apiUrl, {
        headers: {
            'ngrok-skip-browser-warning': 'true'
        }
    })
        .then(response => response.text())
        .then(data => {

            console.log(data);
        })
        .catch(error => {
            console.error('Ocorreu um erro ao consumir a API:', error);
        });
}


function montarTabela(dados){
    tabela = document.getElementById("tabela")


}