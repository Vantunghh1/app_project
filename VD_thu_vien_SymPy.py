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