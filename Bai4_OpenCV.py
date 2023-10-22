# Nhập vào 1 ảnh, nhập vào 2 ngưỡng, sử dụng kĩ thuật tách biên để tách biên ảnh
# Hiển thị ảnh ban đầu và ảnh sau khi tách biên

import cv2

def main():
    image_path = input("Nhập đường dẫn tới ảnh: ")
    image = cv2.imread(image_path)
    if image is None:
        print("Không thể đọc ảnh. Vui lòng kiểm tra lại đường dẫn.")
        return
    while True:
        lower_threshold = int(input("Nhập ngưỡng dưới: "))
        upper_threshold = int(input("Nhập ngưỡng trên: "))
        cv2.imshow("Ảnh ban đầu", image)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        canny_image = cv2.Canny(gray_image, lower_threshold, upper_threshold)
        cv2.imshow("Ảnh sau khi tách biên", canny_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()