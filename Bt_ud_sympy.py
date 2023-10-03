import tkinter as tk
import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox


def tinh_toan_co_ban():
    # Tạo một cửa sổ mới để hiển thị dữ liệu
    new_window = tk.Toplevel(window)
    new_window.title('Dữ liệu từ tệp văn bản')


    text_widget.pack()
def tinh_toan_nang_cao():
    new_window = tk.Toplevel(window)
    new_window.title('Tong so sinh vien di thi :')



def giai_phuong_trinh():
    new_window = tk.Toplevel(window)
    new_window.title('Du lieu ve sl diem A :')



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
