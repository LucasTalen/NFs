
// Pede permissão para acessara câmera, ele gera um erro caso a permisão seja negada
Instascan.Camera.getCameras().then(cameras => {
    if (cameras.length > 0) {
        alert(cameras)
        scanner.start(cameras[1]);
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
}

