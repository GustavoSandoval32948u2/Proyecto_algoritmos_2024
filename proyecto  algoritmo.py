import numpy as np
from tkinter import Tk, Entry, Button, Text, Frame, Label
import tkinter as tk

class MatrixCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Multifuncional de Matrices")
        self.root.geometry("1600x1000")
        self.root.configure(bg='#a8d5a2')

        # Frame principal para la parte izquierda (entrada y botones)
        calc_frame = Frame(root, bg='#a8d5a2')
        calc_frame.pack(side="left", padx=10, pady=0, anchor='n')

        # Etiqueta de instrucciones
        self.instruction_label = Label(calc_frame, text="Ingrese 4 números separados por comas", bg='#a8d5a2', font=("Arial", 16, "bold"))
        self.instruction_label.pack(pady=10)

        # Campo de entrada de la matriz
        self.matrix_input = Entry(calc_frame, width=30, font=("Arial", 18))
        self.matrix_input.pack(pady=5)

        # Botones de operaciones
        Button(calc_frame, text="Gauss-Jordan", command=self.gauss_jordan, width=30, height=3, font=("Arial", 16, "bold"), bg='blue', fg='white').pack(pady=15)
        Button(calc_frame, text="Regla de Cramer", command=self.cramer, width=30, height=3, font=("Arial", 16, "bold"), bg='blue', fg='white').pack(pady=15)
        Button(calc_frame, text="Multiplicación de Matrices", command=self.multiplicar, width=30, height=3, font=("Arial", 16, "bold"), bg='blue', fg='white').pack(pady=15)
        Button(calc_frame, text="Matriz Inversa", command=self.inversa, width=30, height=3, font=("Arial", 16, "bold"), bg='blue', fg='white').pack(pady=15)

        # Frame para el área de resultados
        result_frame = Frame(root, bg='#a8d5a2')
        result_frame.pack(side="left", padx=10, pady=0, anchor='n')

        # Etiqueta de resultados
        result_label = Label(result_frame, text="Resultado", bg='#a8d5a2', font=("Arial", 18, "bold"), fg='black')
        result_label.pack(pady=10)

        # Área de texto para mostrar resultados
        self.result_text = Text(result_frame, wrap="word", width=40, height=35, font=("Arial", 16), bg='#a8d5a2', relief="flat")
        self.result_text.pack(pady=5, fill="both", expand=True)
