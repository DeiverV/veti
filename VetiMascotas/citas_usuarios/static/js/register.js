let divNotifiAuth;
let vetNIT = document.querySelector("#label-NIT")
let esVet = document.querySelector("#es_vet")

esVet.addEventListener("click",()=>{
    if(esVet.checked){
        vetNIT.style.display="initial"
        vetNIT.firstElementChild.setAttribute("required",true)
    }else{
        vetNIT.style.display="none"
        vetNIT.firstElementChild.removeAttribute("required")
    }
})

if(document.querySelector("#notifi-auth")){
    divNotifiAuth=document.querySelector("#notifi-auth")
    setTimeout(()=>{
        divNotifiAuth.style.top="0"
    },1500)
    setTimeout(()=>{
        divNotifiAuth.style.top="-100%"
        setTimeout(()=>{
            divNotifiAuth.style.display="none"
        },300)
    },5000)
    console.log("hola")
}