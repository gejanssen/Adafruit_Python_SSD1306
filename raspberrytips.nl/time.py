import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

disp = Adafruit_SSD1306.SSD1306_128_32(rst=24)
tijd = time.strftime("%H:%M:%S")


disp.begin()
disp.clear()
disp.display()

image = Image.new('1', (disp.width, disp.height))

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('FreeSerif.ttf', 25)
# first 5 lines are yellow
draw.text((1, 5),tijd ,  font=font, fill=255)

disp.image(image)
disp.display()
