import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import easyocr
import sqlite3
from datetime import datetime

class LicensePlateRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng nhận diện biển số xe")

        self.dem_xe_vao = 0
        self.dem_xe_ra = 0
        self.so_xe_con_lai = 0

        # Biến lưu ảnh từ webcam
        self.webcam = cv2.VideoCapture(0)

        # Biến lưu ảnh chụp được
        self.captured_image = None

        # Biến lưu trạng thái của hệ thống (True nếu xe ra về, False nếu xe vào)
        self.system_status = False

        # Tạo và đặt vị trí các thành phần trên giao diện
        self.label_image = tk.Label(root)
        self.label_image.pack(pady=10)

        self.btn_nhan_dien = tk.Button(root, text="Nhận diện", command=self.capture_and_recognize_license_plate)
        self.btn_nhan_dien.pack(pady=5)

        self.label_hien_thi = tk.Label(root, text="Biển số xe: ")
        self.label_hien_thi.pack(pady=10)

        self.btn_save = tk.Button(root, text="Lưu", command=self.save_to_database)
        self.btn_save.pack(pady=5)

        self.btn_view_database = tk.Button(root, text="Xem Cơ sở dữ liệu", command=self.view_database)
        self.btn_view_database.pack(pady=5)

        self.btn_xoa_xe_ra = tk.Button(root, text="Xe Ra Về", command=self.process_vehicle_exit)
        self.btn_xoa_xe_ra.pack(pady=5)

        self.btn_delete_all = tk.Button(root, text="Xóa Tất Cả Dữ Liệu", command=self.delete_all_data)
        self.btn_delete_all.pack(pady=5)

        self.label_so_xe_vao = tk.Label(root, text="Số xe đã vào: 0")
        self.label_so_xe_vao.pack()

        self.label_so_xe_ra = tk.Label(root, text="Số xe đã ra: 0")
        self.label_so_xe_ra.pack()

        self.label_so_xe_con_lai = tk.Label(root, text="Tổng số xe còn lại: 0")
        self.label_so_xe_con_lai.pack()


        # Khởi tạo mô hình nhận diện biển số xe
        self.reader = easyocr.Reader(['en'])

        # Kết nối đến cơ sở dữ liệu SQLite
        self.conn = sqlite3.connect('license_plate_database.db')
        self.create_table()

        # Bắt đầu hiển thị hình ảnh từ webcam
        self.update_webcam()

    def create_table(self):
        # Tạo bảng trong cơ sở dữ liệu nếu chưa tồn tại
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS license_plates (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    plate_number TEXT,
                    capture_time TEXT
                )
            ''')

    def save_to_database(self):
        if self.detected_license_plate:

            # Reset giá trị AUTOINCREMENT
            self.reset_autoincrement()
            # Lưu vào cơ sở dữ liệu
            self.save_plate_to_database(self.detected_license_plate)
            # Cập nhật số xe đã vào và tổng số xe còn lại
            self.dem_xe_vao += 1
            self.so_xe_con_lai += 1

            # Hiển thị thông tin trên giao diện
            self.label_so_xe_vao.config(text=f"Số xe đã vào: {self.dem_xe_vao}")
            self.label_so_xe_con_lai.config(text=f"Tổng số xe còn lại: {self.so_xe_con_lai}")

            # Hiển thị thông báo lên giao diện
            self.label_hien_thi.config(text=f"Biển số xe: {self.detected_license_plate} đã được lưu")
            # Reset biến detected_license_plate sau khi lưu
            self.detected_license_plate = ""
        else:
            self.label_hien_thi.config(text="Vui lòng nhận diện biển số xe trước khi lưu")

    def save_plate_to_database(self, plate_number):
        # Lưu biển số và thời gian vào cơ sở dữ liệu
        capture_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO license_plates (plate_number, capture_time) VALUES (?, ?)', (plate_number, capture_time))

    def delete_all_data(self):
        # Xóa tất cả dữ liệu từ cơ sở dữ liệu
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM license_plates')

        # Reset giá trị AUTOINCREMENT
        self.reset_autoincrement()
        self.dem_xe_vao = 0
        self.dem_xe_ra = 0
        self.so_xe_con_lai = 0
        # Hiển thị thông tin trên giao diện
        self.label_so_xe_vao.config(text=f"Số xe đã vào: {self.dem_xe_vao}")
        self.label_so_xe_ra.config(text=f"Số xe đã ra: {self.dem_xe_ra}")
        self.label_so_xe_con_lai.config(text=f"Tổng số xe còn lại: {self.so_xe_con_lai}")
        # Hiển thị thông báo lên giao diện
        self.label_hien_thi.config(text="Đã xóa tất cả dữ liệu trong cơ sở dữ liệu")
    def capture_and_recognize_license_plate(self):
        if self.captured_image is not None:
            # Chuyển đổi ảnh sang đen trắng
            gray = cv2.cvtColor(self.captured_image, cv2.COLOR_BGR2GRAY)

            # Thực hiện OCR trên ảnh đen trắng để nhận diện biển số xe
            results = self.reader.readtext(gray)

            if results:
                # Kết hợp kết quả nhận diện trên hai hàng chữ
                license_plate_number = ' '.join([result[-2] for result in results])
                # Lưu biển số vào biến
                self.detected_license_plate = license_plate_number
                # Hiển thị biển số trên giao diện
                self.label_hien_thi.config(text=f"Biển số xe: {license_plate_number}")

            else:
                self.label_hien_thi.config(text="Không nhận diện được biển số xe")
        else:
            self.label_hien_thi.config(text="Vui lòng nhận diện biển số xe trước khi lưu")

    def update_webcam(self):
        # Đọc frame từ webcam
        ret, frame = self.webcam.read()

        # Hiển thị frame từ webcam
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        image = ImageTk.PhotoImage(image)
        self.label_image.config(image=image)
        self.label_image.image = image

        # Lặp lại hàm update_webcam sau một khoảng thời gian nhất định (ở đây là 10ms)
        self.root.after(10, self.update_webcam)

        # Lưu ảnh chụp được
        self.captured_image = frame

    def process_vehicle_exit(self):
        if self.captured_image is not None:
            # Chuyển đổi ảnh sang đen trắng
            gray = cv2.cvtColor(self.captured_image, cv2.COLOR_BGR2GRAY)

            # Thực hiện OCR trên ảnh đen trắng để nhận diện biển số xe
            results = self.reader.readtext(gray)

            if results:
                # Kết hợp kết quả nhận diện trên hai hàng chữ
                license_plate_number = ' '.join([result[-2] for result in results])

                # Kiểm tra xem biển số có trong cơ sở dữ liệu không
                if self.check_plate_in_database(license_plate_number):
                    # Nếu có, hiển thị thông báo
                    self.label_hien_thi.config(text=f"Biển số xe: {license_plate_number} đã ra khỏi bãi đỗ")
                    # Sau đó, xóa biển số từ cơ sở dữ liệu
                    self.remove_plate(license_plate_number)
                    # Reset giá trị AUTOINCREMENT
                    self.reset_autoincrement()
                    # Cập nhật số xe đã ra và tổng số xe còn lại
                    self.dem_xe_ra += 1
                    self.so_xe_con_lai -= 1

                    # Hiển thị thông tin trên giao diện
                    self.label_so_xe_ra.config(text=f"Số xe đã ra: {self.dem_xe_ra}")
                    self.label_so_xe_con_lai.config(text=f"Tổng số xe còn lại: {self.so_xe_con_lai}")
                else:
                    self.label_hien_thi.config(text=f"Biển số xe: {license_plate_number} không có trong cơ sở dữ liệu")
            else:
                self.label_hien_thi.config(text="Không nhận diện được biển số xe")
        else:
            self.label_hien_thi.config(text="Vui lòng nhận diện biển số xe trước khi xử lý xe ra về")

    def check_plate_in_database(self, plate_number):
        # Kiểm tra xem biển số có trong cơ sở dữ liệu không
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM license_plates WHERE plate_number = ?', (plate_number,))
            return cursor.fetchone() is not None

    def reset_autoincrement(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM sqlite_sequence WHERE name="license_plates"')

    def remove_plate(self, plate_number):
        # Xóa biển số từ cơ sở dữ liệu
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM license_plates WHERE plate_number = ?', (plate_number,))




    def view_database(self):
        # Tạo cửa sổ mới để hiển thị cơ sở dữ liệu
        database_window = tk.Toplevel(self.root)
        database_window.title("Cơ sở dữ liệu biển số xe")

        # Tạo cây để hiển thị dữ liệu từ cơ sở dữ liệu
        tree = ttk.Treeview(database_window)
        tree["columns"] = ("ID", "Biển số xe", "Thời gian")

        # Đặt độ rộng cho từng cột
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("ID", anchor=tk.CENTER, width=50)
        tree.column("Biển số xe", anchor=tk.CENTER, width=150)
        tree.column("Thời gian", anchor=tk.CENTER, width=150)

        # Đặt tiêu đề cho từng cột
        tree.heading("#0", text="", anchor=tk.CENTER)
        tree.heading("ID", text="ID", anchor=tk.CENTER)
        tree.heading("Biển số xe", text="Biển số xe", anchor=tk.CENTER)
        tree.heading("Thời gian", text="Thời gian", anchor=tk.CENTER)

        # Truy vấn cơ sở dữ liệu và hiển thị dữ liệu trong cây
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM license_plates")
            rows = cursor.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)

        tree.pack(expand=tk.YES, fill=tk.BOTH)

if __name__ == "__main__":
    root = tk.Tk()
    app = LicensePlateRecognitionApp(root)
    root.mainloop()
