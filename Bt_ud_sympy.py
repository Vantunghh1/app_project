from sympy import *
from tkinter import *
from tkinter import messagebox
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from sympy import symbols, Eq, solve
from tkinter import ttk


def tinh_toan_co_ban():
    # Tạo một cửa sổ mới để hiển thị dữ liệu
    new_window = tk.Toplevel(window)
    new_window.title('Tinh toan co ban')

    text_widget.pack()
def tinh_toan_nang_cao():
    new_window = tk.Toplevel(window)
    new_window.title('Tong so sinh vien di thi :')



def giai_phuong_trinh():
    new_window = tk.Toplevel(window)
    new_window.title('Giai phuong trinh bac n')
    new_window.geometry('600x600')
    # Nhập bậc của phương trình

    def calculate_equation():
        input_text = degree_entry.get()
        if not input_text:
            messagebox.showerror("Lỗi", "Vui lòng nhập bậc n.")
            return

        try:
            n = int(input_text)
            x = symbols('x')

            coefficients = []
            for i in range(n + 1):
                coefficient = float(input(f"Nhập hệ số a{i}: "))
                coefficients.append(coefficient)

            # Tạo phương trình
            equation = Eq(sum(coefficients[i] * x ** i for i in range(n + 1)), 0)

            # Giải phương trình
            solutions = solve(equation, x)

            print("Nghiệm của phương trình:")
            for solution in solutions:
                print(f"x = {solution}")

            equation = Eq(x ** n, 0)
            solutions = solve(equation, x)
            solutions_label.config(text=f"Giải phương trình: {solutions}")
        except ValueError:
            messagebox.showerror("Lỗi", "Bậc n phải là một số nguyên.")




    degree_label = ttk.Label(new_window, text="Nhập bậc n:")
    degree_label.pack(pady=10)

    degree_entry = ttk.Entry(new_window)
    degree_entry.pack()

    calculate_button = ttk.Button(new_window, text="Tính phương trình", command=calculate_equation)
    calculate_button.pack(pady=10)

    solutions_label = ttk.Label(new_window, text="")
    solutions_label.pack()


window = tk.Tk()
window.title('Giao diện Python')
window.geometry('600x600')

button1 = tk.Button(window, text='Tinh toan co ban ', command=tinh_toan_co_ban)
button1.grid(column=1, row=0)


button2 = tk.Button(window, text='Tinh toan nang cao', command=tinh_toan_nang_cao)
button2.grid(column=2, row=0)

button3 = tk.Button(window, text='Giai phuong trinh', command=giai_phuong_trinh)
button3.grid(column=3, row=0)


window.mainloop()
