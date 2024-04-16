#Programa Principal
#Importacion de los Eventos y clase Agenda
from eventos.examen import Examen
from eventos.trabajo_practico import TrabajoPractico
from eventos.reunion_estudio import ReunionEstudio
from agenda.agenda import Agenda
from agenda.menu import mostrar_menu

#Crear una instancia de la clase Agenda
agenda = Agenda()
    
while True:
        #Muestra menu y hace las condiciones para elegir cada opcion
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo_evento = input("Ingrese el tipo de evento (examen, tp, reunion): ")
            fecha = input("Ingrese la fecha (AÑO-MES-DIA): ")
            descripcion = input("Ingrese la descripción: ")

            if tipo_evento == "examen":
                materia = input("Ingrese la materia: ")
                evento = Examen(fecha, descripcion, materia)
            elif tipo_evento == "tp":
                materia = input("Ingrese la materia: ")
                entrega = input("Ingrese la fecha de entrega (AÑO-MES-DIA HORA:MINUTOS): ")
                evento = TrabajoPractico(fecha, descripcion, materia, entrega)
            elif tipo_evento == "reunion":
                tema = input("Ingrese el tema de la reunión: ")
                evento = ReunionEstudio(fecha, descripcion, tema)
            else:
                print("Tipo de evento inválido")
                continue
            
            #Agrega a la Agenda
            agenda.agregar_evento(evento)
            print("Evento agregado correctamente")

        #Muestra todos los Eventos en la Agenda
        elif opcion == "2":
            print("Eventos en la agenda:")
            agenda.mostrar_eventos()

        #Elimina Eventos de la Agenda
        elif opcion == "3":
            descripcion = input("Ingrese la descripción del evento a eliminar: ")
            agenda.eliminar_evento(descripcion)
            print("Evento eliminado correctamente")

        #Salir del programa
        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, por favor seleccione nuevamente")