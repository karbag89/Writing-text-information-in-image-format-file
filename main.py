import os
import glob
import textwrap

from PIL import Image, ImageFont, ImageDraw


# ----------------------------------------------------------------------------
# Description :
# The function executes the full file path operation and returns the result 
# of 'file_fullname' and 'author_fullname' values
#
# Parameters :
#     file        Full name of currect image file
#
# Return :
#     file_fulname and author_fulname values
# ----------------------------------------------------------------------------
def get_author_fullname(file):
    """Getting image author name and surname."""
    v_fullename = str(os.path.basename(file))
    v_filename = v_fullename[:v_fullename.find('.')]
    v_author = v_filename.split('-')

    name = v_author[0].capitalize()
    surname = v_author[1].capitalize()
    author_fullname = '©' + name + ' ' + surname

    return v_fullename, author_fullname


# ----------------------------------------------------------------------------
# Description :
# The function drawing the author_fullname information on the image file.
#
# Parameters :
#     file        Full name of currect image file
#     info        Author full name for image text information
#
# Return :
#     None
# ----------------------------------------------------------------------------
def image_operation(file, info):
    img = Image.open(file)
    draw = ImageDraw.Draw(img)

    w, h = img.size
    font_size = 40
    x_pos = (w - (len(info)*font_size*0.58))
    y_pos = h - (font_size+font_size*0.5)

    # Setting the image text font
    font = ImageFont.truetype("arial.ttf", font_size)

    # Drawing the "author_fullname" information on the image file
    draw.text((x_pos, y_pos), get_author_fullname(file)[1], (255, 255, 255), \
               font=font)

    # Saving new image fime on defult '\output-images' directory
    img.save(final_directory + '\\' + get_author_fullname(file)[0], "JPEG")

    return None


# Getting current directory
current_directory = os.getcwd()
final_directory = current_directory + '\output-images'
# Checking the folder exist or not
if not os.path.exists(final_directory):
    os.makedirs(final_directory)


# Getting the image directory path
img_dir = current_directory + '\source-images'
data_path = os.path.join(img_dir, '*g')
# Reading files using glob library
files = glob.glob(data_path)
for file in files:
    info = get_author_fullname(file)[1]

    image_operation(file, info)
