//con document.querySelector('nombre del selector en HTML') se hace la conexión con el objeto de HTML 
// Se asigna a una variable (titulo) 
//let titulo = document.querySelector('h1');
// a la variable se le puede asignar un valor, como un string, con "inner.HTML"
//titulo.innerHTML = 'Juego del número secreto ';

//let parrafo = document.querySelector('p')
//parrafo.innerHTML='Indica un número del 1 al 10'

// Se puede usar arrays o listas en Javascript
// Estas pueden tener distintos datos. Se sugiere que una lista contenga solo un tipo de dato y otra lista otro tipo de dato
// El array se declara con let (nombre del array) = [] 
//ejemplo let numerosSorteados=[];

//Para agregar un elemento al final del array se usa el método push
//numerosSorteados.push(5);
//numerosSorteados=[5];

//Para saber el tamaño o cantidad de elementos en un array, se ocupa
//console.log(numerosSorteados.length);
//El resultado será 1, ya que solo se ha ingresado un elemento.

//Se puede acceder a un elemento con la ayuda del índice
//Se puede hacer de esta forma console.log(numerosSorteados[0])
//La posición 0 siempre es el primer elemento.

//Podemos pedir el último elemento de la lista de esta forma:
//console.log(numerosSorteados[numerosSorteados.length]-1);

//Se puede eliminar el últimmo elemento de un array con pop
//De esta manera numerosSorteados.pop();

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
    //console.log(typeof(numeroSecreto))
    //console.log(numeroSecreto);
    //console.log(typeof(numeroDeUsuario))
    //console.log(numeroDeUsuario);
    // Con el === se le pide a la máquina que la comparación tiene que ser igual en valor y en tipo de datos.
    ///console.log(numeroDeUsuario === numeroSecreto);
    //Con esto puedo utilizar una sola función, previamente definida, para encontrar el número secreto.
    if (numeroDeUsuario === numeroSecreto){
        asignarTextoElemento('p',`Acertaste el número en ${intentos} ${(intentos===1) ?'vez':'veces'}`);
        //con este código document.getElementById('reiniciar').removeAttribute('disabled') se puede remover
        //el atributo que tenga un elemento de HTML en Javascript
        document.getElementById('reiniciar').removeAttribute('disabled');
    } else{
        //console.log(intentos)
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
    //Con que document.querySelector('#valorUsuario') también se puede llamar al ID
    //let valorCaja= document.querySelector('#valorUsuario');
    //valorCaja.value='';
    //Esta es una forma más abreviada del código anterior.
    document.querySelector('#valorUsuario').value='';
}

//al escribir solo function, VS Code entrega la opción de function statement que genera la anatomía básica de toda función
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