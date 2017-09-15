Adafruit Python SSD1306
=======================

Python library to use SSD1306-based 128x64 or 128x32 pixel OLED displays with a Raspberry Pi or Beaglebone Black.

Designed specifically to work with the Adafruit SSD1306-based OLED displays ----> https://www.adafruit.com/categories/98

Adafruit invests time and resources providing this open source code, please support Adafruit and open-source hardware by purchasing products from Adafruit!

Written by Tony DiCola for Adafruit Industries.
MIT license, all text above must be included in any redistribution


```
rpi-zw2:~ $ git clone https://github.com/adafruit/Adafruit_Python_SSD1306
Cloning into 'Adafruit_Python_SSD1306'...
remote: Counting objects: 112, done.
remote: Total 112 (delta 0), reused 0 (delta 0), pack-reused 112
Receiving objects: 100% (112/112), 34.60 KiB | 0 bytes/s, done.
Resolving deltas: 100% (57/57), done.
gej@rpi-zw2:~ $ 
```
Enable i2c

```
gej@rpi-zw2:~/Adafruit_Python_SSD1306 $ sudo raspi-config

Interface,
I2C,
Select
Would you like the ARM I2C interface to be enabled?
Yes
