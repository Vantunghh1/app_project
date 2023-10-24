import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk

# Khai báo biến toàn cục
img = None
drawing = False
ix, iy = -1, -1
fx, fy = -1, -1

# Define kernels
kernel_sharpen_1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
kernel_sharpen_2 = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]])
kernel_sharpen_3 = np.array([[-1, -1, -1, -1, -1],
                            [-1, 2, 2, 2, -1],
                            [-1, 2, 8, 2, -1],
                            [-1, 2, 2, 2, -1],
                            [-1, -1, -1, -1, -1]]) / 8.0

# Hàm để hiển thị ảnh trên giao diện
def hien_thi_anh(image_to_display):
    img = Image.fromarray(cv2.cvtColor(image_to_display, cv2.COLOR_BGR2RGB))
    img = ImageTk.PhotoImage(image=img)
    panel.configure(image=img)
    panel.image = img

# Hàm xử lý sự kiện khi chuột được nhấn xuống để bắt đầu vẽ hình chữ nhật
def chuot_nhan_xuong(event):
    global drawing, ix, iy
    drawing = True
    ix, iy = event.x, event.y

# Hàm xử lý sự kiện khi chuột được kéo để vẽ hình chữ nhật
def chuot_keo(event):
    global img, drawing, ix, iy, fx, fy
    if drawing:
        fx, fy = event.x, event.y
        img_copy = img.copy()
        cv2.rectangle(img_copy, (ix, iy), (fx, fy), (0, 255, 0), 2)
        hien_thi_anh(img_copy)

# Hàm xử lý sự kiện khi chuột được thả ra sau khi vẽ xong hình chữ nhật
def chuot_tha(event):
    global drawing, ix, iy, fx, fy, img
    if drawing:
        drawing = False
        roi = img[iy:fy, ix:fx]
        # Áp dụng mờ Gaussian lên vùng đã khoanh vùng
        blurred_roi = cv2.GaussianBlur(roi, (15, 15), 0)
        img[iy:fy, ix:fx] = blurred_roi
        hien_thi_anh(img)

# Hàm khi nút "Mở ảnh" được nhấn
def mo_anh():
    global img
    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path)
        # Thay đổi kích thước thành 500x500
        img = cv2.resize(img, (500, 500))
        hien_thi_anh(img)

# Hàm xử lý sự kiện khi nút "Làm nét ảnh" được nhấn
def update_sharpness_and_brightness(kernel):
    global img
    sharpness = sharpness_var.get()
    brightness = brightness_var.get()
    sharpened = cv2.filter2D(img, -1, kernel * sharpness)
    adjusted_brightness = cv2.convertScaleAbs(sharpened, alpha=brightness, beta=0)
    cv2.imshow('Sharpened and Brightened Image', adjusted_brightness)
    # Lưu ảnh sau khi đã làm nét và điều chỉnh độ sáng
    cv2.imwrite('sharpened_image.jpg', adjusted_brightness)
    global edited_img
    edited_img = adjusted_brightness

# Hàm khi nút "Lưu ảnh" được nhấn
def save_image():
    if 'edited_img' in globals():
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if file_path:
            cv2.imwrite(file_path, edited_img)
            print(f"Saved edited image as {file_path}")
    else:
        print("Không có ảnh để lưu. Vui lòng chọn ảnh và thực hiện chỉnh sửa trước.")

# Tạo cửa sổ giao diện
top = tk.Tk()
top.title("Xử Lý Ảnh và Tăng cường Sắc nét")

# Tạo nút "Mở ảnh"
open_button = tk.Button(top, text="Mở ảnh", command=mo_anh)
open_button.pack()

# Panel để hiển thị ảnh
panel = tk.Label(top)
panel.pack()

# Gắn các sự kiện chuột để vẽ hình chữ nhật
panel.bind("<Button-1>", chuot_nhan_xuong)
panel.bind("<B1-Motion>", chuot_keo)
panel.bind("<ButtonRelease-1>", chuot_tha)

# Tạo thanh trượt để điều chỉnh độ sắc nét
sharpness_var = tk.DoubleVar()
sharpness_slider = ttk.Scale(top, from_=0.1, to=3.0, variable=sharpness_var, orient="horizontal", length=200)
sharpness_slider.pack()
sharpness_slider.set(1.0)

# Tạo thanh trượt để điều chỉnh độ sáng
brightness_var = tk.DoubleVar()
brightness_slider = ttk.Scale(top, from_=0.1, to=3.0, variable=brightness_var, orient="horizontal", length=200)
brightness_slider.pack()
brightness_slider.set(1.0)

# Tạo nút "Làm nét ảnh" và các kernel sharpen
btn_sharpen_1 = tk.Button(top, text="Sử dụng Kernel 1", command=lambda: update_sharpness_and_brightness(kernel_sharpen_1))
btn_sharpen_1.pack()
btn_sharpen_2 = tk.Button(top, text="Sử dụng Kernel 2", command=lambda: update_sharpness_and_brightness(kernel_sharpen_2))
btn_sharpen_2.pack()
btn_sharpen_3 = tk.Button(top, text="Sử dụng Kernel 3", command=lambda: update_sharpness_and_brightness(kernel_sharpen_3))
btn_sharpen_3.pack()

# Tạo nút "Lưu ảnh"
btn_save = tk.Button(top, text="Lưu Ảnh", command=save_image)
btn_save.pack()

top.mainloop()
