let divCrearMascota = document.querySelector("#crear-mascota-perfil")
let btnAbrirCrearMascota = document.querySelector("#abrir-crear-mascota-btn")
let btnCerrarCrearMascota = document.querySelector("#cerrar-cmascota")

btnAbrirCrearMascota.addEventListener("click",()=>{
        divCrearMascota.style.width="100%"
        divCrearMascota.style.height="100%"
})

btnCerrarCrearMascota.addEventListener("click",()=>{
        divCrearMascota.style.width="0"
        divCrearMascota.style.height="0"
})


