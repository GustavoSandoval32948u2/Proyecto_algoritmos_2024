import tkinter as tk
from tkinter import Tk, Entry, Button, Text, Frame, Label, messagebox, Toplevel
from math import factorial
import matplotlib.pyplot as plt
import numpy as np
from sympy import Matrix

# Funciones de matemáticas discretas
def combinaciones_sin_repeticion(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def combinaciones_con_repeticion(n, r):
    return factorial(n + r - 1) // (factorial(r) * factorial(n - 1))

def permutaciones_sin_repeticion(n, r):
    return factorial(n) // factorial(n - r)

def permutaciones_con_repeticion(n, r):
    return n ** r

def calcular_combinaciones_sin_repeticion(entry_n, entry_r, label_resultado):
    n = int(entry_n.get())
    r = int(entry_r.get())
    resultado = combinaciones_sin_repeticion(n, r)
    label_resultado.config(text=f"Resultado: {resultado}")

def calcular_combinaciones_con_repeticion(entry_n, entry_r, label_resultado):
    n = int(entry_n.get())
    r = int(entry_r.get())
    resultado = combinaciones_con_repeticion(n, r)
    label_resultado.config(text=f"Resultado: {resultado}")

def calcular_permutaciones_sin_repeticion(entry_n, entry_r, label_resultado):
    n = int(entry_n.get())
    r = int(entry_r.get())
    resultado = permutaciones_sin_repeticion(n, r)
    label_resultado.config(text=f"Resultado: {resultado}")

def calcular_permutaciones_con_repeticion(entry_n, entry_r, label_resultado):
    n = int(entry_n.get())
    r = int(entry_r.get())
    resultado = permutaciones_con_repeticion(n, r)
    label_resultado.config(text=f"Resultado: {resultado}")

def ventana_matematica_discreta():
    root_md = tk.Toplevel()
    root_md.title("Combinaciones y Permutaciones")
    root_md.geometry("1200x600")
    
    bg_color = "#8E9AAF"
    btn_color = "#32CD32"
    txt_color = "#ffffff"
    resultado_color = "#FFD700"
    font_large = ("Helvetica", 16, "bold")
    font_medium = ("Helvetica", 14)
    font_small = ("Helvetica", 12)

    root_md.configure(bg=bg_color)

    label_n = tk.Label(root_md, text="VALOR DE N:", font=font_medium, bg=bg_color, fg=txt_color)
    label_n.grid(row=0, column=0, padx=20, pady=10)

    entry_n = tk.Entry(root_md, font=font_medium, width=10)
    entry_n.grid(row=0, column=1, padx=20, pady=10)

    label_r = tk.Label(root_md, text="VALOR DE R:", font=font_medium, bg=bg_color, fg=txt_color)
    label_r.grid(row=1, column=0, padx=20, pady=10)

    entry_r = tk.Entry(root_md, font=font_medium, width=10)
    entry_r.grid(row=1, column=1, padx=20, pady=10)

    label_combinaciones = tk.Label(root_md, text="OPERACIONES DE COMBINACIONES", font=font_large, bg=bg_color, fg=resultado_color)
    label_combinaciones.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

    label_resultado = tk.Label(root_md, text="Resultado:", font=font_large, bg=bg_color, fg=resultado_color)
    label_resultado.grid(row=8, column=0, columnspan=2, padx=20, pady=20)

    boton_combinaciones_sin_repeticion = tk.Button(root_md, text="COMBINACIONES SIN REPETICIÓN", font=font_small, bg=btn_color, fg=txt_color, command=lambda: calcular_combinaciones_sin_repeticion(entry_n, entry_r, label_resultado))
    boton_combinaciones_sin_repeticion.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

    boton_combinaciones_con_repeticion = tk.Button(root_md, text="COMBINACIÓN CON REPETICIÓN", font=font_small, bg=btn_color, fg=txt_color, command=lambda: calcular_combinaciones_con_repeticion(entry_n, entry_r, label_resultado))
    boton_combinaciones_con_repeticion.grid(row=4, column=0, columnspan=2, padx=20, pady=10)

    label_permutaciones = tk.Label(root_md, text="OPERACIONES DE PERMUTACIONES", font=font_large, bg=bg_color, fg=resultado_color)
    label_permutaciones.grid(row=5, column=0, columnspan=2, padx=20, pady=20)

    boton_permutaciones_sin_repeticion = tk.Button(root_md, text="PERMUTACIONES SIN REPETICIÓN", font=font_small, bg=btn_color, fg=txt_color, command=lambda: calcular_permutaciones_sin_repeticion(entry_n, entry_r, label_resultado))
    boton_permutaciones_sin_repeticion.grid(row=6, column=0, columnspan=2, padx=20, pady=10)

    boton_permutaciones_con_repeticion = tk.Button(root_md, text="PERMUTACIÓN CON REPETICIÓN", font=font_small, bg=btn_color, fg=txt_color, command=lambda: calcular_permutaciones_con_repeticion(entry_n, entry_r, label_resultado))
    boton_permutaciones_con_repeticion.grid(row=7, column=0, columnspan=2, padx=20, pady=10)


    contexto_texto = (
    "En combinatoria, se estudian las formas en las que se pueden seleccionar y organizar elementos.\n\n"
    
    "COMBINACIONES: Se refiere a la selección de 'r' elementos de un conjunto de 'n' elementos, el orden no importa.\n"
    "La fórmula para calcular combinaciones es C(n, r) = n! / [r! * (n - r)!].\n"
    "Por ejemplo, si tienes un conjunto de 5 elementos y eliges 2, no importa el orden en que los selecciones.\n"
    "Lo importante es la selección misma, sin tener en cuenta las posibles permutaciones de esos elementos.\n\n"
    
    "PERMUTACIONES: En contraste con las combinaciones, aquí el orden sí importa (la disposición de 'r' elementos)\n"
    "de un conjunto de 'n' elementos, donde el orden en que se colocan los elementos cambia el resultado final.\n"
    "La fórmula para permutaciones sin repetición es P(n, r) = n! / (n - r)!.\n"
    "Por ejemplo, si tienes 5 libros y quieres organizarlos en un estante de 3 posiciones, el orden si importa.\n\n"
    
    "PERMUTACIONES CON REPETICIÓN: Si los elementos pueden repetirse en la disposición, usamos la fórmula P = n^r,\n"
    "lo que significa que en cada elección puedes repetir los elementos. Es útil en casos de reposición.\n\n"
    
    "Estas fórmulas son esenciales para resolver problemas de probabilidad y combinatoria, permitiendo calcular\n"
    "el número de formas en que se pueden organizar o seleccionar elementos bajo diferentes condiciones."
)

    label_contexto = tk.Label(root_md, text=contexto_texto, font=("Helvetica", 12), bg=bg_color, fg=txt_color, justify="left")
    label_contexto.grid(row=0, column=2, rowspan=9, padx=(20, 10), pady=10, sticky="ne")

# Función de álgebra lineal
def ventana_algebra_lineal():
    ventana = tk.Tk()
    ventana.title("Aplicación de Álgebra Lineal")
    ventana.geometry("1200x600")  
    ventana.configure(bg="#e0f7fa")

    bienvenida_label = tk.Label(ventana, text="Bienvenido a la Aplicación de Álgebra Lineal", font=("Arial", 20), bg="#e0f7fa")
    bienvenida_label.pack(pady=20)

    multiplicar_button = tk.Button(ventana, text="Multiplicar Matrices", command=lambda: ventana_multiplicar(ventana), bg="#4db6ac", fg="white", font=("Arial", 16))
    multiplicar_button.pack(pady=10)

    inversa_button = tk.Button(ventana, text="Encontrar Inversa de Matriz", command=lambda: ventana_inversa(ventana), bg="#4db6ac", fg="white", font=("Arial", 16))
    inversa_button.pack(pady=10)

    ecuaciones_button = tk.Button(ventana, text="Resolver Sistemas de Ecuaciones Lineales", command=lambda: ventana_ecuaciones_lineales(ventana), bg="#4db6ac", fg="white", font=("Arial", 16))
    ecuaciones_button.pack(pady=10)

    ventana.mainloop()

# Ventana para la opción de multiplicar matrices
def ventana_multiplicar(ventana):
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Multiplicar Matrices")
    nueva_ventana.geometry("1200x600")  
    nueva_ventana.configure(bg="#e0f7fa")

    left_frame = tk.Frame(nueva_ventana, bg="#e0f7fa")
    left_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)

    instrucciones_label = tk.Label(left_frame, text="Ingresa las dimensiones de las matrices para multiplicarlas:", font=("Arial", 14), bg="#e0f7fa")
    instrucciones_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

    filas1_label = tk.Label(left_frame, text="Filas de la primera matriz:", bg="#e0f7fa", font=("Arial", 12))
    filas1_label.grid(row=1, column=0, padx=10, sticky='w')
    filas1_entry = tk.Entry(left_frame, font=("Arial", 12))
    filas1_entry.grid(row=1, column=1)

    columnas1_label = tk.Label(left_frame, text="Columnas de la primera matriz:", bg="#e0f7fa", font=("Arial", 12))
    columnas1_label.grid(row=2, column=0, padx=10, sticky='w')
    columnas1_entry = tk.Entry(left_frame, font=("Arial", 12))
    columnas1_entry.grid(row=2, column=1)

    filas2_label = tk.Label(left_frame, text="Filas de la segunda matriz:", bg="#e0f7fa", font=("Arial", 12))
    filas2_label.grid(row=3, column=0, padx=10, sticky='w')
    filas2_entry = tk.Entry(left_frame, font=("Arial", 12))
    filas2_entry.grid(row=3, column=1)

    columnas2_label = tk.Label(left_frame, text="Columnas de la segunda matriz:", bg="#e0f7fa", font=("Arial", 12))
    columnas2_label.grid(row=4, column=0, padx=10, sticky='w')
    columnas2_entry = tk.Entry(left_frame, font=("Arial", 12))
    columnas2_entry.grid(row=4, column=1)

    # Título y contexto en la parte derecha
    right_frame = tk.Frame(nueva_ventana, bg="#e0f7fa")
    right_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

    contexto_label = tk.Label(right_frame, text="¿Qué es la Multiplicación de Matrices?", font=("Arial", 16, 'bold'), bg="#e0f7fa")
    contexto_label.pack(anchor='ne', pady=(0, 5))

    contexto_text = (
        "La multiplicación de matrices es una operación que combina dos matrices para producir una tercera matriz. "
        "Esta operación es fundamental en diversas áreas como la ingeniería, la computación y la física. "
        "Para multiplicar dos matrices, el número de columnas de la primera matriz debe ser igual al número de filas "
        "de la segunda matriz. El elemento de la fila i y columna j de la matriz resultante se calcula como la "
        "suma del producto de los elementos de la fila i de la primera matriz por los elementos de la columna j de "
        "la segunda matriz."
    )

    contexto_label_d = tk.Label(right_frame, text=contexto_text, font=("Arial", 12), bg="#e0f7fa", justify="left", wraplength=400)
    contexto_label_d.pack(anchor='ne', padx=10, pady=10)

    resultado_label = tk.Label(left_frame, text="Resultado de la multiplicación:", font=("Arial", 12), bg="#e0f7fa")
    resultado_label.grid(row=5, column=0, columnspan=2, pady=10)

    resultado_frame = tk.Frame(left_frame)
    resultado_frame.grid(row=9, column=0, columnspan=2, pady=10)

    matriz_frame = tk.Frame(left_frame)
    matriz_frame.grid(row=8, column=0, columnspan=2, pady=10)

    def crear_entradas_matrices():
        try:
            filas1 = int(filas1_entry.get())
            columnas1 = int(columnas1_entry.get())
            filas2 = int(filas2_entry.get())
            columnas2 = int(columnas2_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos.")
            return

        if columnas1 != filas2:
            messagebox.showerror("Error", "El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda matriz.")
            return

        for widget in matriz_frame.winfo_children():
            widget.destroy()
        for widget in resultado_frame.winfo_children():
            widget.destroy()

        # Generar celdas para la primera matriz
        matriz1_entries = []
        for i in range(filas1):
            fila_entries = []
            for j in range(columnas1):
                entrada = tk.Entry(matriz_frame, width=5, font=("Arial", 12))
                entrada.grid(row=i, column=j)
                fila_entries.append(entrada)
            matriz1_entries.append(fila_entries)

        # Generar celdas para la segunda matriz
        matriz2_entries = []
        for i in range(filas2):
            fila_entries = []
            for j in range(columnas2):
                entrada = tk.Entry(matriz_frame, width=5, font=("Arial", 12))
                entrada.grid(row=i, column=j + columnas1 + 2)  
                fila_entries.append(entrada)
            matriz2_entries.append(fila_entries)

        # Calcular y mostrar el resultado de la multiplicación
        def multiplicar_matrices():
            try:
                matriz1 = [[int(matriz1_entries[i][j].get()) for j in range(columnas1)] for i in range(filas1)]
                matriz2 = [[int(matriz2_entries[i][j].get()) for j in range(columnas2)] for i in range(filas2)]
                resultado = [[0] * columnas2 for _ in range(filas1)]

                for i in range(filas1):
                    for j in range(columnas2):
                        for k in range(columnas1):  
                            resultado[i][j] += matriz1[i][k] * matriz2[k][j]

                for i in range(filas1):
                    for j in range(columnas2):
                        entrada_resultado = tk.Label(resultado_frame, text=resultado[i][j], font=("Arial", 12))
                        entrada_resultado.grid(row=i, column=j)

            except ValueError:
                messagebox.showerror("Error", "Por favor, ingresa solo números en las matrices.")
                return

        # Botón para multiplicar las matrices
        multiplicar_button = tk.Button(left_frame, text="Multiplicar Matrices", command=multiplicar_matrices, bg="#4db6ac", fg="white", font=("Arial", 12))
        multiplicar_button.grid(row=8, column=3,padx=10, pady=10)

    generar_button = tk.Button(left_frame, text="Generar Entradas de Matrices", command=crear_entradas_matrices, bg="#4db6ac", fg="white", font=("Arial", 12))
    generar_button.grid(row=5, column=0, columnspan=2, pady=10)

# Ventana para la opción de encontrar la inversa de una matriz
def ventana_inversa(ventana):
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Encontrar Inversa de Matriz")
    nueva_ventana.geometry("1200x600")  
    nueva_ventana.configure(bg="#e0f7fa")

    left_frame = tk.Frame(nueva_ventana, bg="#e0f7fa")
    left_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)

    instrucciones_label = tk.Label(left_frame, text="Ingresa las dimensiones de la matriz:", font=("Arial", 14), bg="#e0f7fa")
    instrucciones_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

    filas_label = tk.Label(left_frame, text="Filas de la matriz:", bg="#e0f7fa", font=("Arial", 12))
    filas_label.grid(row=1, column=0, padx=10, sticky='w')
    filas_entry = tk.Entry(left_frame, font=("Arial", 12))
    filas_entry.grid(row=1, column=1)

    columnas_label = tk.Label(left_frame, text="Columnas de la matriz:", bg="#e0f7fa", font=("Arial", 12))
    columnas_label.grid(row=2, column=0, padx=10, sticky='w')
    columnas_entry = tk.Entry(left_frame, font=("Arial", 12))
    columnas_entry.grid(row=2, column=1)

    # Título y contexto en la parte derecha
    right_frame = tk.Frame(nueva_ventana, bg="#e0f7fa")
    right_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

    contexto_label = tk.Label(right_frame, text="¿Qué es la Inversa de Matrices?", font=("Arial", 16, 'bold'), bg="#e0f7fa")
    contexto_label.pack(anchor='ne', pady=(0, 5))

    contexto_text = (
        "La inversa de una matriz es un concepto fundamental en álgebra lineal. "
        "Si A es una matriz cuadrada, su inversa se denota como A^(-1), y se define "
        "como la matriz que, cuando se multiplica por A, produce la matriz identidad. "
        "No todas las matrices tienen inversa, y solo las matrices cuadradas que son no singulares (determinante diferente de cero) tienen inversa."
    )

    contexto_label_d = tk.Label(right_frame, text=contexto_text, font=("Arial", 12), bg="#e0f7fa", justify="left", wraplength=400)
    contexto_label_d.pack(anchor='ne', padx=10, pady=10)

    resultado_label = tk.Label(left_frame, text="Resultado de la inversa:", font=("Arial", 12), bg="#e0f7fa")
    resultado_label.grid(row=8, column=0, columnspan=2, pady=(20, 0), sticky='')

    resultado_frame = tk.Frame(left_frame)
    resultado_frame.grid(row=9, column=0, columnspan=2, pady=10, sticky='')  

    matriz_frame = tk.Frame(left_frame)
    matriz_frame.grid(row=7, column=0, columnspan=2, pady=10)

    def crear_entradas_matriz():
        try:
            filas = int(filas_entry.get())
            columnas = int(columnas_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos.")
            return

        if filas != columnas:
            messagebox.showerror("Error", "La matriz debe ser cuadrada (igual número de filas y columnas).")
            return

        for widget in matriz_frame.winfo_children():
            widget.destroy()
        for widget in resultado_frame.winfo_children():
            widget.destroy()

        # Generar celdas para la matriz
        matriz_entries = []
        for i in range(filas):
            fila_entries = []
            for j in range(columnas):
                entrada = tk.Entry(matriz_frame, width=5, font=("Arial", 12))
                entrada.grid(row=i, column=j)
                fila_entries.append(entrada)
            matriz_entries.append(fila_entries)

        # Calcular y mostrar el resultado de la inversa
        def calcular_inversa():
            try:
                matriz = [[float(matriz_entries[i][j].get()) for j in range(columnas)] for i in range(filas)]
                inversa = calcular_inversa_matriz(matriz)

                if inversa is not None:
                    for i in range(filas):
                        for j in range(columnas):
                            entrada_resultado = tk.Label(resultado_frame, text=f"{inversa[i][j]:.2f}", font=("Arial", 12))
                            entrada_resultado.grid(row=i, column=j)
                else:
                    messagebox.showerror("Error", "La matriz no tiene inversa (determinante es cero).")

            except ValueError:
                messagebox.showerror("Error", "Por favor, ingresa solo números en la matriz.")
                return

        calcular_button = tk.Button(left_frame, text="Calcular Inversa", command=calcular_inversa, bg="#4db6ac", fg="white", font=("Arial", 12))
        calcular_button.grid(row=8, column=2, padx=(10,0), pady=20) 

    generar_button = tk.Button(left_frame, text="Generar Entradas de Matriz", command=crear_entradas_matriz, bg="#4db6ac", fg="white", font=("Arial", 12))
    generar_button.grid(row=4, column=0, columnspan=2, pady=20)

# Función para calcular la inversa de la matriz
def calcular_inversa_matriz(matriz):
    try:
        matriz_np = np.array(matriz)
        inversa = np.linalg.inv(matriz_np)
        return inversa.tolist()
    except np.linalg.LinAlgError:
        return None  

# Ventana para la opción de resolver sistemas de ecuaciones lineales
def ventana_ecuaciones_lineales(ventana):
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Resolver Sistemas de Ecuaciones Lineales")
    nueva_ventana.geometry("1200x600")
    nueva_ventana.configure(bg="#e0f7fa")

    left_frame = tk.Frame(nueva_ventana, bg="#e0f7fa")
    left_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)

    instrucciones_label = tk.Label(left_frame, text="Ingresa el número de ecuaciones y variables:", font=("Arial", 14), bg="#e0f7fa")
    instrucciones_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

    ecuaciones_label = tk.Label(left_frame, text="Número de ecuaciones (2, 3 o 4):", bg="#e0f7fa", font=("Arial", 12))
    ecuaciones_label.grid(row=1, column=0, padx=10, sticky='w')
    ecuaciones_entry = tk.Entry(left_frame, font=("Arial", 12))
    ecuaciones_entry.grid(row=1, column=1)

    metodo_label = tk.Label(left_frame, text="Selecciona el método:", font=("Arial", 12), bg="#e0f7fa")
    metodo_label.grid(row=2, column=0, padx=10, pady=(10, 10))
    
    metodo_var = tk.StringVar(value="Gauss-Jordan")
    gauss_jordan_radiobutton = tk.Radiobutton(left_frame, text="Gauss-Jordan", variable=metodo_var, value="Gauss-Jordan", bg="#e0f7fa", font=("Arial", 12))
    cramer_radiobutton = tk.Radiobutton(left_frame, text="Regla de Cramer", variable=metodo_var, value="Cramer", bg="#e0f7fa", font=("Arial", 12))
    
    gauss_jordan_radiobutton.grid(row=3, column=0, sticky='w')
    cramer_radiobutton.grid(row=3, column=1, sticky='w')

    resultado_label = tk.Label(left_frame, text="Resultado del sistema:", font=("Arial", 12), bg="#e0f7fa")
    resultado_label.grid(row=5, column=0, columnspan=2, pady=(20))

    resultado_frame = tk.Frame(left_frame)
    resultado_frame.grid(row=7, column=0, columnspan=2, pady=10)

    matriz_frame = tk.Frame(left_frame)
    matriz_frame.grid(row=8, column=0, columnspan=2, pady=10)   

    # Título y contexto en la parte derecha
    right_frame = tk.Frame(nueva_ventana, bg="#e0f7fa")
    right_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

    contexto_label = tk.Label(right_frame, text="¿Qué son los sistemas de ecuaciones lineales?", font=("Arial", 16, 'bold'), bg="#e0f7fa")
    contexto_label.pack(anchor='ne', pady=(0, 5))

    contexto_text = (
        """
        La resolución de sistemas de ecuaciones lineales incluye abordar sistemas de distintas dimensiones, como 2x2, 3x3 y 4x4. 
        En un sistema 2x2, se resuelven dos ecuaciones con dos incógnitas, mientras que en un 3x3 se trabajan tres ecuaciones con tres variables, 
        y en un 4x4, cuatro ecuaciones con cuatro incógnitas. Se pueden emplear métodos como Gauss-Jordan, 
        que transforma el sistema a una forma escalonada reducida, o la regla de Cramer, que utiliza determinantes para sistemas cuadrados. 
        Al resolver, pueden surgir tres situaciones: soluciones únicas (donde las ecuaciones se intersecan en un único punto), 
        sin solución (cuando las ecuaciones representan líneas o planos paralelos) o soluciones infinitas (cuando las ecuaciones son dependientes y representan la misma línea o plano). 
        """

    )

    contexto_label_d = tk.Label(right_frame, text=contexto_text, font=("Arial", 12), bg="#e0f7fa", justify="left", wraplength=400)
    contexto_label_d.pack(anchor='ne', padx=10, pady=10)

    def crear_entradas_sistema():
        try:
            num_ecuaciones = int(ecuaciones_entry.get())
            if num_ecuaciones not in [2, 3, 4]:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido de ecuaciones (2, 3 o 4).")
            return

        for widget in matriz_frame.winfo_children():
            widget.destroy()
        for widget in resultado_frame.winfo_children():
            widget.destroy()

        coeficientes_entries = []
        terminos_independientes_entries = []

        for i in range(num_ecuaciones):
            fila_entries = []
            for j in range(num_ecuaciones):
                entrada = tk.Entry(matriz_frame, width=5, font=("Arial", 12))
                entrada.grid(row=i, column=j)
                fila_entries.append(entrada)
            coeficientes_entries.append(fila_entries)

            entrada_termino_independiente = tk.Entry(matriz_frame, width=5, font=("Arial", 12))
            entrada_termino_independiente.grid(row=i, column=num_ecuaciones + 1)  
            terminos_independientes_entries.append(entrada_termino_independiente)

        # Calcular y mostrar el resultado del sistema
        def resolver_sistema():
            try:
                coeficientes = [[float(coeficientes_entries[i][j].get()) for j in range(num_ecuaciones)] for i in range(num_ecuaciones)]
                terminos_independientes = [float(terminos_independientes_entries[i].get()) for i in range(num_ecuaciones)]
                metodo = metodo_var.get()

                if metodo == "Gauss-Jordan":
                    soluciones, mensaje = resolver_por_gauss_jordan(coeficientes, terminos_independientes)
                else:
                    soluciones, mensaje = resolver_por_cramer(coeficientes, terminos_independientes)

                # Mostrar el resultado
                if soluciones is None:
                    resultado_label = tk.Label(resultado_frame, text=mensaje, font=("Arial", 12))
                    resultado_label.grid(row=0, column=0)
                else:
                    for i in range(num_ecuaciones):
                        entrada_resultado = tk.Label(resultado_frame, text=f"x{i+1} = {soluciones[i]:.2f}", font=("Arial", 12))
                        entrada_resultado.grid(row=i, column=0)
                    mensaje_label = tk.Label(resultado_frame, text=mensaje, font=("Arial", 12))
                    mensaje_label.grid(row=num_ecuaciones, column=0)

                    # Llamar a la funcion para graficar
                    graficar_ecuaciones(coeficientes, terminos_independientes)

            except ValueError:
                messagebox.showerror("Error", "Por favor, ingresa solo números en las matrices.")
                return  

        # Botón para resolver el sistema
        resolver_button = tk.Button(left_frame, text="Resolver Sistema", command=resolver_sistema, bg="#4db6ac", fg="white", font=("Arial", 12))
        resolver_button.grid(row=5, column=2, padx=10, pady=5, sticky='w')

    generar_button = tk.Button(left_frame, text="Generar Entradas del Sistema", command=crear_entradas_sistema, bg="#4db6ac", fg="white", font=("Arial", 12))
    generar_button.grid(row=4, column=1,pady=20)

