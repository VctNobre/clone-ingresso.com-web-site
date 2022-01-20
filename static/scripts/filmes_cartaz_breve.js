const cartaz = document.querySelector('[id=cartaz]')
const breve = document.querySelector('[id=breve]')
const listaCartaz = document.querySelector('[id=lista-cartaz]')
const listaBreve = document.querySelector('[id=lista-breve]')

const clickCartaz = () => {
    cartaz.classList.add('maps-active')
    listaCartaz.classList.remove('filmes-inativo')
    breve.classList.remove('maps-active')
    listaBreve.classList.add('filmes-inativo')

}

const clickBreve= () => {
    breve.classList.add('maps-active')
    listaBreve.classList.remove('filmes-inativo')
    cartaz.classList.remove('maps-active')
    listaCartaz.classList.add('filmes-inativo')

}

cartaz.addEventListener('click', clickCartaz);
breve.addEventListener('click', clickBreve);
