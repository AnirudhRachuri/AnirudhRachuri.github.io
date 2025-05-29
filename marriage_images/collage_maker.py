from PIL import Image

def make_portrait_collage(image_path1, image_path2, output_path='portrait_collage.jpg'):
    # Open both images
    img1 = Image.open(image_path1)
    img2 = Image.open(image_path2)

    # Resize both images to have the same width (min of the two)
    target_width = min(img1.width, img2.width)

    def resize_to_width(img, width):
        aspect_ratio = img.height / img.width
        new_height = int(width * aspect_ratio)
        return img.resize((width, new_height), Image.ANTIALIAS)

    img1_resized = resize_to_width(img1, target_width)
    img2_resized = resize_to_width(img2, target_width)

    # Create a new image with portrait orientation (vertical stacking)
    total_height = img1_resized.height + img2_resized.height
    collage = Image.new('RGB', (target_width, total_height))

    # Paste images
    collage.paste(img1_resized, (0, 0))
    collage.paste(img2_resized, (0, img1_resized.height))

    # Save the result
    collage.save(output_path)
    print(f"Portrait collage saved as {output_path}")

# Example usage
make_portrait_collage("RCM02507.JPG", "0I1A3634.JPG", "image4.jpg")
