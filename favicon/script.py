import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from matplotlib.pyplot import imshow

image = Image.new("RGBA", (500,500), (0,0,0))
draw = ImageDraw.Draw(image)

fontsize = 250
offsetX = 60
offsetY = 60
font = ImageFont.truetype("roboto/Roboto-Bold.ttf", fontsize)
draw.text((offsetX+0,  offsetY),"A",(255,255,255),font=font)
draw.text((offsetX+107,offsetY),"R",(255,255,255),font=font)
draw.text((offsetX+233,offsetY),"C",(255,255,255),font=font)

#draw.arc((0,100,300,200), 0, 270, fill=(0,0,0,255))

image.save("image.png", "PNG")
