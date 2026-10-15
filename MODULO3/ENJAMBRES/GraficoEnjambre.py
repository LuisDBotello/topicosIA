import matplotlib.pyplot as plt
from matplotlib.widgets import Button


class GraficoEnjambre:
    def __init__(self, enjambre):
        self.enjambre = enjambre

        self.fig, self.ax = plt.subplots()

        self.ax.set_title("Simulación de partículas")
        self.ax.set_xlabel("Posición X")
        self.ax.set_ylabel("Posición Y")
        self.ax.grid(True)

        # Crear el gráfico de dispersión
        self.puntos = self.ax.scatter([], [])

        boton_ax = self.fig.add_axes([0.78, 0.02, 0.18, 0.06])
        self.boton_reiniciar = Button(boton_ax, "Reiniciar")
        self.boton_reiniciar.on_clicked(self.reiniciar)

        # Registrar el gráfico como observador de cada partícula
        for particula in self.enjambre.particulas:
            particula.agregar_observador(self)

        self.actualizar_grafico()

    def actualizar(self, particula):
        """Se ejecuta cuando una partícula notifica un cambio."""
        self.actualizar_grafico()

    def actualizar_grafico(self):
        posiciones = [
            [p.x, p.y]
            for p in self.enjambre.particulas
        ]

        # Actualizar las coordenadas de los puntos
        self.puntos.set_offsets(posiciones)

        # Mantener los ejes dentro de los límites del enjambre
        self.ax.set_xlim(-self.enjambre.limX, self.enjambre.limX)
        self.ax.set_ylim(-self.enjambre.limY, self.enjambre.limY)

        self.fig.canvas.draw_idle()

    def mostrar(self):
        plt.show()

    def reiniciar(self, event=None):
        self.puntos.set_offsets([])
        self.ax.set_xlim(-1, 1)
        self.ax.set_ylim(-1, 1)
        self.fig.canvas.draw_idle()