# Función para graficar las ecuaciones
def graficar_ecuaciones(coeficientes, terminos_independientes):
    x_vals = np.linspace(-10, 10, 400)  

    # Graficar cada ecuación
    for i in range(len(coeficientes)):
        a, b = coeficientes[i]
        c = terminos_independientes[i]

        # Calcular los valores de y
        y_vals = (c - a * x_vals) / b  
        
        # Graficar la recta
        plt.plot(x_vals, y_vals, label=f'Ecuación {i + 1}')

    plt.axhline(0, color='black', lw=0.5)  # Línea horizontal en y=0
    plt.axvline(0, color='black', lw=0.5)  # Línea vertical en x=0
    plt.xlim(-10, 10)  
    plt.ylim(-10, 10)  
    plt.grid(color='gray', linestyle='--', linewidth=0.5) 
    plt.legend()  
    plt.title('Gráficas de las Ecuaciones')  
    plt.xlabel('x')  # Etiqueta del eje x
    plt.ylabel('y')  # Etiqueta del eje y
    plt.show()  

# Función para resolver el sistema de ecuaciones por Gauss-Jordan
def resolver_por_gauss_jordan(coeficientes, terminos_independientes):
    matriz = np.column_stack((coeficientes, terminos_independientes))
    try:
        soluciones = np.linalg.solve(coeficientes, terminos_independientes)
        return soluciones, "Solución única"
    except np.linalg.LinAlgError as e:
        rango_a = np.linalg.matrix_rank(coeficientes)
        rango_aumentada = np.linalg.matrix_rank(matriz)

        if rango_a != rango_aumentada:
            return None, "El sistema no tiene solución"
        elif rango_a == rango_aumentada and rango_a < len(coeficientes):
            return None, "El sistema tiene soluciones infinitas"

