import PIL.Image

# opening the image
PATH = "image.jpeg"
img = PIL.Image.open(PATH)

# resize the image
WIDTH = 50
curr_width, curr_height = img.size
ratio = curr_height / curr_width
HEIGHT = int(WIDTH * ratio)
img = img.resize((WIDTH, HEIGHT))

# convert image to greyscale
img = img.convert("L")

# get the greyscale values of the data
img_data = list(img.getdata())

# convert it into values from 0 - 10
# we can do some simple math: 0 - 255 divided by 25 gives us 0 - 10 if rounded and we can use this
for i in range(len(img_data)):
    img_data[i] = img_data[i] // 25

# list of ascii values to be used in order of darkest to lightest approx.
ascii_values = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# converting the greyscale to ascii
final_img = ""
for i in range(len(img_data)):
    final_img += ascii_values[img_data[i]]
    if (i + 1) % WIDTH == 0:  # Add newline after WIDTH elements
        final_img += "\n"

# Alternatively, ensure the last line is correctly formatted (in case len(img_data) is not a multiple of WIDTH)
if len(img_data) % WIDTH != 0:
    final_img += "\n"

print(final_img)
