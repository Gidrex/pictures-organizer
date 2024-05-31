import os
from PIL import Image

# Function to convert all jpg to png
def convert_jpg_to_png(directory):
    images = os.listdir(directory)
    files_to_remove = []
    converted = False
    for file in images:
        if file.endswith('.jpg'):
            img = Image.open(os.path.join(directory, file))
            file_name = os.path.splitext(file)[0]
            new_file_path = os.path.join(directory, file_name + '.png')
            img.save(new_file_path, 'PNG')
            print(f"{file} converted to {file_name}.png")
            files_to_remove.append(os.path.join(directory, file))
            converted = True
    # Remove the jpg files after converting
    for file in files_to_remove:
        os.remove(file)
        print(f"{file} was deleted")
    if not converted:
        print("No jpg files to convert")

# Function to rename images
def rename_images(directory):
    images = os.listdir(directory)
    png_files = sorted([file for file in images if file.endswith('.png')])
    renamed = False
    for counter, file in enumerate(png_files, start=1):
        new_file_name = f"{counter}.png"
        new_file_path = os.path.join(directory, new_file_name)
        current_file_path = os.path.join(directory, file)
        if current_file_path != new_file_path:
            os.rename(current_file_path, new_file_path)
            print(f"{file} renamed to {new_file_name}")
            renamed = True
    if not renamed:
        print("No png files to rename")

# Main function
def main():
    directory = '.'  # current directory, can be changed to the desired one
    convert_jpg_to_png(directory)
    rename_images(directory)

if __name__ == "__main__":
    main()
