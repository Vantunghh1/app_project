#bài này giải hệ phương trình x+2y=5 và 3x+4y =6
# Yêu cầu hoàn chỉnh lại đoạn code
#để có 1 app giải hệ phương trình có n phương trình n ẩn
import numpy as np
print("bai tap nhom 11")

print("Cua so don gian giai phuong trinh bac hai")
import numpy as np
import tkinter as tk
from tkinter import Label, Entry, Button


def solve_equation():
    a1 = int(a1_entry.get())
    a2 = int(a2_entry.get())
    a3 = int(a3_entry.get())
    a4 = int(a4_entry.get())
    b1 = int(b1_entry.get())
    b2 = int(b2_entry.get())

    A = np.array([(a1, a2), (a3, a4)])
    B = np.array([b1, b2])

    A1 = np.linalg.inv(A)
    X = np.dot(A1, B)
    det_A = np.linalg.det(A1)
    if det_A == 0:
        result_label.config(text=f'Vo nghiem')
    else:
        result_label.config(text=f'Nghiem cua he: {X}')


root = tk.Tk()
root.title("Giai phuong trinh bac hai")

frame = tk.Frame(root)
frame.pack()

Label(frame, text="Nhom 11").grid(row=0, column=0, columnspan=2)
Label(frame, text="Nhap a1=").grid(row=1, column=0)
Label(frame, text="Nhap a2=").grid(row=2, column=0)
Label(frame, text="Nhap a3=").grid(row=3, column=0)
Label(frame, text="Nhap a4=").grid(row=4, column=0)
Label(frame, text="Nhap b1=").grid(row=5, column=0)
Label(frame, text="Nhap b2=").grid(row=6, column=0)

a1_entry = Entry(frame)
a2_entry = Entry(frame)
a3_entry = Entry(frame)
a4_entry = Entry(frame)
b1_entry = Entry(frame)
b2_entry = Entry(frame)

a1_entry.grid(row=1, column=1)
a2_entry.grid(row=2, column=1)
a3_entry.grid(row=3, column=1)
a4_entry.grid(row=4, column=1)
b1_entry.grid(row=5, column=1)
b2_entry.grid(row=6, column=1)

solve_button = Button(frame, text="Giai phuong trinh", command=solve_equation)
solve_button.grid(row=7, column=0, columnspan=2)

result_label = Label(frame, text="")
result_label.grid(row=8, column=0, columnspan=2)

root.mainloop()

