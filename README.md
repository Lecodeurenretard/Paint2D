# Paint2D
## Purpose
This is an NSI (highschool CS in France) project where we have to use Python and Pygame to make a program.
I chose to make paint because it was the first project I made back when I learnt the canvas API for JS.

## Usage
Here is a screenshot of the software:  
![screenshot](img/doc-screenshot-edited.png)

1. The save icon: saves your drawing to the `my_drawing.png` file.
2. The sizing buttons: increases or decrease the size of the brush.
3. The brush preview: a preview of the brush's the current foreground and background color.
4. The eraser button: toggles the eraser, the eraser color is always white.
5. The reset button: resets the canvas to plain white.
6. The fill button: fills the canvas with the background color.
7. The color buttons: modifie the color of the brush.
8. The canvas: where you can draw.

Left click to draw with foreground color and right click to draw with background color. 

You can load an existing image by running the application in the command line with the name of the image for argument.  
Example:
```bash
python3 main.py my-image.png
```
