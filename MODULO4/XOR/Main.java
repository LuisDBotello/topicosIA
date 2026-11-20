package practicas.topicosIA.MODULO4.XOR;

public class Main {
    public static void main(String[] args) {
        int epocas = 20;
        int[][] entradas = {
            {0, 0},
            {0, 1},
            {1, 0},
            {1, 1}
        };

        int[] salidasEsperadas = {
            0,
            1,
            1,
            0
        };

        Layer layer = new Layer(1, 2);
        layer.entrenar(entradas, salidasEsperadas, epocas);
    }
}
