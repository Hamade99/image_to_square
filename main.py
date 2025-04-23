import os
from PIL import Image

def crop_center_square(img):
    width, height = img.size
    new_edge = min(width, height)
    left = (width - new_edge) // 2
    top = (height - new_edge) // 2
    right = left + new_edge
    bottom = top + new_edge
    return img.crop((left, top, right, bottom))

def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                with Image.open(input_path) as img:
                    img = img.convert("RGB")  # Ensures compatibility
                    cropped = crop_center_square(img)
                    cropped.save(output_path)
                    print(f"Cropped and saved: {output_path}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage:
process_images(r"C:\Users\A\Desktop\Code things\Shia Whispers\images\unformatted", r"C:\Users\A\Desktop\Code things\Shia Whispers\images")
