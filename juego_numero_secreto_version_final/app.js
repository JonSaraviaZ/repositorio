let numeroSecreto= 0;
let intentos=0;
let listaNumerosSorteados=[];
let numeroMaximo=10;

console.log(numeroSecreto);

function asignarTextoElemento(elemento,texto){
    let elementoHTML = document.querySelector(elemento);
    elementoHTML.innerHTML = texto;
    return;
}

function verificarIntento(){
    //al encerrar en el parámetro en parseInt se transforma el string en un número entero.
    let numeroDeUsuario = parseInt(document.getElementById('valorUsuario').value);
    // Con el === se le pide a la máquina que la comparación tiene que ser igual en valor y en tipo de datos.
    ///console.log(numeroDeUsuario === numeroSecreto);
    //Con esto puedo utilizar una sola función, previamente definida, para encontrar el número secreto.
    if (numeroDeUsuario === numeroSecreto){
        asignarTextoElemento('p',`Acertaste el número en ${intentos} ${(intentos===1) ?'vez':'veces'}`);
        //con este código document.getElementById('reiniciar').removeAttribute('disabled') se puede remover
        //el atributo que tenga un elemento de HTML en Javascript
        document.getElementById('reiniciar').removeAttribute('disabled');
    } else{
        //el usuario no acertó
        if (numeroDeUsuario>numeroSecreto){
            asignarTextoElemento('p','El número secreto es menor');
        } else{
            asignarTextoElemento('p','El número secreto es mayor');
        }
        intentos++;
        limpiarCaja();
    }
    return;
}

//Con la función limpiar caja se elimina automáticamente el número no acertado del usuario
function limpiarCaja(){
    document.querySelector('#valorUsuario').value='';
}

function generarNumeroSecreto() {
    let numeroGenerado= Math.floor(Math.random()*numeroMaximo)+1;
    console.log(numeroGenerado);
    console.log(listaNumerosSorteados);
    // Si ya sorteamos todos los números
    if (listaNumerosSorteados.length == numeroMaximo){
        asignarTextoElemento('p','Ya se sortearon todos los números posibles');
    } else{
        // Si el número generado está incluido en la lista
        if (listaNumerosSorteados.includes(numeroGenerado)){
            //en Javascript se puede llamar a si misma una lista para que ejecute la acción principal
            //Esto es recursividad
            return generarNumeroSecreto();
        } else {
            listaNumerosSorteados.push(numeroGenerado);
            return numeroGenerado;
        }
    }
}

function condicionesIniciales() {
    asignarTextoElemento('h1','Juego del número secreto!');
    asignarTextoElemento('p',`Indica un número del 1 al ${numeroMaximo}`);
    numeroSecreto=generarNumeroSecreto();
    intentos=1;
}

function reiniciarJuego() {
    //Limpiar la caja
    limpiarCaja();
    //Indicar mensaje de intervalo de números
    //Generar el número aleatorio
    //Inicializar el número intentos
    condicionesIniciales();
    //Deshabilitar el botón de nuevo juego
    //setAttribute agrega un atributo a un elemento y pide dos parámetros,
    //primero configuramos el valor del elemento y con un valor (tiende a ser true o false)
    document.querySelector('#reiniciar').setAttribute('disabled','true');
}

condicionesIniciales();
