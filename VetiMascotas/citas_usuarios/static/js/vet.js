const btnSliderCertifNext = document.querySelector("#next-certificate")
const btnSliderCertifPrev = document.querySelector("#prev-certificate")
const sliderCertificados = document.querySelector("#contenedor-certificados")
let slider = window.getComputedStyle(sliderCertificados);


btnSliderCertifNext.addEventListener("click",(e)=>{
    e.preventDefault()
    let leftSlider = slider.getPropertyValue('left');
    leftSlider = parseInt(leftSlider)-300
    sliderCertificados.style.left=`${leftSlider}px`
})

btnSliderCertifPrev.addEventListener("click",(e)=>{
    e.preventDefault()
    let leftSlider = slider.getPropertyValue('left');
    leftSlider = parseInt(leftSlider)+300
    sliderCertificados.style.left=`${leftSlider}px`
})

const btnSliderLocalesfNext = document.querySelector("#next-local")
const btnSliderLocalesPrev = document.querySelector("#prev-local")
const sliderLocales = document.querySelector("#contenedor-locales")
let locales = window.getComputedStyle(sliderLocales);


btnSliderLocalesfNext.addEventListener("click",(e)=>{
    e.preventDefault()
    let leftSliderLocales = locales.getPropertyValue('left');
    leftSliderLocales = parseInt(leftSliderLocales)-300
    sliderLocales.style.left=`${leftSliderLocales}px`
})

btnSliderLocalesPrev.addEventListener("click",(e)=>{
    e.preventDefault()
    let leftSliderLocales = locales.getPropertyValue('left');
    leftSliderLocales = parseInt(leftSliderLocales)+300
    sliderLocales.style.left=`${leftSliderLocales}px`
})


let divCrearCertificado = document.querySelector("#crear-certificacion-vet")
let btnAbrirCrearCertificado = document.querySelector("#abrir-crear-certificado")
let btnCerrarCrearCertificado = document.querySelector("#cerrar-cvet")

btnAbrirCrearCertificado.addEventListener("click",()=>{
    divCrearCertificado.style.width="100%"
    divCrearCertificado.style.height="100%"
})

btnCerrarCrearCertificado.addEventListener("click",()=>{
    divCrearCertificado.style.width="0"
    divCrearCertificado.style.height="0"
})

let divCrearLocal = document.querySelector("#crear-local-vet")
let btnAbrirCrearLocal = document.querySelector("#abrir-crear-local")
let btnCerrarCrearLocal = document.querySelector("#cerrar-lvet")


btnAbrirCrearLocal.addEventListener("click",()=>{
    divCrearLocal.style.width="100%"
    divCrearLocal.style.height="100%"
})

btnCerrarCrearLocal.addEventListener("click",()=>{
    divCrearLocal.style.width="0"
    divCrearLocal.style.height="0"
})


let divCrearCita = document.querySelector("#crear-cita-vet")
let btnAbrirCrearCita  = document.querySelector("#abrir-crear-cita")
let btnCerrarCrearCita = document.querySelector("#cerrar-citavet")


btnAbrirCrearCita.addEventListener("click",()=>{
    divCrearCita.style.width="100%"
    divCrearCita.style.height="100%"
})

btnCerrarCrearCita.addEventListener("click",()=>{
    divCrearCita.style.width="0"
    divCrearCita.style.height="0"
})