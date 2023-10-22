import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image, ImageTk

image = None

# Hàm để tách biên ảnh
def tach_bien_anh():
    global image
    if image is None:
        messagebox.showerror("Lỗi", "Vui lòng mở một ảnh trước.")
        return

    lower_threshold = simpledialog.askinteger("Tách biên", "Nhập ngưỡng dưới:")
    upper_threshold = simpledialog.askinteger("Tách biên", "Nhập ngưỡng trên:")

    if lower_threshold is not None and upper_threshold is not None:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        canny_image = cv2.Canny(gray_image, lower_threshold, upper_threshold)
        hien_thi_anh(canny_image)

# Hàm để hiển thị ảnh trên giao diện
def hien_thi_anh(image_to_display):
    img = Image.fromarray(cv2.cvtColor(image_to_display, cv2.COLOR_BGR2RGB))
    img = ImageTk.PhotoImage(image=img)
    panel.configure(image=img)
    panel.image = img

# Hàm khi nút "Mở ảnh" được nhấn
def mo_anh():
    global image
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        hien_thi_anh(image)

# Hàm khi nút "Zoom In/Out" được nhấn
def zoom_in_out():
    global image
    if image is None:
        messagebox.showerror("Lỗi", "Vui lòng mở một ảnh trước.")
        return

    factor = simpledialog.askfloat("Phóng to/Thu nhỏ", "Nhập tỉ lệ phóng to/thu nhỏ (1.0 là tỉ lệ ban đầu):")
    if factor is not None:
        scaled_image = cv2.resize(image, None, fx=factor, fy=factor)
        hien_thi_anh(scaled_image)

# Hàm khi nút "Xoay ảnh" được nhấn
def xoay_anh():
    global image
    if image is None:
        messagebox.showerror("Lỗi", "Vui lòng mở một ảnh trước.")
        return

    degree = simpledialog.askfloat("Xoay ảnh", "Nhập góc quay:")
    if degree is not None:
        height, width = image.shape[:2]
        center = (width / 2, height / 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, degree, 1.0)
        rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
        hien_thi_anh(rotated_image)

# Hàm khi nút "Chuẩn hóa" được nhấn
def chuan_hoa_anh():
    global image
    if image is None:
        messagebox.showerror("Lỗi", "Vui lòng mở một ảnh trước.")
        return

    normalized_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
    hien_thi_anh(normalized_image)

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Xử Lý Ảnh")

# Tạo nút "Mở ảnh"
open_button = tk.Button(root, text="Mở ảnh", command=mo_anh)
open_button.pack()

# Tạo nút "Zoom In/Out"
zoom_button = tk.Button(root, text="Phóng to/Thu nhỏ", command=zoom_in_out)
zoom_button.pack()

# Tạo nút "Xoay ảnh"
rotate_button = tk.Button(root, text="Xoay ảnh", command=xoay_anh)
rotate_button.pack()

# Tạo nút "Chuẩn hóa"
normalize_button = tk.Button(root, text="Chuẩn hóa", command=chuan_hoa_anh)
normalize_button.pack()

# Tạo nút "Tách biên"
edge_button = tk.Button(root, text="Tách biên", command=tach_bien_anh)
edge_button.pack()

# Panel để hiển thị ảnh
panel = tk.Label(root)
panel.pack()

root.mainloop()
