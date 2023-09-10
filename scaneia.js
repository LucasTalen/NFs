let posicao_camera = 0



function trocaCamera(){

    // Pede permissão para acessara câmera, ele gera um erro caso a permisão seja negada
    Instascan.Camera.getCameras().then(cameras => {
        if (cameras.length > 0) {
            alert(cameras)
            if (!Camera.length > posicao_camera){
                posicao_camera += 1
              }else{
                posicao_camera -= 1
              }
            scanner.start(cameras[posicao_camera]);
        }
    });

    console.log(posicao_camera)


}


// // Pede permissão para acessara câmera, ele gera um erro caso a permisão seja negada
// Instascan.Camera.getCameras().then(cameras => {
//     if (cameras.length > 0) {
//         alert(cameras)
//         scanner.start(cameras[posicao_camera]);
//     }
// });

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


function enviarCodigoQR(){
    const socket = io.connect("https://upright-filly-upward.ngrok-free.app/api")

    socket.on('connect', () => {
        console.log('Conectado ao servidor WebSocket');
      });
    
    socket.on('dados-extraidos', (data) => {
    
    console.log('Dados recebidos:', data);
    alert(data)
    
    });
    

}
