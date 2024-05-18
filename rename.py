import os
from PIL import Image

images = os.listdir('.')

# Convert all jpg to png
for file in images:
    if file.endswith('.jpg'):
        img = Image.open(file)
        file_name = os.path.splitext(file)[0]
        img.save(file_name + '.png', 'PNG')
        print(f"{file} converted to {file_name}.png")
        os.remove(file)
        print(f"{file} was deleted")

# Numbering of images
counter = 1
for file in images:
    if file.endswith('.png'):
        new_file_name = f"{counter}.png"
        next = True
        
        for exist in images:
            if exist == new_file_name:
                next = False;

        if next: 
            os.rename(file, new_file_name)
            print(f"{file} renamed to {new_file_name}")
    
        counter += 1

if not next:
    print("Nothing to do")
