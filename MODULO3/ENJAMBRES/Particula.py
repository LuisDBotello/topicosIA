class Particula:

    def __init__(self, id, x=0, y=0, valor=0):
        self.id = id
        self.x = x
        self.y = y
        self.valor = valor
        self.vx = 0.0
        self.vy = 0.0

        self.best = float("-inf")
        self.bestx = None
        self.besty = None

        # Cada partícula tiene sus propios observadores
        self.observadores = []

    def agregar_observador(self, observador):
        if observador not in self.observadores:
            self.observadores.append(observador)

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y
        self.notify()

    def notify(self):
        for observador in self.observadores:
            observador.actualizar(self)

    def __str__(self):
        return f"Partícula {self.id}: ({self.x:.2f}, {self.y:.2f})"
