import sympy as sym
x = sym.Symbol('x')  # khai bao bien x
y = sym.Symbol('y')  # khai bao bien y

fx = 2*x**2 - 1
dao_ham_bac_1 = sym.diff(fx, x)  # lấy đạo hàm bậc 1 theo biến x
print(dao_ham_bac_1)
dao_ham_bac_2 = sym.diff(fx, x, 2)  # lấy đạo hàm bậc 2 theo biến x
print(dao_ham_bac_2)

tich_phan_kxd = sym.integrate(fx, x)  # tính tích phân không xác định
print(tich_phan_kxd)
tich_phan_xd = sym.integrate(fx,(x, 1, 2))  # tính tích phân xác định với cận dưới là 1 và cận trên là 2
print(tich_phan_xd)

gioi_han = sym.limit(sym.sin(x)/x, x, 0)  # giới hạn của sin(x)/x  với x->0
print(gioi_han)

khai_trien_bt = sym.expand((x+y)**2)  # khai triển biểu thức (x + y) **2
print(khai_trien_bt)

rut_gon_bt = sym.simplify((x + x*y)/x)  # rút gọn biểu thức (x + x*y) / x
print(rut_gon_bt)

# độ chính xác
print((sym.pi).evalf(5))  # lấy số pi đến độ chính xác là 5 chữ số  dùng hàm evalf
print(sym.N(sym.sqrt(2),10))  # lấy căn bậc 2 của 2 đến độ chính xác là 10 chữ số  dùng hàm N

# xác định phân số đơn giản ban đầu
phan_so = sym.nsimplify(0.333333)
print(phan_so)
phan_so2 = sym.nsimplify(0.333333, tolerance=1e-2)
print(phan_so2)

# giải phương trình
ket_qua = sym.solve(x**2-1, x) # giai phương trình 1 ẩn
print(ket_qua)
ket_qua2 = sym.solve((x-5)*(y-6)) # giai hệ phương trình 2 ẩn
print(ket_qua2)
ket_qua3 = sym.solve((x+5*y-2, 3*x + 6*y-15), (x, y))
ket_qua3[x], ket_qua3[y]
print(ket_qua3)

# biến đổi Fourier



