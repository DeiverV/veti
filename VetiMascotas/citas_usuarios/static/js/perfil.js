let divCrearMascota = document.querySelector("#crear-mascota-perfil")
let btnAbrirCrearMascota = document.querySelector("#abrir-crear-mascota-btn")
let btnCerrarCrearMascota = document.querySelector("#cerrar-cmascota")

let divEditarMascota = document.querySelector("#editar-mascota-perfil")
let btnAbrirEditarMascota = document.querySelector("#abrir-editar-mascota")
let btnCerrarEditarMascota = document.querySelector("#cerrar-emascota")

btnAbrirCrearMascota.addEventListener("click",()=>{
        divCrearMascota.style.width="100%"
        divCrearMascota.style.height="100%"
})

btnCerrarCrearMascota.addEventListener("click",()=>{
        divCrearMascota.style.width="0"
        divCrearMascota.style.height="0"
})

if(btnAbrirEditarMascota){
        btnAbrirEditarMascota.addEventListener("click",()=>{
                divEditarMascota.style.width="100%"
                divEditarMascota.style.height="100%"
        })

        btnCerrarEditarMascota.addEventListener("click",()=>{
                divEditarMascota.style.width="0"
                divEditarMascota.style.height="0"
        })
}




