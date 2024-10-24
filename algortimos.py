    def gauss_jordan(self):
        matrix = self.get_matrix()
        if matrix is not None:
            try:
                m = Matrix(matrix)
                result = m.rref()[0]

                # Convertir los valores cercanos a enteros y redondear
                result_list = self.format_matrix(result.tolist())

                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Matriz en forma escalonada:\n{result_list}")
            except Exception as e:
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Error calculando Gauss-Jordan: {e}")

    def cramer(self):
        matrix = self.get_matrix()
        if matrix is not None:
            try:
                m = Matrix(matrix)
                det = m.det()
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Determinante: {int(det)}")
            except Exception as e:
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Error calculando Regla de Cramer: {e}")