cd /home/gej/Adafruit_Python_SSD1306/raspberrytips.nl
/usr/bin/python /home/gej/Adafruit_Python_SSD1306/raspberrytips.nl/booting.py
/bin/sleep 10
/usr/bin/python /home/gej/Adafruit_Python_SSD1306/raspberrytips.nl/hallojos.py
sleep 60
/usr/bin/python /home/gej/Adafruit_Python_SSD1306/raspberrytips.nl/time.py
sleep 60
#/usr/bin/watch -n 15 /usr/bin/python /home/gej/Adafruit_Python_SSD1306/raspberrytips.nl/time.py
while :
do
	/usr/bin/python /home/gej/Adafruit_Python_SSD1306/raspberrytips.nl/time.py
	/bin/sleep 15
done
