#bài này giải hệ phương trình x+2y=5 và 3x+4y =6
# Yêu cầu hoàn chỉnh lại đoạn code
#để có 1 app giải hệ phương trình có n phương trình n ẩn
import numpy as np
a1 = int(input("Nhap a1="))
a2 = int(input("Nhap a2="))
a3 = int(input("Nhap a3="))
a4 = int(input("Nhap a4="))

b1 = int(input("Nhap b1="))
b2 = int(input("Nhap b2="))
A = np.array([(a1,a2),(a3,a4)])
B = np.array([b1,b2])
A1  = np.linalg.inv(A) # tạo ma trận nghich đảo
print(A)
print(B)
print(A1)
X = np.dot(A1,B)
print('Nghiem cua he:',X)
