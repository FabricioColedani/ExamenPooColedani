from eventos.evento import Evento
# Definición de clases hija (Examen)
class Examen(Evento):
    def __init__(self, fecha, descripcion, materia):
        super().__init__(fecha, descripcion)
        self.materia = materia

    def __str__(self):
        return f"{self.descripcion} - {self.fecha} - Materia: {self.materia}"
