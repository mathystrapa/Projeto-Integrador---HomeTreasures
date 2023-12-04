var formSignin = document.querySelector('#signin')
var formSignup = document.querySelector('#signup')
var btnColor = document.querySelector('.btnColor')

document.querySelector('#btnSignin')
  .addEventListener('click', () => {
    formSignin.style.left = "25px"
    formSignup.style.left = "450px"
    btnColor.style.left = "0px"
})

document.querySelector('#btnSignup')
  .addEventListener('click', () => {
    formSignin.style.left = "-450px"
    formSignup.style.left = "25px"
    btnColor.style.left = "110px"
})


// barra de pesquisa
const input = document.getElementById("barra");
                    input.addEventListener("keyup", function(event) {
                      if (event.keyCode === 13) {
                        event.preventDefault();
                        if (input.value === "") {
                          alert("Por favor, digite algo para pesquisar.");
                        } else {
                          alert("Você pesquisou por: " + input.value);
                          // Substitua o alert acima com a sua lógica de pesquisa
    }
   }
});


// Função para adicionar ao carrinho
function adicionarAoCarrinho(nome_produto) {
  window.location.href = '/adicionar-ao-carrinho/' + nome_produto;
}

// Função para remover do carrinho
function removerDoCarrinho(nome_produto) {
  window.location.href = '/remover-do-carrinho/' + nome_produto;
}