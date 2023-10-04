from sympy import *
from tkinter import *
from tkinter import messagebox
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from sympy import symbols, Eq, solve
from tkinter import ttk
from sympy import *

init_printing()
x, y, z = symbols('x y z')


def tinh_toan_co_ban():
    # Tạo một cửa sổ mới để hiển thị dữ liệu
    new_window = tk.Toplevel(window)
    new_window.title('Tính toán cơ bản')

def tinh_toan_nang_cao():
    new_window = tk.Toplevel(window)
    new_window.title('Tính toán nâng cao')
    new_window.geometry("600x600")
    Nhap_x = ttk.Label(new_window, text="Nhập a:")
    Nhap_y = ttk.Label(new_window, text="Nhập b:")
    Nhap_z = ttk.Label(new_window, text="Nhập c:")
    Nhap_x.grid(column = 5, row = 1)
    Nhap_y.grid(column = 5, row = 2)
    Nhap_z.grid(column = 5, row = 3)
    nhapx = ttk.Entry(new_window)
    nhapx.grid(column = 6, row = 1)
    nhapy = ttk.Entry(new_window)
    nhapy.grid(column = 6, row = 2)
    nhapz = ttk.Entry(new_window)
    nhapz.grid(column = 6, row = 3)
    show1 = ttk.Label(new_window,text =  " ");
    show1.grid(column = 3, row = 5)
    show2 = ttk.Label(new_window,text = " ");
    show2.grid(column=3, row=6)
    show3 = ttk.Label(new_window,text = " ");
    show3.grid(column=3, row=7)
    def calculate():
        a = int(nhapx.get())
        b = int(nhapy.get())
        c = int(nhapz.get())
        eq = Eq(x ** a + b * x + c, 0)
        # giai phuong trinh
        solutions = solve(eq, x)
        # tinh gioi han
        limit_expr = limit(sin(x) / x, x, 0)
        # Tính đạo hàm
        diff_expr = diff(cos(x), x)
        show1.config(text="Kết quả của giải phương trình là: " + str(solutions))
        show2.config(text="Kết quả của tính giới hạn: " + str(limit_expr))
        show3.config(text="Kết quả của tính đạo hàm: " + str(diff_expr))
    buttona = Button(new_window, text="Tinh toan", command = calculate)
    buttona.grid(column=6, row=4)


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
