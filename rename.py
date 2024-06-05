import os
from PIL import Image

# convert images to png
def convert_images_to_png(directory):
    images = os.listdir(directory)
    array_to_remove = [] 
    converted = False

    # Convert .jpg and .webp images to .png.
    for file in images:
        file_path = os.path.join(directory, file)
        file_name, file_ext = os.path.splitext(file)
        
        if file_ext.lower() in ['.jpg', '.webp']:
            img = Image.open(file_path)
            new_file_path = get_unique_file_path(directory, file_name + '.png')
            img.save(new_file_path, 'PNG')
            print(f"{file} converted to {os.path.basename(new_file_path)}")
            
            if file_ext.lower() in ['.jpg', '.webp']:
                array_to_remove.append(file_path)
            converted = True

    # Remove the jpg and webp files after converting
    for file in array_to_remove:
        os.remove(file)
        print(f"{file} was deleted")
    if not converted:
        print("No .jpg or .webp files to convert")


# Ensure the file path is unique to avoid overwriting existing files.
def get_unique_file_path(directory, file_name):
    base_name, ext = os.path.splitext(file_name)
    counter = 1
    unique_file_path = os.path.join(directory, file_name)
    
    while os.path.exists(unique_file_path):
        unique_file_path = os.path.join(directory, f"{base_name}_{counter}{ext}")
        counter += 1

    return unique_file_path

# Rename .png images in the directory to a sequential numeric order.
def rename_images(directory):
    images = os.listdir(directory)
    png_files = sorted([file for file in images if file.endswith('.png')])
    renamed = False
    
    for counter, file in enumerate(png_files, start=1):
        new_file_name = f"{counter}.png"
        new_file_path = os.path.join(directory, new_file_name)
        current_file_path = os.path.join(directory, file)
        
        if current_file_path != new_file_path:
            new_file_path = get_unique_file_path(directory, new_file_name)
            os.rename(current_file_path, new_file_path)
            print(f"{file} renamed to {os.path.basename(new_file_path)}")
            renamed = True
    
    if not renamed:
        print("No .png files to rename")

# Main function to handle the image conversion and renaming process.
def main():
    directory = '.'  # current directory, can be changed to the desired one
    convert_images_to_png(directory)
    rename_images(directory)

if __name__ == "__main__":
    main()
