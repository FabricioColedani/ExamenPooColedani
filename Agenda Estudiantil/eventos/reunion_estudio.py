from eventos.evento import Evento
# Definición de clases hija (Reunion de Estudio)
class ReunionEstudio(Evento):
    def __init__(self, fecha, descripcion, tema):
        super().__init__(fecha, descripcion)
        self.tema = tema

    def __str__(self):
        return f"{self.descripcion} - {self.fecha} - Tema: {self.tema}"
