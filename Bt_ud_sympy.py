from sympy import *
import tkinter as tk
<<<<<<< HEAD
from tkinter import ttk, messagebox
=======
from sympy import symbols, Eq, solve
from tkinter import ttk
from sympy import *

init_printing()
x, y, z = symbols('x y z')

>>>>>>> 55202b16ee0bd6d21f41da6a2d0976439b75c0c3

def tinh_toan_co_ban():
    new_window = tk.Toplevel(window)
    new_window.title('Tính toán cơ bản')

def tinh_toan_nang_cao():
    new_window = tk.Toplevel(window)
<<<<<<< HEAD
    new_window.title('Tong so sinh vien di thi :')
=======
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

>>>>>>> 55202b16ee0bd6d21f41da6a2d0976439b75c0c3

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
