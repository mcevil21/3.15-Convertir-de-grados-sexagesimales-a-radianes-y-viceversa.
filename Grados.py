class EvaluadorCalificacion:
    def __init__(self, calificacion, asistencia):
        self.calificacion = calificacion
        self.asistencia = asistencia
    def obtener_categoria(self):
        if self.calificacion > 9.0:
            if self.asistencia == 1:
                return "La calificación es A Excelente con Mención Honorífica."
            else:
                return "La calificación es A Excelente."
        elif self.calificacion > 8.0:
            if self.asistencia == 1:
                return "La calificación es B Muy Bien con Mención."
            else:
                return "La calificación es B Excelente."
        elif self.calificacion > 7.5:
            return "La calificación es C Bien."
        else:
            return "La calificación es R Reprobado. Lo siento mucho."
    def mostrar_categoria(self):
        print(self.obtener_categoria())
def main():
    try:
        calificacion = float(input("Dame una calificación: \n"))
        asistencia = int(input("Dame la asistencia: 1 si asistió o 0 si no asistió\n"))
        if asistencia not in [0, 1]:
            print("Valor de asistencia no válido. Debe ser 1 o 0.")
            return
        evaluador = EvaluadorCalificacion(calificacion, asistencia)
        evaluador.mostrar_categoria()
    except ValueError:
        print("Por favor, introduce un número válido.")
if __name__ == "__main__":
    main()