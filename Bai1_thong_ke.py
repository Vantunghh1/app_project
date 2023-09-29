import tkinter as tk
import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox

df = pd.read_csv('diemPython.csv', index_col=0, header=0)
in_data = array(df.iloc[:, :])
def read_text_file():
    # Tạo một cửa sổ mới để hiển thị dữ liệu
    new_window = tk.Toplevel(window)
    new_window.title('Dữ liệu từ tệp văn bản')
    text_widget = tk.Text(new_window)
    text_widget.insert(tk.END, in_data)
    text_widget.pack()
def tong_SV_di_thi():
    new_window = tk.Toplevel(window)
    new_window.title('Tong so sinh vien di thi :')
    tongsv = in_data[:, 1]
    Tong = np.sum(tongsv)
    text_widget = tk.Text(new_window)
    text_widget.insert(tk.END, tongsv)

window = tk.Tk()
window.title('Giao diện Python')
window.geometry('600x600')

button = tk.Button(window, text='Hiển thị dữ liệu', command=read_text_file)
button.grid(column=1, row=0)


button2 = tk.Button(window, text='Tổng sinh viên đi thi', command=tong_SV_di_thi)
button2.grid(column=2, row=0)


window.mainloop()
