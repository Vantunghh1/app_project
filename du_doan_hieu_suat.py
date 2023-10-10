import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Đọc dữ liệu từ tệp CSV
data = pd.read_csv('Student_Performance.csv')

# Tách biến đầu ra (Performance Index)
X = data.iloc[:, :-1]  # Tất cả các cột trừ cột cuối cùng
y = data.iloc[:, -1]   # Chỉ cột cuối cùng

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Xây dựng mô hình hồi quy tuyến tính sử dụng TensorFlow
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Luyện mô hình
history = model.fit(X_train, y_train, epochs=100, verbose=0)

# Dự đoán chỉ số hiệu suất trên tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá mô hình
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("MSE (Mean Squared Error) trên tập kiểm tra:", mse)
print("R-squared (R2) trên tập kiểm tra:", r2)

# Vẽ biểu đồ dự đoán và thực tế
plt.scatter(y_test, y_pred)
plt.xlabel("Chỉ số hiệu suất thực tế")
plt.ylabel("Chỉ số hiệu suất dự đoán")
plt.title("Biểu đồ dự đoán và thực tế")
plt.show()

# Nhập dữ liệu dự đoán từ bàn phím và dự đoán
new_data = {}
new_data['Hours Studied'] = float(input("Nhập số giờ học: "))
new_data['Previous Scores'] = float(input("Nhập điểm trước đó: "))
new_data['Extracurricular Activities'] = int(input("Nhập số hoạt động ngoại khóa (0 hoặc 1): "))
new_data['Sleep Hours'] = float(input("Nhập số giờ ngủ: "))
new_data['Sample Question Papers Practiced'] = int(input("Nhập số lượng đề thử nghiệm đã làm: "))

# Chuyển dữ liệu dự đoán thành một DataFrame
new_data_df = pd.DataFrame([new_data])

# Dự đoán chỉ số hiệu suất cho dữ liệu mới
predicted_performance = model.predict(new_data_df)
print("\nDự đoán chỉ số hiệu suất cho dữ liệu mới:", predicted_performance[0][0])