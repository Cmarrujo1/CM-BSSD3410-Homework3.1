# File handling in Python:
# Source: https://www.geeksforgeeks.org/file-handling-python/
# Author: none

# List slicing in Python:
# Source: https://www.geeksforgeeks.org/python-list-slicing/
# Author: none

# Handling user input in Python:
# Source: https://www.geeksforgeeks.org/taking-input-in-python/
# Working with arrays using NumPy: https://www.geeksforgeeks.org/python-numpy-array-slicing/
# Author: none

# Image processing using Python's PIL:
# Source: https://www.geeksforgeeks.org/python-pillow-library-introduction/
# Author: none

from PIL import Image, ImageDraw
import colorsys
import matplotlib.pyplot as plt
import numpy as np

highlighted_image = Image.open('monkey.jpg')

plt.imshow(highlighted_image)
plt.title('Highlighted Image Preview')
plt.show()

def compare_pixles(pix1, pix2):
    return pix1[0][0] > pix2[0][0]

def storePixles(im):
    width = int(im.size[0])
    height = int(im.size[1])

    pixel_array = []
    yiq_pixels = []

    for i in range(width):
        for j in range(height):
            r, g, b = im.getpixel((i, j))
            yiq = colorsys.rgb_to_yiq(r/255, g/255, b/255)
            yiq_pixels.append([yiq, (i, j)])
            pixel_array.append([(r, g, b), (i, j)])

        return pixel_array, yiq_pixels

        def pixles_to_image(im, pixels):
            outimg = Image.new("RGB", im.size)

            if isinstance(pixels[0][0][0], float):
                print('YIQ')
                yiq_out = []
                for p in pixels:
                    r, g, b = colorsys.yiq_to_rgb(p[0][0], p[0][1], p[0][2])
                    r, g, b = int(r * 255), int(g * 255), int(b * 255)
                    yiq_out.append((r, g, b))
                outimg.putdata(yiq_out)
            else:
                outimg.putdata([p[0] for p in pixels])

            outimg.show()
            return outimg

        def pixles_to_points(im, pixels):
            for p in pixels:
                if isinstance(p[0][0], float):
                    im.putpixel(p[1], tuple(int(v * 255) for v in colorsys.yiq_to_rgb(p[0][0], p[0][1], p[0][2])))
                else:
                    im.putpixel(p[1], p[0])

            im.show()

        def grayscale(im, pixels):
            draw = ImageDraw.Draw(im)
            for px in pixels:
                gray_av = int((px[0][0] + px[0][1] + px[0][2]) / 3)
                draw.point(px[1], (gray_av, gray_av, gray_av))

        subi = np.array([0, 1, 2])

        while True:
            user_input = input(
                "Enter Q to save, R to reverse slicing, T to adjust tolerance, or C to change target color: ").strip().upper()

            if user_input == 'Q':
                highlighted_image.save('monkey.png')
                print("Image saved as 'monkey.png'.")
                break

            elif user_input == 'R':
                subi = subi[::-1]
                print("Slicing logic reversed.")

            elif user_input == 'T':
                tolerance_adjustment = int(input("Enter tolerance adjustment (positive or negative integer): "))
                subi += tolerance_adjustment
                print(f"Tolerance adjusted by {tolerance_adjustment}.")

            elif user_input == 'C':
                r = int(input("Enter Red value (0-255): "))
                g = int(input("Enter Green value (0-255): "))
                b = int(input("Enter Blue value (0-255): "))
                target_color = np.array([r, g, b])
                print(f"Target color changed to RGB({r}, {g}, {b}).")

            else:
                print("Invalid input. Please try again.")





