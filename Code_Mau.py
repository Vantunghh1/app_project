import cv2  # for image processing
import easygui  # Thư viện cho phép mở hộp thoại chọn tệp ảnh.

import matplotlib.pyplot as plt # Được sử dụng để hiển thị và vẽ hình ảnh.
import os  #  Cung cấp các hàm liên quan đến hệ điều hành
import tkinter as tk
from tkinter import *
from tkinter import filedialog  # Sử dụng thư viện filedialog cho hộp thoại lưu

top = tk.Tk()
top.geometry('400x400')
top.title('Cartoonify Your Image !')
top.configure(background='white')
label = Label(top, background='#CDCDCD', font=('calibri', 20, 'bold'))


def upload():
    # sử dụng easygui để mở hộp thoại chọn tệp
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)  # Gọi hàm cartoonify với đường dẫn tệp ảnh được chọn


def cartoonify(ImagePath): # Hàm tạo hiệu ứng vẽ tranh cho hình ảnh

    originalmage = cv2.imread(ImagePath)  # Đọc hình ảnh từ đường dẫn
    originalmage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2RGB)  # Chuyển đổi không gian màu BGR sang RGB

    # Kiểm tra nếu không tìm thấy hình ảnh
    if originalmage is None:
        print("Can not find any image. Choose appropriate file")
        sys.exit()  # Thoát chương trình nếu không tìm thấy hình ảnh

    ReSized1 = cv2.resize(originalmage, (960, 540))

    # converting an image to grayscale
    grayScaleImage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2GRAY)  # Chuyển đổi hình ảnh sang ảnh xám
    ReSized2 = cv2.resize(grayScaleImage, (960, 540))

    # applying median blur to smoothen an image
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)   # Làm mờ ảnh xám bằng median blur
    ReSized3 = cv2.resize(smoothGrayScale, (960, 540))

    # retrieving the edges for cartoon effect
    # by using thresholding technique         xác định biên bằng cách sử dụng ngưỡng
    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 9, 9)

    ReSized4 = cv2.resize(getEdge, (960, 540))
    colorImage = cv2.bilateralFilter(originalmage, 9, 300, 300)  # Lọc song song để tăng cường biên và màu sắc
    ReSized5 = cv2.resize(colorImage, (960, 540))

    # masking edged image with our "BEAUTIFY" image
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge) # Áp dụng mặt nạ biên cho hình ảnh màu

    ReSized6 = cv2.resize(cartoonImage, (960, 540))
    # plt.imshow(ReSized6, cmap='gray')

    # Plotting the whole transition
    images = [ReSized1, ReSized2, ReSized3, ReSized4, ReSized5, ReSized6]

    fig, axes = plt.subplots(3, 2, figsize=(8, 8), subplot_kw={'xticks': [], 'yticks': []},
                             gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')

    save1 = Button(top, text="Lưu ảnh hoạt hình", command=lambda: save(ReSized6, ImagePath), padx=30, pady=5)
    save1.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
    save1.pack(side=TOP, pady=50)
    plt.show()

def save(ReSized6, ImagePath):
    newName = "cartoonified_Image"
    path1 = os.path.dirname(ImagePath)
    extension = os.path.splitext(ImagePath)[1]
    save_path = filedialog.asksaveasfilename(defaultextension=extension, filetypes=[("Image Files", "*" + extension)])
    if save_path:
        cv2.imwrite(save_path, cv2.cvtColor(ReSized6, cv2.COLOR_RGB2BGR))
        I = "Image saved by name " + newName + " at " + save_path
        tk.messagebox.showinfo(title=None, message=I)


upload = Button(top, text="Chọn ảnh", command=upload, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
upload.pack(side=TOP, pady=50)

top.mainloop()



