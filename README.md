# text-bitmaps
Python module to produce bitmap images containing text for use with small, low-resolution displays such as Papirus e-paper liquid-crystal displays.

Below is an example of a 200 x 96 pixel, black-and-white image produced with this module, as it would appear on the Papirus display (this is an LCD display so color 1 is black and zero is white).

<IMG SRC="eapoe.bmp">

The font is based on the Mullard SAA5050 chip (dated July 1982) that was used to display text-based information on TV screens. Many thanks to [bjh21](http://bjh21.me.uk/bedstead/) for providing the raw data for the original fonts as well as a large collection of additional unicode characters.

The following bitmaps are included here:

ASCII
- fixed
- proportional

Unicode - Basic Latin (ASCII) and Latin-1 Supplement
- fixed
- proportional

The proportional set allow more characters per line because certain characters ('i', 'j', etc) have been trimmed.
