from PIL import Image
import os

path = "previous_projects/"

for root, dirs, files in os.walk(path):
    print(files)
    for file in files:
        if file.endswith(".bmp"):
            img_path = os.path.join(root, file)
            print(img_path)
            new_img_path = os.path.join(root, file.replace(".bmp", ".png"))

            # Open the image and save it as PNG
            Image.open(img_path).save(new_img_path)

            # Remove the original BMP
            os.remove(img_path)
