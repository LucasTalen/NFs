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
    // const socket = io.connect("https://upright-filly-upward.ngrok-free.app/api")

    // socket.on('connect', () => {
    //     console.log('Conectado ao servidor WebSocket');
    //   });
    
    // socket.on('dados-extraidos', (data) => {
    
    // console.log('Dados recebidos:', data);
    // alert(data)
    
    // });

    // setInterval(() => {
    //     fetch('https://upright-filly-upward.ngrok-free.app/api')
    //       .then(response => response.json())
    //       .then(data => {
    //         // Manipular os dados recebidos aqui
    //         console.log(data);
    //       })
    //       .catch(error => {
    //         console.error('Erro ao buscar dados:', error);
    //       });
    //   }, 5000); // Realizar a consulta a cada 5 segundos (5000 milissegundos)
    


      const eventSource = new EventSource('https://upright-filly-upward.ngrok-free.app/api');

      eventSource.onmessage = (event) => {
        const data = JSON.parse(event.data);
        // Manipule os dados recebidos aqui
        console.log(data);
      };
      
      eventSource.onerror = (error) => {
        console.error('Erro de SSE:', error);
      };




    

}