# Función para resolver el sistema de ecuaciones por la regla de Cramer
def resolver_por_cramer(coeficientes, terminos_independientes):
    det_a = np.linalg.det(coeficientes)
    if det_a == 0:
        return None, "El sistema no tiene solución o tiene soluciones infinitas"
    else:
        soluciones = []
        for i in range(len(coeficientes)):
            matriz_temp = np.copy(coeficientes)
            matriz_temp[:, i] = terminos_independientes
            soluciones.append(np.linalg.det(matriz_temp) / det_a)
        return soluciones, "Solución única" 
    
# Función para graficar las ecuaciones
def graficar_ecuaciones(coeficientes, terminos_independientes):
    x_vals = np.linspace(-10, 10, 400)  
    plt.figure(figsize=(10, 6))

    for i in range(len(coeficientes)):
        a = coeficientes[i]
        b = terminos_independientes[i]

        # Calculamos la pendiente y la intersección
        if len(a) == 2:  
            m = -a[0] / a[1]  
            b = b / a[1]  
            y_vals = m * x_vals + b
            plt.plot(x_vals, y_vals, label=f'Ecuación {i+1}: {a[0]}x + {a[1]}y = {terminos_independientes[i]}')
        elif len(a) == 3: 
            if len(coeficientes) == 2:
                x_vals_2d = np.linspace(-10, 10, 400)
                y_vals_1 = (b[0] - a[0] * x_vals_2d) / a[1]
                y_vals_2 = (b[1] - coeficientes[1][0] * x_vals_2d) / coeficientes[1][1]
                plt.plot(x_vals_2d, y_vals_1, label=f'Ecuación 1')
                plt.plot(x_vals_2d, y_vals_2, label=f'Ecuación 2')

    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.title('Gráfica de las Ecuaciones')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.show()

class MatrixCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Multifuncional de Matrices")
        self.root.geometry("1200x800")
        self.root.configure(bg='#98FF98')

        calc_frame = Frame(root, bg='#98FF98')
        calc_frame.pack(side="left", padx=10, pady=0, anchor='n')

        Button(calc_frame, text="¿Qué hace cada operación?", command=self.show_context, width=25, height=3, font=("Arial", 14, "bold"), bg='orange', fg='black').pack(pady=10)

        self.instruction_label = Label(calc_frame, text="Ingrese las dimensiones (datos separados por , y ; para columnas)", bg='#98FF98', font=("Arial", 14, "bold"))
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
        context_window = tk.Toplevel(self.root)
        context_window.title("Contexto de Operaciones")
        context_window.geometry("400x300")
        context_window.configure(bg='#A1D6E2')

        context_message = (
            "1. Método de Gauss-Jordan: Implementa la eliminación Gaussiana para hallar soluciones de sistemas de ecuaciones lineales.\n"
            "2. Regla de Cramer: Resuelve sistemas de ecuaciones lineales utilizando determinantes.\n"
            "3. Multiplicación de matrices: Implementa la multiplicación entre dos matrices de tamaño n x n.\n"
            "4. Cálculo de la matriz inversa: Proporciona la opción de calcular la matriz inversa de una matriz cuadrada, si esta existe."
        )

        text_widget = tk.Text(context_window, wrap=tk.WORD, bg='white', fg='black', font=("Arial", 12))
        text_widget.insert(tk.END, context_message)
        text_widget.config(state=tk.DISABLED)  
        text_widget.pack(expand=True, fill='both', padx=10, pady=10)

        close_button = tk.Button(context_window, text="Cerrar", command=context_window.destroy, width=15, height=2, bg='orange')
        close_button.pack(pady=10)

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
    ventana_algoritmos.title("Algoritmos")
    ventana_algoritmos.geometry("1200x800")
    ventana_algoritmos.configure(bg='#98FF98')

    app_algoritmos = MatrixCalculator(ventana_algoritmos)

