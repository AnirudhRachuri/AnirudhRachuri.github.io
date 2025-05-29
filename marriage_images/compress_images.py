import os
from PIL import Image

def compress_under_size(size, file_path):
    '''file_path is a string to the file to be custom compressed
    and the size is the maximum size in bytes it can be which this 
    function searches until it achieves an approximate supremum'''

    quality = 90 #not the best value as this usually increases size

    current_size = os.stat(file_path).st_size

    picture_og = Image.open(file_path)
    while current_size > size or quality == 0:
        picture_og.save(file_path,"JPEG", optimize=True, quality=100) 

        if quality == 0:
            os.remove(file_path)
            print("Error: File cannot be compressed below this size")
            break
        print(f"Compressing {file_path} to {quality}% quality")
        compress_pic(file_path, quality)
        current_size = os.stat(file_path).st_size
        quality -= 5


def compress_pic(file_path, qual):
    '''File path is a string to the file to be compressed and
    quality is the quality to be compressed down to'''
    picture = Image.open(file_path)

    # ensure the image is in potrait orientation
    if picture.width > picture.height:
        picture = picture.rotate(90, expand=True)

    picture.save(file_path,"JPEG", optimize=True, quality=qual) 

    processed_size = os.stat(file_path).st_size

    return processed_size

dir_path = "./"

for file in os.listdir(dir_path):
    try:
        pic = f"{dir_path}/{file}"
        print(f"Compressing {pic} to 1MB")
        compress_under_size(1000000, pic)
    except Exception:
        print(f"Error processing {file}. It may not be a valid image file.")
        pass