const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Función para calcular el precio final del producto
function calcularPrecioFinal(costoMateriaPrima, margenGanancia, impuestos) {
    // Calculamos el precio base añadiendo el margen de ganancia
    const precioBase = costoMateriaPrima * (1 + margenGanancia / 100);
    
    // Calculamos el precio final añadiendo los impuestos
    const precioFinal = precioBase * (1 + impuestos / 100);
    
    return precioFinal;
}

// Función para calcular la ganancia total esperada
function calcularGananciaEsperada(precioFinal, costoMateriaPrima, cantidadVentas) {
    const gananciaUnitaria = precioFinal - costoMateriaPrima;
    const gananciaTotal = gananciaUnitaria * cantidadVentas;
    return gananciaTotal;
}

// Función principal que maneja la interacción con el usuario
function main() {
    console.log("=== Calculadora de Precios y Ganancias ===\n");
    
    rl.question("Ingrese el costo de la materia prima: ", (costoMateriaPrima) => {
        rl.question("Ingrese el margen de ganancia deseado (%): ", (margenGanancia) => {
            rl.question("Ingrese el porcentaje de impuestos (%): ", (impuestos) => {
                // Convertimos las entradas a números
                costoMateriaPrima = parseFloat(costoMateriaPrima);
                margenGanancia = parseFloat(margenGanancia);
                impuestos = parseFloat(impuestos);

                // Calculamos el precio final
                const precioFinal = calcularPrecioFinal(costoMateriaPrima, margenGanancia, impuestos);
                
                // Mostramos el resultado del precio
                console.log("\n=== Resultados del Precio ===");
                console.log(`Costo de materia prima: $${costoMateriaPrima.toFixed(2)}`);
                console.log(`Margen de ganancia: ${margenGanancia}%`);
                console.log(`Impuestos: ${impuestos}%`);
                console.log(`Precio final sugerido: $${precioFinal.toFixed(2)}\n`);
                
                rl.question("¿Cuántas ventas espera realizar? ", (ventasEsperadas) => {
                    ventasEsperadas = parseInt(ventasEsperadas);
                    
                    // Calculamos y mostramos la ganancia esperada
                    const gananciaTotal = calcularGananciaEsperada(precioFinal, costoMateriaPrima, ventasEsperadas);
                    
                    console.log("\n=== Proyección de Ganancias ===");
                    console.log(`Cantidad de ventas esperadas: ${ventasEsperadas}`);
                    console.log(`Ganancia total esperada: $${gananciaTotal.toFixed(2)}`);
                    
                    rl.close();
                });
            });
        });
    });
}

// Ejecutamos el programa
main();
