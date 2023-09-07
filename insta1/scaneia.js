function criarTabela(tab){

    let tabelaDiv = document.getElementById('tabela');
    
    let tabelaExistente = document.getElementById('minha-tabela');
    
    if (tabelaExistente) {
        tabelaExistente.innerHTML = tab;
    } else {
        let div = document.createElement('div');
        div.id = 'minha-tabela';
        div.innerHTML = tab;
        tabelaDiv.appendChild(div);
    }
    
      
}


function serve(codigo){
const socket = new WebSocket('ws://localhost:8765');

socket.onopen = () => {
  console.log('Conexão estabelecida com o servidor WebSocket');
  
  const data = codigo;
  socket.send(data);  // Envia os dados para o servidor Python
};

socket.onmessage = (event) => {
  const result = event.data;  // Recebe o resultado enviado pelo servidor Python
  console.log('Resultado recebido do Python:', result);
  criarTabela(result)
};

socket.onclose = () => {
  console.log('Conexão com o servidor WebSocket encerrada');
};
}
// Pede permissão para acessara câmera, ele gera um erro caso a permisão seja negada
Instascan.Camera.getCameras().then(cameras => {
    if (cameras.length > 0) {
        
        scanner.start(cameras[0]);
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
    console.log(codigoQr);
    serve(codigoQr)
}