# Ventana principal
def ventana_principal():
    root = tk.Tk()
    root.title("PROYECTO FINAL 2024")
    root.geometry("1200x600")  
    root.configure(bg="#A1D6E2")  

    # Título principal
    label_titulo = tk.Label(root, text="PROYECTO FINAL 2024", font=("Helvetica", 30, "bold"), bg="#A1D6E2", fg="black")
    label_titulo.pack(pady=30)  

    # Botón de Álgebra Lineal
    btn_algebra = tk.Button(root, text="Álgebra Lineal", command=ventana_algebra_lineal, 
                             font=("Helvetica", 16, "bold"), bg="#4FC3F7", fg="white", width=25, height=2)  
    btn_algebra.pack(pady=20)  

    # Botón de Matemática Discreta
    btn_matematica_discreta = tk.Button(root, text="Matemática Discreta", command=ventana_matematica_discreta, 
                                         font=("Helvetica", 16, "bold"), bg="#9B59B6", fg="white", width=25, height=2)  
    btn_matematica_discreta.pack(pady=20)  

    # Botón de Algoritmos
    btn_algoritmos = tk.Button(root, text="Algoritmos", command=abrir_ventana_algoritmos, font=("Helvetica", 16, "bold"), 
                               bg="#E57373", fg="white", width=25, height=2)  
    btn_algoritmos.pack(pady=30) 

    label_creadores = tk.Label(root, text="Creadores", font=("Helvetica", 12, "bold"), bg="#A1D6E2", fg="black")
    label_creadores.place(x=10, y=550)  

    label_nombres = tk.Label(root, text="Edin Adolfo, Gustavo Sandoval y Mauricio Figueroa", font=("Helvetica", 12), bg="#A1D6E2", fg="black")
    label_nombres.place(x=10, y=570)

    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) or isinstance(widget, tk.Label):
            widget.pack_configure(anchor='center')

    root.mainloop()

# Ejecutar la ventana principal
ventana_principal()
