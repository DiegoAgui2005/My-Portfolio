// Clase para manejar los cálculos del producto
class ProductoPrecio {
    constructor(materiaPrima, margenGanancia, impuestos) {
        this.materiaPrima = materiaPrima;
        this.margenGanancia = margenGanancia;
        this.impuestos = impuestos;
    }

    calcularPrecioBase() {
        return this.materiaPrima * (1 + this.margenGanancia / 100);
    }

    calcularPrecioFinal() {
        const precioBase = this.calcularPrecioBase();
        return precioBase * (1 + this.impuestos / 100);
    }

    calcularGananciaUnitaria() {
        return this.calcularPrecioFinal() - this.materiaPrima;
    }

    calcularGananciaTotal(cantidadVentas) {
        return this.calcularGananciaUnitaria() * cantidadVentas;
    }

    calcularDesglose() {
        const precioBase = this.calcularPrecioBase();
        const precioFinal = this.calcularPrecioFinal();
        const margenCalculado = precioBase - this.materiaPrima;
        const impuestosCalculados = precioFinal - precioBase;

        return {
            precioBase: this.materiaPrima,
            margenCalculado,
            impuestosCalculados
        };
    }
}

// Clase para manejar el historial de cálculos
class Historial {
    constructor() {
        this.calculos = JSON.parse(localStorage.getItem('calculosHistorial')) || [];
    }

    agregarCalculo(datos) {
        this.calculos.push({
            ...datos,
            fecha: new Date().toISOString()
        });
        this.guardarHistorial();
    }

    guardarHistorial() {
        localStorage.setItem('calculosHistorial', JSON.stringify(this.calculos));
    }

    obtenerHistorial() {
        return this.calculos;
    }
}

// Clase para manejar la interfaz de usuario
class UI {
    constructor() {
        this.form = document.getElementById('calculatorForm');
        this.results = document.getElementById('results');
        this.noResults = document.getElementById('noResults');
        this.historial = new Historial();

        this.inicializarEventos();
    }

    inicializarEventos() {
        this.form.addEventListener('submit', (e) => this.handleSubmit(e));
        document.getElementById('historialBtn').addEventListener('click', () => this.mostrarHistorial());
    }

    handleSubmit(e) {
        e.preventDefault();

        // Obtener valores del formulario
        const materiaPrima = parseFloat(document.getElementById('materiaPrima').value);
        const margenGanancia = parseFloat(document.getElementById('margenGanancia').value);
        const impuestos = parseFloat(document.getElementById('impuestos').value);
        const ventasEsperadas = parseInt(document.getElementById('ventasEsperadas').value);

        // Crear instancia de ProductoPrecio y realizar cálculos
        const producto = new ProductoPrecio(materiaPrima, margenGanancia, impuestos);
        const precioFinal = producto.calcularPrecioFinal();
        const desglose = producto.calcularDesglose();
        const gananciaTotal = producto.calcularGananciaTotal(ventasEsperadas);

        // Mostrar resultados
        this.mostrarResultados({
            precioFinal,
            desglose,
            ventasEsperadas,
            gananciaTotal
        });

        // Guardar en historial
        this.historial.agregarCalculo({
            materiaPrima,
            margenGanancia,
            impuestos,
            ventasEsperadas,
            precioFinal,
            gananciaTotal
        });
    }

    mostrarResultados(datos) {
        // Ocultar mensaje de no resultados
        this.noResults.classList.add('d-none');
        this.results.classList.remove('d-none');

        // Actualizar valores en la interfaz
        document.getElementById('precioFinal').textContent = this.formatearMoneda(datos.precioFinal);
        document.getElementById('costoBase').textContent = this.formatearMoneda(datos.desglose.precioBase);
        document.getElementById('margenCalculado').textContent = this.formatearMoneda(datos.desglose.margenCalculado);
        document.getElementById('impuestosCalculados').textContent = this.formatearMoneda(datos.desglose.impuestosCalculados);
        document.getElementById('ventasProyectadas').textContent = datos.ventasEsperadas;
        document.getElementById('gananciaTotal').textContent = this.formatearMoneda(datos.gananciaTotal);

        // Añadir animación
        this.animarResultados();
    }

    formatearMoneda(valor) {
        return new Intl.NumberFormat('es-MX', {
            style: 'currency',
            currency: 'MXN'
        }).format(valor);
    }

    animarResultados() {
        const resultItems = document.querySelectorAll('.result-item');
        resultItems.forEach((item, index) => {
            item.style.opacity = '0';
            setTimeout(() => {
                item.style.opacity = '1';
            }, index * 100);
        });
    }

    mostrarHistorial() {
        const historial = this.historial.obtenerHistorial();
        // Aquí puedes implementar la lógica para mostrar el historial en un modal o en otra vista
        console.log('Historial de cálculos:', historial);
    }
}

// Inicializar la aplicación cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    new UI();
}); 