# Nueva sección de texto con alineación a la izquierda para evitar cortes
        description_frame = Frame(root, bg='#a8d5a2')
        description_frame.pack(side="right", padx=20, pady=0, anchor='n')

        # Crear etiquetas para los títulos y párrafos, con justificación a la izquierda y wraplength ajustado
        self.add_description(description_frame, "Gauss-Jordan:", 
                             "El método de Gauss-Jordan se usa para resolver sistemas de \n"
                             "ecuaciones lineales, encontrar la inversa de una matriz,\n"
                             "o comprobar si un sistema es consistente. Además, muestra\n"
                             "la matriz resultante en su forma escalonada, lo que facilita \n"
                             "la resolución de sistemas de ecuaciones lineales.")
        
        self.add_description(description_frame, "Regla de Cramer:", 
                             "La regla de Cramer es un método para resolver sistemas de \n"
                             "ecuaciones lineales con tantas ecuaciones como incógnitas,\n"
                             "usando determinantes. El determinante también es útil para \n"
                             "verificar si una matriz es invertible y debería mostrar el valor \n"
                             "del determinante de la matriz en el área de resultados.")
        
        self.add_description(description_frame, "Multiplicación de matrices:", 
                             "La multiplicación de matrices es fundamental en álgebra lineal \n"
                             "para diversas aplicaciones, como la transformación de \n"
                             "coordenadas, la resolución de ecuaciones lineales y el \n"
                             "modelado en física o ingeniería. Debería mostrar el producto \n"
                             "de la multiplicación de la matriz en el área de resultados.")
        
        self.add_description(description_frame, "Matriz inversa:", 
                             "La matriz inversa es esencial en la resolución de sistemas de \n"
                             "ecuaciones lineales y en muchos problemas de álgebra lineal.\n"
                             "Solo matrices cuadradas y no singulares (aquellas cuyo \n"
                             "determinante no es cero) tienen inversa y debería mostrar la \n"
                             "matriz inversa en el área de resultados o indicar si la matriz \n"
                             "no es invertible.")
def add_description(self, frame, title, text):
        """Añadir un título y un texto con justificación a la izquierda"""
        # Título centrado
        title_label = tk.Label(frame, text=title, font=("Arial", 14, "bold"), bg='#a8d5a2', anchor="center")
        title_label.pack(padx=10, pady=10)

        # Texto justificado a la izquierda con wraplength ajustado a 600 píxeles
        text_label = tk.Label(frame, text=text, justify="left", wraplength=600, bg='#a8d5a2', font=("Arial", 12), anchor="w")
        text_label.pack(padx=10, pady=0)

    def get_matrix(self):
        try:
            elements = list(map(float, self.matrix_input.get().split(',')))
            n = int(len(elements) ** 0.5)
            return np.array(elements).reshape(n, n)
        except ValueError:
            self.result_text.delete(1.0, "end")
            self.result_text.insert("end", "Error: Asegúrese de que todos los valores sean números y estén separados por comas.")
            return None
        except Exception as e:
            self.result_text.delete(1.0, "end")
            self.result_text.insert("end", f"Error en los datos de entrada: {e}")
            return None

    def format_matrix(self, matrix):
        """Convierte los valores flotantes cercanos a enteros en enteros para eliminar los .0000"""
        formatted_matrix = []
        for row in matrix:
            formatted_row = []
            for el in row:
                if abs(el - round(el)) < 1e-9:  # Si la diferencia es muy pequeña, lo redondeamos
                    formatted_row.append(int(round(el)))
                else:
                    formatted_row.append(round(el, 2))  # Redondeamos a 2 decimales si no es entero
            formatted_matrix.append(formatted_row)
        return formatted_matrix
