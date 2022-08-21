const tarjetasDevs = document.querySelectorAll(".contenedor-info-developer")
let odd = false

const apareceTarjeta = (tarjeta) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if(!odd){
                tarjeta.style.right="0"
                odd=true
            }else{
                tarjeta.style.left="0"
                odd=false
            }
            return resolve()
        }, 1000);
    });
}

if(tarjetasDevs){
    window.addEventListener("load",() =>{
        (async ()=> {
            for(let tarjeta of tarjetasDevs){
                await apareceTarjeta(tarjeta)
            }
        })();
    })
}