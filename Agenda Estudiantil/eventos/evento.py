# Definición de la clase base Evento
class Evento:
    def __init__(self, fecha, descripcion):
        self.fecha = fecha
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.descripcion} - {self.fecha}"
