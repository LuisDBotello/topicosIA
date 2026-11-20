package practicas.topicosIA.MODULO4.XOR;

public class Layer {
    private Neurona[] neuronas;

    public Layer(int nNeuronas, int nEntradas) {
        neuronas = new Neurona[nNeuronas];
        for (int i = 0; i < nNeuronas; i++) {
            neuronas[i] = new Neurona(nEntradas);
        }
    }

    public void entrenar(int[][] inputs, int[] salidasEsperadas, int epocas) {
        
        for (Neurona neurona : neuronas)
            for (int epoca = 0; epoca < epocas; epoca++) 
                for (int i = 0; i < inputs.length; i++) {
                    int[] entradas = inputs[i]; //entradas = par de bits
                    int salidaEsperada = salidasEsperadas[i]; 
                    
                    double[] pesosIniciales = neurona.getInputs().stream().mapToDouble(Neurona.Input::peso).toArray();
                    
                    // Calcular la salida de cada neurona
                    int salidaActual = neurona.calcularSalida(entradas);
                    int error = salidaEsperada - salidaActual;

                    // Actualizar los pesos de cada neurona
                    neurona.actualizarPesos(error);
                    System.out.println(String.format("Entradas: %s, Salida Esperada: %d, Pesos iniciales: %s, Salida Actual: %d, Error: %d, Pesos finales: %s", java.util.Arrays.toString(entradas), salidaEsperada, java.util.Arrays.toString(pesosIniciales), salidaActual, error, java.util.Arrays.toString(neurona.getInputs().stream().map(Neurona.Input::peso).toArray())));
                }
            
    }
}
