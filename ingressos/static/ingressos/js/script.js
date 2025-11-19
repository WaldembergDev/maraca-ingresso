
document.addEventListener('DOMContentLoaded', function(){
    // obtendo o token 
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    // declarando as variáveis
    let botoes = document.querySelectorAll('.btn-ingresso');
    let modal = document.getElementById('modal');
    let modalBootstrap = new bootstrap.Modal(modal);
    const csrfToken = getCookie('XSRF-TOKEN');

    botoes.forEach(botao => {
        botao.addEventListener('click', function(){
            let idHistorico = botao.dataset.id;
            let urlIngresso = `/ingressos/json-detalhes-compra/${idHistorico}`
            // realizando requisição para a api do django
            fetch(urlIngresso, {
                headers: {
                    'X-CSRF-TOKEN': csrfToken,
                    'Content-Type': 'application/json'
                }
            }).then(response =>{
                if (response.ok){
                    return response.json();
                }else{
                    alert('Erro ao realizar requisição');
                }
            }).then(json =>{
                // obtendo as variaveis do modal
                let titulo = document.getElementById('tituloId');
                let local = document.getElementById('localId');
                let dataCompraId = document.getElementById('dataCompraId');
                let valorPagoId = document.getElementById('valorPagoId');
                let quantidadeId = document.getElementById('quantidadeId');

                // salvando os dados no modal
                titulo.textContent = json.titulo;
                local.textContent = json.local;
                dataCompraId.textContent = json.data_compra;
                valorPagoId.textContent = json.valor_pago;
                quantidadeId.textContent = json.quantidade;
                modalBootstrap.show();
            }).catch(erro =>{
                console.log(erro)
            })              
        })
    })
});
