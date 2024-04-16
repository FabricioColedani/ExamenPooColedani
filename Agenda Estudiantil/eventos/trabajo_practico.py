from eventos.evento import Evento
# Definición de clases hija (Trabajo Practico)
class TrabajoPractico(Evento):
    def __init__(self, fecha, descripcion, materia, entrega):
        super().__init__(fecha, descripcion)
        self.materia = materia
        self.entrega = entrega

    def __str__(self):
        return f"{self.descripcion} - {self.fecha} - Materia: {self.materia} - Entrega: {self.entrega}"
