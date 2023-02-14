from PIL import Image
import os

output = ""
photos_folder = os.listdir("./Resized_Photos/2023")
counter = 0
for file in photos_folder:
    output += (
        '<div class="grid-item"><img src="Resized_Photos/2023/'
        + file
        + '" alt="'
        + str(counter)
        + '"></div>\n'
    )
    counter += 1

print(output)

with open("to_paste_2023.txt", "w") as f:
    f.write(output)
