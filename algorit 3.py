class MatrixCalculator:
    def _init_(self, root):
        self.root = root
        self.root.title("Calculadora Multifuncional de Matrices")
        self.root.geometry("1200x800")
        self.root.configure(bg='#98FF98')

        calc_frame = Frame(root, bg='#98FF98')
        calc_frame.pack(side="left", padx=10, pady=0, anchor='n')

        Button(calc_frame, text="¿Qué hace cada operación?", command=self.show_context, width=20, height=2, font=("Arial", 14, "bold"), bg='orange', fg='black').pack(pady=10)

        self.instruction_label = Label(calc_frame, text="Ingrese las dimensiones de la matriz:", bg='#98FF98', font=("Arial", 16, "bold"))
        self.instruction_label.pack(pady=10)

        self.rows_input = Entry(calc_frame, width=15, font=("Arial", 18))
        self.rows_input.pack(pady=5)
        self.rows_input.insert(0, "Filas (1-5)")

        self.cols_input = Entry(calc_frame, width=15, font=("Arial", 18))
        self.cols_input.pack(pady=5)
        self.cols_input.insert(0, "Columnas (1-5)")

        self.matrix_input = Entry(calc_frame, width=30, font=("Arial", 18))
        self.matrix_input.pack(pady=5)

        Button(calc_frame, text="Gauss-Jordan", command=self.gauss_jordan, width=20, height=2, font=("Arial", 14, "bold"), bg='blue', fg='white').pack(pady=12)
        Button(calc_frame, text="Regla de Cramer", command=self.cramer, width=20, height=2, font=("Arial", 14, "bold"), bg='blue', fg='white').pack(pady=12)
        Button(calc_frame, text="Multiplicación de Matrices", command=self.multiplicar, width=20, height=2, font=("Arial", 14, "bold"), bg='blue', fg='white').pack(pady=12)
        Button(calc_frame, text="Matriz Inversa", command=self.inversa, width=20, height=2, font=("Arial", 14, "bold"), bg='blue', fg='white').pack(pady=12)

        result_frame = Frame(root, bg='#98FF98')
        result_frame.pack(side="left", padx=10, pady=0, anchor='n')

        result_label = Label(result_frame, text="Resultado", bg='#98FF98', font=("Arial", 16, "bold"), fg='black')
        result_label.pack(pady=3)

        self.result_text = Text(result_frame, wrap="word", width=40, height=20, font=("Courier", 20, "bold"), bg='#f0f0f0', fg='black', relief="flat")
        self.result_text.pack(pady=5, fill="both", expand=True)

    def show_context(self):
        context_message = (
            "1. Método de Gauss-Jordan: Implementa la eliminación Gaussiana para hallar soluciones de sistemas de ecuaciones lineales.\n"
            "2. Regla de Cramer: Resuelve sistemas de ecuaciones lineales utilizando determinantes.\n"
            "3. Multiplicación de matrices: Implementa la multiplicación entre dos matrices de tamaño n x n.\n"
            "4. Cálculo de la matriz inversa: Proporciona la opción de calcular la matriz inversa de una matriz cuadrada, si esta existe."
        )
        messagebox.showinfo("Contexto de Operaciones", context_message)

    def get_matrix(self):
        try:
            # Obtener la matriz de la entrada del usuario
            rows = int(self.rows_input.get())
            cols = int(self.cols_input.get())
            if rows < 1 or rows > 5 or cols < 1 or cols > 5:
                raise ValueError("Las dimensiones deben estar entre 1 y 5.")
            
            matrix_input = self.matrix_input.get()
            if '|' in matrix_input:
                matrices = matrix_input.split('|')
                if len(matrices) != 2:
                    raise ValueError("Ingrese dos matrices separadas por '|' para la multiplicación.")
                matrices = [m.split(';') for m in matrices]
                matrix_a = np.array([list(map(float, row.split(','))) for row in matrices[0]])
                matrix_b = np.array([list(map(float, row.split(','))) for row in matrices[1]])
                return matrix_a, matrix_b
            else:
                rows_data = matrix_input.split(';')
                if len(rows_data) != rows or any(len(row.split(',')) != cols for row in rows_data):
                    raise ValueError(f"Ingrese exactamente {rows} filas y {cols} columnas.")
                matrix = np.array([list(map(float, row.split(','))) for row in rows_data])
                return matrix
        except ValueError as e:
            self.result_text.delete(1.0, "end")
            self.result_text.insert("end", f"Error: {e}")
            return None
        except Exception as e:
            self.result_text.delete(1.0, "end")
            self.result_text.insert("end", f"Error en los datos de entrada: {e}")
            return None
