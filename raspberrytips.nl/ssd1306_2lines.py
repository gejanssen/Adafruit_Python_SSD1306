import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import sys

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# verwerken van argumenten
line1=(sys.argv[1])
line2=(sys.argv[2])

disp = Adafruit_SSD1306.SSD1306_128_32(rst=24)

disp.begin()
disp.clear()
disp.display()

image = Image.new('1', (disp.width, disp.height))

draw = ImageDraw.Draw(image)
#draw.rectangle((0,0,disp.width-1,disp.height-1), outline=1, fill=0)

#font = ImageFont.load_default()
font = ImageFont.truetype('FreeSerif.ttf', 12)
draw.text((1, 0),line1,  font=font, fill=255)
draw.text((1, 17),line2,  font=font, fill=255)

#x=1
#for x in sys.argv:
#     Only for debug
#     print "Argument: ", x

disp.image(image)
disp.display()
