def format_matrix(self, matrix):
        """Convierte los valores flotantes cercanos a enteros en enteros para eliminar los .0000"""
        formatted_matrix = []
        for row in matrix:
            formatted_row = []
            for el in row:
                if abs(el - round(el)) < 1e-9:
                    formatted_row.append(int(round(el)))
                else:
                    formatted_row.append(round(el, 2))
            formatted_matrix.append(formatted_row)
        return formatted_matrix

    def gauss_jordan(self):
        matrix = self.get_matrix()
        if matrix is not None:
            try:
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Paso 1: Matriz original:\n{self.format_matrix(matrix.tolist())}\n\n")
                
                m = Matrix(matrix)
                result, pivot_indices = m.rref()  
                
                self.result_text.insert("end", "Paso 2: Aplicamos operaciones elementales para reducir la matriz:\n")
                for idx, pivot in enumerate(pivot_indices):
                    self.result_text.insert("end", f"Operación {idx + 1}: Se hace pivot en la columna {pivot + 1}\n")
                
                self.result_text.insert("end", f"Resultado final (forma escalonada):\n{self.format_matrix(result.tolist())}\n")
            except Exception as e:
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Error al calcular Gauss-Jordan: {e}")

    def cramer(self):
        matrix = self.get_matrix()
        if matrix is not None:
            try:
                self.result_text.delete(1.0, "end")
                
                # Verificamos que sea un sistema cuadrado
                if matrix.shape[0] != matrix.shape[1] - 1:
                    self.result_text.insert("end", "La matriz no tiene la forma adecuada para aplicar la regla de Cramer (debe ser una matriz cuadrada aumentada).\n")
                    return
                
                m = Matrix(matrix[:, :-1])  
                det = m.det()  
                self.result_text.insert("end", f"Paso 1: Calculamos el determinante de la matriz de coeficientes:\nDeterminante = {det}\n\n")

                if det == 0:
                    self.result_text.insert("end", "El sistema no tiene solución única porque el determinante es 0.\n")
                else:
                    b = Matrix(matrix[:, -1])  
                    solution = []
                    for i in range(m.shape[1]):
                        mi = m.copy()
                        mi[:, i] = b  
                        det_mi = mi.det()  
                        self.result_text.insert("end", f"Paso 2.{i+1}: Reemplazamos la columna {i+1} por los términos independientes y calculamos el nuevo determinante:\nDeterminante = {det_mi}\n\n")
                        solution.append(det_mi / det)
                    
                    self.result_text.insert("end", f"Solución final del sistema:\n{self.format_matrix([solution])}\n")
            except Exception as e:
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Error al calcular la regla de Cramer: {e}")

    def multiplicar(self):
        matrices = self.get_matrix()
        if matrices is not None and isinstance(matrices, tuple):
            try:
                result = np.dot(matrices[0], matrices[1])
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Resultado de la multiplicación:\n{self.format_matrix(result.tolist())}\n")
            except ValueError as e:
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Error en la multiplicación: {e}")

    def inversa(self):
        matrix = self.get_matrix()
        if matrix is not None:
            try:
                m = Matrix(matrix)
                inv = m.inv()  
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Matriz inversa:\n{self.format_matrix(inv.tolist())}\n")
            except Exception as e:
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Error al calcular la matriz inversa: {e}")

# Define la función para abrir la ventana de Algoritmos
def abrir_ventana_algoritmos():
    ventana_algoritmos = Toplevel()
    ventana_algoritmos.title("Algoritmos - Álgebra Lineal")
    ventana_algoritmos.geometry("1200x800")
    ventana_algoritmos.configure(bg='#98FF98')

    app_algoritmos = MatrixCalculator(ventana_algoritmos)
