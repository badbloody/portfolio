import cv2
import os

def resize_images(input_folder, output_folder, desired_size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
  	
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            img = cv2.imread(os.path.join(input_folder, filename))

            resized_img = cv2.resize(img, desired_size, interpolation=cv2.INTER_AREA)

            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, resized_img)

if __name__ == "__main__":
    input_folder = "images"  
    output_folder = "thumbnails"  
    desired_size = (300, 300)  
    resize_images(input_folder, output_folder, desired_size)
