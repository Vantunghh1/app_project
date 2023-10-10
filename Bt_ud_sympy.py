from sympy import *
import tkinter as tk
from tkinter import ttk, messagebox

def tinh_toan_co_ban():
    new_window = tk.Toplevel(window)
    new_window.title('Tinh toan co ban')

def tinh_toan_nang_cao():
    new_window = tk.Toplevel(window)
    new_window.title('Tong so sinh vien di thi :')

def giai_phuong_trinh():
    new_window = tk.Toplevel(window)
    new_window.title('Giai phuong trinh bac n')
    new_window.geometry('600x600')

    def create_coefficient_input_fields():
        for entry in coefficient_entries:
            entry.destroy()

        degree = int(degree_entry.get())
        if degree <= 0:
            messagebox.showerror("Lỗi", "Bậc n phải là một số nguyên dương.")
            return

        coefficient_labels.clear()
        coefficient_entries.clear()

        for i in range(degree + 1):
            label = ttk.Label(new_window, text=f"Nhập hệ số a{i}:")
            label.pack()
            entry_var = tk.StringVar()
            entry = ttk.Entry(new_window, textvariable=entry_var)
            entry.pack()
            coefficient_labels.append(label)
            coefficient_entries.append(entry)

    def calculate_equation():
        degree = int(degree_entry.get())

        if degree <= 0:
            messagebox.showerror("Lỗi", "Bậc n phải là một số nguyên dương.")
            return

        coefficients = []
        for i in range(degree + 1):
            try:
                coefficient = float(coefficient_entries[i].get())
                coefficients.append(coefficient)
            except ValueError:
                messagebox.showerror("Lỗi", f"Hệ số a{i} không hợp lệ.")

        x = symbols('x')
        equation = Eq(sum(coefficients[i] * x ** i for i in range(degree + 1)), 0)

        solutions = solve(equation, x)

        solutions_label.config(text="Nghiệm của phương trình:")
        for solution in solutions:
            solutions_label.config(text=solutions_label.cget("text") + f"\nx = {solution}")

    degree_label = ttk.Label(new_window, text="Nhập bậc n:")
    degree_label.pack(pady=10)

    degree_entry = ttk.Entry(new_window)
    degree_entry.pack()

    create_button = ttk.Button(new_window, text="Tạo hệ số", command=create_coefficient_input_fields)
    create_button.pack(pady=10)

    coefficient_labels = []
    coefficient_entries = []

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
