//Generador de contraseñas
let cantidad = document.getElementById("cantidad");
let boton = document.getElementById("generar");
let boton_limpiar = document.getElementById("limpiar");
let contraseña = document.getElementById('contrasena');

const cadenaCaracteres = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz!@#$%^&*()0123456789';

alert("Este generador de contraseñas te permite crear claves seguras.\n\nTan solo ingresa un número igual o mayor a 8 en el campo Cantidad.\n\nProyecto optimizado por Jonathan Saravia.")

function generar(){
    let numeroDigitado =  parseInt(cantidad.value);
    console.log(numeroDigitado);
    let password = '';
    let comprobarpassword = false;
    if(isNaN(numeroDigitado)){
        alert("Dato incorrecto. Intenta nuevamente.")
    } else {
        for(let i=0; i < numeroDigitado; i++){
            if(numeroDigitado < 8){
                alert("No se puede generar la contraseña.\nLa cantidad de catacteres tiene que ser mayor o igual a 8\nIntenta nuevamente.");
                break;
            } else {
                let caracterAleatorio =  cadenaCaracteres[Math.floor(Math.random() * cadenaCaracteres.length)];
                console.log(caracterAleatorio);
                password+=caracterAleatorio;
                comprobarpassword = true;
            }
    }
    if(comprobarpassword == true){
        comprobarContrasena(password);
    }
    }
}

function comprobarContrasena(password){
    contrasena.value = password;
    const tieneNumero = /\d/.test(contrasena.value);
    const tieneMayusculas = /[A-Z]/.test(contrasena.value);
    if(tieneNumero && tieneMayusculas){
        alert("Contraseña Fuerte.\nLa contraseña incluye al menos un número y una mayúsculas.");
    } else{
        alert("Contraseña Débil.\nLa contraseña no incluye al menos un número ni una mayúsculas.\nInténtalo de nuevo.")
    }
}

function limpiar(){
    if (cantidad.value=='' && cantidad.value ==''){
        alert("Error: no hay datos previamente ingresados.");
    } else {
        contrasena.value = '';
        cantidad.value='';
        alert("Se borraron los datos exitosamente.");
    }
}








