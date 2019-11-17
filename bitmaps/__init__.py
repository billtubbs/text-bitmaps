#!/usr/bin/env python
"""
Python module to produce bitmap images containing text
for use with small, low-resolution black-and-white displays
such as Papirus e-paper liquid-crystal displays.
"""

import os
from PIL import Image, ImageDraw

import pkg_resources

# For python 2 compatibility:
try:
    FileNotFoundError = IOError
except:
    pass

display_size = (200, 96)  # Pixel dimensions of Papirus Zero display
format_string = "chr_0x{:04x}{}.bmp"


def get_char_image(c, char_set='ascii', spacing='fixed',
                   sub_label='', fill='chr_np',
                   img_dir='SAA5050'):
    """Returns bitmap image of character c.

    Args:
        c (str or int): Single character (e.g. 'a'), or character code.
        char_set (str): Character set to use ('unicode' or 'ascii').
        sub_label (str): '' or '_s2' for double-size bitmaps.
        fill (str): Filename of char to use when character not
            recognized (or file error).
    """

    if isinstance(c, str):
        c = ord(c)

    # Now that this is a package, to get the path to the
    # bitmap image files we do this:
    path_in_package = os.path.join(img_dir, char_set, spacing)
    filepath = pkg_resources.resource_filename(__name__, path_in_package)

    filename = format_string.format(c, sub_label)
    try:
        im = Image.open(os.path.join(filepath, filename))
    except IOError:
        filename = "{}{}.bmp".format(fill, sub_label)
        im = Image.open(os.path.join(filepath, filename))

    return im


char_height = get_char_image(32).size[1]


def display_text_prop(text, display_size=display_size,
                      char_set='unicode',
                      x_borders=(1, 1), y_borders=(1, 1),
                      spacing='prop', char_size=1,
                      fill='chr_np', tab_setting=4):
    """Create image from text.

    Args:
        text (str): Text to display in image.
        display_size (tuple): Size of image to create.
        char_set (str): Character set to use ('unicode' or 'ascii').
        x_borders (tuple): Size of left and write borders (pixels).
        y_borders (tuple): Size of top and bottom borders (pixels).
        spacing (str): Fixed or propoertional char spacing ('fixed'
            or 'prop').
        fill (str): Filename of char to use when character not
            recognized (or file error).

    Returns:
        display (PIL.Image): Image object.
        char_count (int): Number of characters that were displayed.
            This depends on the size of the image and the character
            spacing.
    """

    if char_size > 1:
        sub_label = '_s{:d}'.format(char_size)
    else:
        sub_label = ''

    # Binary image
    display = Image.new('1', display_size, color=0)

    x, y = (x_borders[0], y_borders[0])

    # Handle tabs
    if chr(9) in text:
        text = text.replace(chr(9), ' '*tab_setting)

    # Newlines are handled
    for char_count, c in enumerate(text):
        if c == chr(10):
            # Start newline
            x, y = (x_borders[0], y + char_height * char_size)
            if y + char_height * char_size > display_size[1]:
                break
        else:
            im = get_char_image(c, char_set=char_set, spacing=spacing,
                                sub_label=sub_label, fill=fill)
            if x + im.size[0] > display_size[0]:
                x, y = (x_borders[0], y + char_height * char_size)
                if y + char_height * char_size > display_size[1]:
                    break
                if c == " ":
                    continue
            display.paste(im, (x, y))
            x += im.size[0]

    # TODO: Also need to handle chrs 11, 12, and 13

    return display, char_count + 1
