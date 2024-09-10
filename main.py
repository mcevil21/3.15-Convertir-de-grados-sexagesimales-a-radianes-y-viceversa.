from Grados import EvaluadorCalificacion
if __name__ == "__main__":
    calificacion = float(input("Dame una calificación: \n"))
    asistencia = int(input("Dame la asistencia: 1 si asistió o 0 si no asistió\n"))
    evaluador = EvaluadorCalificacion(calificacion, asistencia)
    evaluador.mostrar_categoria()