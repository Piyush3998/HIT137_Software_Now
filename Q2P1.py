from PIL import Image
import time

# Step 1: Generate the number (n)
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
print ("generated number=", generated_number)

# Step 2: Open the image
image = Image.open('/Users/moomtahinarahman/Downloads/Assignment 2/Chapter1.jpg')
pixels = image.load()

# Step 3: Modify the pixels
width, height = image.size
new_image = Image.new('RGB', (width, height))
red_sum = 0

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        new_r = min(r + generated_number, 255)
        new_g = min(g + generated_number, 255)
        new_b = min(b + generated_number, 255)

        new_image.putpixel((x, y), (new_r, new_g, new_b))
        red_sum += new_r

# Step 4: Save the modified image
new_image.save('/Users/moomtahinarahman/Downloads/Assignment 2/chapter1out.jpg')

# Step 5: Output the sum of red values
print("Sum of red values in the new image:", red_sum)
