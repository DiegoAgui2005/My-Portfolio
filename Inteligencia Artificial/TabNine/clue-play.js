class RuletaDeLaFortuna {
    constructor() {
        this.saldo = 1000; // Saldo inicial del jugador
    }

    girarRuleta() {
        return Math.floor(Math.random() * 36) + 1;
    }

    apostar() {
        let numero;
        do {
            numero = parseInt(prompt("Elige un número entre 1 y 36:"));
            if (isNaN(numero) || numero < 1 || numero > 36) {
                alert("Por favor, elige un número válido entre 1 y 36.");
            }
        } while (isNaN(numero) || numero < 1 || numero > 36);
        return numero;
    }

    cantidadApuesta() {
        let cantidad;
        do {
            cantidad = parseInt(prompt(`¿Cuánto quieres apostar? (Saldo actual: $${this.saldo}):`));
            if (isNaN(cantidad) || cantidad <= 0 || cantidad > this.saldo) {
                alert(`Por favor, apuesta una cantidad válida entre 1 y ${this.saldo}.`);
            }
        } while (isNaN(cantidad) || cantidad <= 0 || cantidad > this.saldo);
        return cantidad;
    }

    jugar() {
        alert("¡Bienvenido a la Ruleta de la Fortuna!");
        
        while (this.saldo > 0) {
            alert(`Tu saldo actual es: $${this.saldo}`);
            let numeroApostado = this.apostar();
            let cantidad = this.cantidadApuesta();
            
            let numeroGanador = this.girarRuleta();
            alert(`La ruleta se detiene en el número: ${numeroGanador}`);
            
            if (numeroApostado === numeroGanador) {
                let ganancia = cantidad * 35;
                this.saldo += ganancia;
                alert(`¡Felicidades! Has ganado $${ganancia}`);
            } else {
                this.saldo -= cantidad;
                alert(`Lo siento, has perdido $${cantidad}`);
            }
            
            if (this.saldo <= 0) {
                alert("¡Oh no! Te has quedado sin saldo.");
                break;
            }
            
            let jugarDeNuevo = confirm("¿Quieres jugar otra vez?");
            if (!jugarDeNuevo) {
                break;
            }
        }

        alert(`Juego terminado. Tu saldo final es: $${this.saldo}`);
    }
}

// Iniciar el juego
let juego = new RuletaDeLaFortuna();
juego.jugar();
