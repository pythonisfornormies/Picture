"""
picture.py
Author: Kai Darrow
Credit: Mr Dennison, Tutorial provided

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
"""
picture.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).
Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.
"""

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0x000000, 0)

# Define a line style that is a thin (1 pixel) wide black line
blackthinline = LineStyle(1, black)
blackthickline = LineStyle(3, black)
# A graphics asset that represents a rectangle
rectangle1 = RectangleAsset(50, 20, blackthinline, red)
circle1 = CircleAsset (10, blackthinline, green)
polygon1 = PolygonAsset(((50,50),(2,27),(67,24),(69,420)), blackthinline, blue)
circle2 = CircleAsset(69, blackthickline, black)
ellipse1 = EllipseAsset(69, 420, blackthickline, blue)
ellipse3 = EllipseAsset(50,20,blackthinline,red)
ellipse4 = EllipseAsset(50,20,blackthickline,green)
circle2 = CircleAsset(3,blackthinline,black)
# Now display a rectangle
Sprite(rectangle1, (500, 50))
Sprite(circle1, (500,500))
Sprite(circle2, (420, 420))
Sprite(ellipse1,(690,420))
Sprite(polygon1)
Sprite(polygon1,(20,420))
Sprite(ellipse3,(240,40))
Sprite(ellipse4,(240,350))
Sprite(circle2,(10,500))
Sprite(circle2,(50,500))


# add your code here /\  /\  /\


myapp = App()
myapp.run()
