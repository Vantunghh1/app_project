import cv2
import numpy as np

def rotate_image(image, angle):
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

image_path = input("Nhập đường dẫn của ảnh: ")
image = cv2.imread(image_path)

if image is None:
    print("Không thể đọc ảnh")
else:
    while True:
        angle = float(input("Nhập góc quay (độ): "))
        cv2.imshow("Ảnh gốc", image)
        rotated_image = rotate_image(image, angle)
        cv2.imshow("Ảnh sau khi quay", rotated_image)
        cv2.waitKey(0)
        angle2 = float(input("Nhập góc quay moi(độ): "))
        cv2.imshow("Ảnh gốc", image)
        rotated_image = rotate_image(image, angle2)
        cv2.imshow("Ảnh sau khi quay", rotated_image)
        cv2.waitKey(0)
cv2.destroyAllWindows()
