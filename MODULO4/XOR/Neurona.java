package practicas.topicosIA.MODULO4.XOR;

import java.util.ArrayList;
import java.util.Random;

public class Neurona {
    private ArrayList<Input> inputs = new ArrayList<>();
    private final double UMBRAL = 0.2;
    private final double TASA_APRENDIZAJE = 0.1;

    public Neurona(int nEntradas) {

        //asignar pesos iniciales
        for (int i = 0; i < nEntradas; i++) {
            double pesoInicial = new Random().nextDouble(-0.5, 0.5);
            inputs.add(new Input(pesoInicial, 0));
        }
    }

    public int calcularSalida(int[] entradas) {
        double output = 0;

        for (int i = 0; i < inputs.size(); i++) {
            inputs.get(i).setValor(entradas[i]);
        }

        for(Input entrada : this.inputs)
            output += entrada.valor()*entrada.peso();
        output -= UMBRAL;
        return output > 0 ? 1 : 0;
    }

    public void actualizarPesos(int error){
        for (Input input : inputs) {
            double nuevoPeso = input.peso() + (TASA_APRENDIZAJE * input.valor() * error);
            input.setPeso(nuevoPeso);
        }
    }


    class Input {
        private double peso;
        private double valor;

        public Input(double peso, double valor) {
            this.peso = peso;
            this.valor = valor;
        }

        public double peso() {
            return peso;
        }

        public double valor() {
            return valor;
        }

        public void setValor(double valor) {
            this.valor = valor;
        }
        public void setPeso(double peso) {
            this.peso = peso;
        }
    }

    
    public ArrayList<Input> getInputs() {
        return inputs;
    }

    public void setInputs(ArrayList<Input> inputs) {
        this.inputs = inputs;
    }
}
