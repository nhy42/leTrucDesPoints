from PIL import Image, ImageDraw


# MADE BY PAUL ZANOLIN
# This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.



# =============  CONFIG  =============
lines = ["0607b", "0616b", "1424b", "0203b", "0010b", "3040o", "3637o", "3443o", "6070r", "6777r", "7677r", "5556r"]
# pour faire les connections, changer le background

data = ["01000100b", "01100101b", "01110011b", "01110000o", "01101111o", "01101001r", "01101110r", "01110100r"]

drawLines = True
testMode = False

# =============  END     =============

# for test purpose
if testMode:
    im = Image.open("baseTest.png")
else:
    im = Image.open("base.png")

im = im.transpose(Image.FLIP_TOP_BOTTOM)
im = im.rotate(-90)

d = ImageDraw.Draw(im)

color = (51, 181, 221)  # classic blue
borderL = 33

for i in range(8):
    if data[i][8] == "r":
        color = (244, 76, 61)  # red
    elif data[i][8] == "b":
        color = (51, 181, 221)  # classic blue
    elif data[i][8] == "o":
        color = (221, 140, 0)  # orange
    for j in range(8):
        if data[i][j] == "0":

            # full the circle
            for f in range(25):
                cornerTLeft = (200 + 200 * i + borderL + f * 8, 200 + 200 * j + borderL + f * 8)
                # topLeft (border + espacement * numcolone + borderL+ un peu plus pour remplir le cercle)
                cornerBRight = (400 + 200 * i - borderL - f * 8, 400 + 200 * j - borderL - f * 8)
                # bottomRight
                d.arc([cornerTLeft, cornerBRight], 0, 360, color, 10)

if drawLines:
    for line in lines:
        if line[4] == "r":
            color = (244, 76, 61)  # red
        elif line[4] == "b":
            color = (51, 181, 221)  # classic blue
        elif line[4] == "o":
            color = (221, 140, 0)  # orange
        d.line([(300 + int(line[0]) * 200, 300 + int(line[1]) * 200),
                (300 + int(line[2]) * 200, 300 + int(line[3]) * 200)], color, 200 - 2 * borderL)

im = im.rotate(90)
im = im.transpose(Image.FLIP_TOP_BOTTOM)
#im.show()
im.save("end.png")
