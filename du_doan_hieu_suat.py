import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('Student_Performance.csv')
# Dữ liệu đầu vào và đầu ra
# Tách biến đầu ra (Performance Index)
X = data.iloc[:, :-1]  # Tất cả các cột trừ cột cuối cùng
y = data.iloc[:, -1]   # Chỉ cột cuối cùng

# Tạo mô hình hồi quy tuyến tính
model = LinearRegression()

# Luyện mô hình trên dữ liệu
model.fit(X, y)

# Dự đoán chỉ số hiệu suất cho một số mẫu mới (ví dụ)
new_data = {}
new_data['Hours Studied'] = float(input("Nhập số giờ học: "))
new_data['Previous Scores'] = float(input("Nhập điểm trước đó: "))
new_data['Extracurricular Activities'] = int(input("Nhập số hoạt động ngoại khóa (0 hoặc 1): "))
new_data['Sleep Hours'] = float(input("Nhập số giờ ngủ: "))
new_data['Sample Question Papers Practiced'] = int(input("Nhập số lượng đề thử nghiệm đã làm: "))

# Chuyển dữ liệu dự đoán thành DataFrame
new_data_df = pd.DataFrame(new_data, index=[0])

# Dự đoán chỉ số hiệu suất cho dữ liệu mới
predicted_performance = model.predict(new_data_df)

print("\nDự đoán chỉ số hiệu suất cho dữ liệu mới:", predicted_performance[0])

# Đánh giá mô hình
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print("\nĐánh giá mô hình:")
print("MSE (Mean Squared Error):", mse)
print("R-squared (R2):", r2)