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


#Test I2c

```
gej@rpi-zw3:~/Adafruit_Python_SSD1306 $ i2cdetect -y 1
Error: Could not open file `/dev/i2c-1' or `/dev/i2c/1': No such file or directory
gej@rpi-zw3:~/Adafruit_Python_SSD1306 $
```

Geen i2c, even aanzetten

```
gej@rpi-zw3:~/Adafruit_Python_SSD1306 $ sudo raspi-config nonint do_i2c 0

-zw3:~/Adafruit_Python_SSD1306 $ i2cdetect -y 1
Error: Could not open file `/dev/i2c-1': Permission denied
Run as root?
gej@rpi-zw3:~/Adafruit_Python_SSD1306 $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --                         
gej@rpi-zw3:~/Adafruit_Python_SSD1306 $
```

Gevonden, i2c aktief. Oled display op adres 3c.

# installeren

```
gej@rpi-zw3:~/Adafruit_Python_SSD1306 $ sudo python ez_setup.py
Downloading https://pypi.python.org/packages/source/s/setuptools/setuptools-3.5.1.zip
Extracting in /tmp/tmp7XdJBm
Now working in /tmp/tmp7XdJBm/setuptools-3.5.1
Installing Setuptools
running install
running bdist_egg
running egg_info
writing requirements to setuptools.egg-info/requires.txt
writing setuptools.egg-info/PKG-INFO
writing top-level names to setuptools.egg-info/top_level.txt
writing dependency_links to setuptools.egg-info/dependency_links.txt
writing entry points to setuptools.egg-info/entry_points.txt
reading manifest file 'setuptools.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
writing manifest file 'setuptools.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-armv6l/egg
running install_lib
running build_py
creating build
creating build/lib.linux-armv6l-2.7
copying pkg_resources.py -> build/lib.linux-armv6l-2.7
copying easy_install.py -> build/lib.linux-armv6l-2.7
creating build/lib.linux-armv6l-2.7/_markerlib
copying _markerlib/__init__.py -> build/lib.linux-armv6l-2.7/_markerlib
copying _markerlib/markers.py -> build/lib.linux-armv6l-2.7/_markerlib
creating build/lib.linux-armv6l-2.7/setuptools
copying setuptools/lib2to3_ex.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/svn_utils.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/compat.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/archive_util.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/sandbox.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/py26compat.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/site-patch.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/depends.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/__init__.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/extension.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/py31compat.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/py27compat.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/dist.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/ssl_support.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/version.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/script template.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/package_index.py -> build/lib.linux-armv6l-2.7/setuptools
copying setuptools/script template (dev).py -> build/lib.linux-armv6l-2.7/setuptools
creating build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/test_easy_install.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/test_build_ext.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/test_svn.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/test_sandbox.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/py26compat.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/test_bdist_egg.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/test_sdist.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/__init__.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/test_markerlib.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/server.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/test_egg_info.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/environment.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/test_upload_docs.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/test_develop.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/test_packageindex.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/test_resources.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/test_test.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/test_find_packages.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/script-with-bom.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/test_dist_info.py -> build/lib.linux-armv6l-2.7/setuptools/tests
copying setuptools/tests/doctest.py -> build/lib.linux-armv6l-2.7/setuptools/tests
creating build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/install.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/bdist_wininst.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/rotate.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/bdist_egg.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/__init__.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/alias.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/upload_docs.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/bdist_rpm.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/egg_info.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/saveopts.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/install_egg_info.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/sdist.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/develop.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/install_lib.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/test.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/install_scripts.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/easy_install.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/register.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/build_ext.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/setopt.py -> build/lib.linux-armv6l-2.7/setuptools/command
copying setuptools/command/build_py.py -> build/lib.linux-armv6l-2.7/setuptools/command
creating build/bdist.linux-armv6l
creating build/bdist.linux-armv6l/egg
creating build/bdist.linux-armv6l/egg/_markerlib
copying build/lib.linux-armv6l-2.7/_markerlib/__init__.py -> build/bdist.linux-armv6l/egg/_markerlib
copying build/lib.linux-armv6l-2.7/_markerlib/markers.py -> build/bdist.linux-armv6l/egg/_markerlib
copying build/lib.linux-armv6l-2.7/pkg_resources.py -> build/bdist.linux-armv6l/egg
copying build/lib.linux-armv6l-2.7/easy_install.py -> build/bdist.linux-armv6l/egg
creating build/bdist.linux-armv6l/egg/setuptools
copying build/lib.linux-armv6l-2.7/setuptools/lib2to3_ex.py -> build/bdist.linux-armv6l/egg/setuptools
copying build/lib.linux-armv6l-2.7/setuptools/svn_utils.py -> build/bdist.linux-armv6l/egg/setuptools
copying build/lib.linux-armv6l-2.7/setuptools/compat.py -> build/bdist.linux-armv6l/egg/setuptools
copying build/lib.linux-armv6l-2.7/setuptools/archive_util.py -> build/bdist.linux-armv6l/egg/setuptools
copying build/lib.linux-armv6l-2.7/setuptools/sandbox.py -> build/bdist.linux-armv6l/egg/setuptools
copying build/lib.linux-armv6l-2.7/setuptools/py26compat.py -> build/bdist.linux-armv6l/egg/setuptools
copying build/lib.linux-armv6l-2.7/setuptools/site-patch.py -> build/bdist.linux-armv6l/egg/setuptools
copying build/lib.linux-armv6l-2.7/setuptools/depends.py -> build/bdist.linux-armv6l/egg/setuptools
copying build/lib.linux-armv6l-2.7/setuptools/__init__.py -> build/bdist.linux-armv6l/egg/setuptools
copying build/lib.linux-armv6l-2.7/setuptools/extension.py -> build/bdist.linux-armv6l/egg/setuptools
copying build/lib.linux-armv6l-2.7/setuptools/py31compat.py -> build/bdist.linux-armv6l/egg/setuptools
copying build/lib.linux-armv6l-2.7/setuptools/py27compat.py -> build/bdist.linux-armv6l/egg/setuptools
copying build/lib.linux-armv6l-2.7/setuptools/dist.py -> build/bdist.linux-armv6l/egg/setuptools
copying build/lib.linux-armv6l-2.7/setuptools/ssl_support.py -> build/bdist.linux-armv6l/egg/setuptools
copying build/lib.linux-armv6l-2.7/setuptools/version.py -> build/bdist.linux-armv6l/egg/setuptools
creating build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/test_easy_install.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/test_build_ext.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/test_svn.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/test_sandbox.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/py26compat.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/test_bdist_egg.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/test_sdist.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/__init__.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/test_markerlib.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/server.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/test_egg_info.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/environment.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/test_upload_docs.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/test_develop.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/test_packageindex.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/test_resources.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/test_test.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/test_find_packages.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/script-with-bom.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/test_dist_info.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/tests/doctest.py -> build/bdist.linux-armv6l/egg/setuptools/tests
copying build/lib.linux-armv6l-2.7/setuptools/script template.py -> build/bdist.linux-armv6l/egg/setuptools
copying build/lib.linux-armv6l-2.7/setuptools/package_index.py -> build/bdist.linux-armv6l/egg/setuptools
creating build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/install.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/bdist_wininst.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/rotate.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/bdist_egg.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/__init__.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/alias.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/upload_docs.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/bdist_rpm.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/egg_info.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/saveopts.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/install_egg_info.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/sdist.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/develop.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/install_lib.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/test.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/install_scripts.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/easy_install.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/register.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/build_ext.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/setopt.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/command/build_py.py -> build/bdist.linux-armv6l/egg/setuptools/command
copying build/lib.linux-armv6l-2.7/setuptools/script template (dev).py -> build/bdist.linux-armv6l/egg/setuptools
byte-compiling build/bdist.linux-armv6l/egg/_markerlib/__init__.py to __init__.pyc
byte-compiling build/bdist.linux-armv6l/egg/_markerlib/markers.py to markers.pyc
byte-compiling build/bdist.linux-armv6l/egg/pkg_resources.py to pkg_resources.pyc
byte-compiling build/bdist.linux-armv6l/egg/easy_install.py to easy_install.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/lib2to3_ex.py to lib2to3_ex.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/svn_utils.py to svn_utils.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/compat.py to compat.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/archive_util.py to archive_util.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/sandbox.py to sandbox.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/py26compat.py to py26compat.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/site-patch.py to site-patch.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/depends.py to depends.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/__init__.py to __init__.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/extension.py to extension.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/py31compat.py to py31compat.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/py27compat.py to py27compat.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/dist.py to dist.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/ssl_support.py to ssl_support.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/version.py to version.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/test_easy_install.py to test_easy_install.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/test_build_ext.py to test_build_ext.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/test_svn.py to test_svn.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/test_sandbox.py to test_sandbox.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/py26compat.py to py26compat.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/test_bdist_egg.py to test_bdist_egg.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/test_sdist.py to test_sdist.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/__init__.py to __init__.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/test_markerlib.py to test_markerlib.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/server.py to server.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/test_egg_info.py to test_egg_info.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/environment.py to environment.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/test_upload_docs.py to test_upload_docs.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/test_develop.py to test_develop.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/test_packageindex.py to test_packageindex.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/test_resources.py to test_resources.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/test_test.py to test_test.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/test_find_packages.py to test_find_packages.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/script-with-bom.py to script-with-bom.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/test_dist_info.py to test_dist_info.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/tests/doctest.py to doctest.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/script template.py to script template.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/package_index.py to package_index.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/install.py to install.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/bdist_wininst.py to bdist_wininst.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/rotate.py to rotate.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/bdist_egg.py to bdist_egg.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/__init__.py to __init__.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/alias.py to alias.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/upload_docs.py to upload_docs.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/bdist_rpm.py to bdist_rpm.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/egg_info.py to egg_info.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/saveopts.py to saveopts.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/install_egg_info.py to install_egg_info.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/sdist.py to sdist.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/develop.py to develop.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/install_lib.py to install_lib.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/test.py to test.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/install_scripts.py to install_scripts.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/easy_install.py to easy_install.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/register.py to register.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/build_ext.py to build_ext.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/setopt.py to setopt.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/command/build_py.py to build_py.pyc
byte-compiling build/bdist.linux-armv6l/egg/setuptools/script template (dev).py to script template (dev).pyc
creating build/bdist.linux-armv6l/egg/EGG-INFO
copying setuptools.egg-info/PKG-INFO -> build/bdist.linux-armv6l/egg/EGG-INFO
copying setuptools.egg-info/SOURCES.txt -> build/bdist.linux-armv6l/egg/EGG-INFO
copying setuptools.egg-info/dependency_links.txt -> build/bdist.linux-armv6l/egg/EGG-INFO
copying setuptools.egg-info/entry_points.txt -> build/bdist.linux-armv6l/egg/EGG-INFO
copying setuptools.egg-info/requires.txt -> build/bdist.linux-armv6l/egg/EGG-INFO
copying setuptools.egg-info/top_level.txt -> build/bdist.linux-armv6l/egg/EGG-INFO
copying setuptools.egg-info/zip-safe -> build/bdist.linux-armv6l/egg/EGG-INFO
creating dist
creating 'dist/setuptools-3.5.1-py2.7.egg' and adding 'build/bdist.linux-armv6l/egg' to it
removing 'build/bdist.linux-armv6l/egg' (and everything under it)
Processing setuptools-3.5.1-py2.7.egg
Copying setuptools-3.5.1-py2.7.egg to /usr/local/lib/python2.7/dist-packages
Adding setuptools 3.5.1 to easy-install.pth file
Installing easy_install script to /usr/local/bin
Installing easy_install-2.7 script to /usr/local/bin

Installed /usr/local/lib/python2.7/dist-packages/setuptools-3.5.1-py2.7.egg
Processing dependencies for setuptools==3.5.1
Finished processing dependencies for setuptools==3.5.1
gej@rpi-zw3:~/Adafruit_Python_SSD1306 $ 
```

# Eerste test

```
gej@rpi-zw3:~/Adafruit_Python_SSD1306/examples $ sudo python animate.py 
Traceback (most recent call last):
  File "animate.py", line 24, in <module>
    import Adafruit_GPIO.SPI as SPI
ImportError: No module named Adafruit_GPIO.SPI
gej@rpi-zw3:~/Adafruit_Python_SSD1306/examples $
```

Ah, nog iets vergeten...

```
gej@rpi-zw3:~/Adafruit_Python_SSD1306 $ sudo python setup.py install
running install
running bdist_egg
running egg_info
writing requirements to Adafruit_SSD1306.egg-info/requires.txt
writing Adafruit_SSD1306.egg-info/PKG-INFO
writing top-level names to Adafruit_SSD1306.egg-info/top_level.txt
writing dependency_links to Adafruit_SSD1306.egg-info/dependency_links.txt
reading manifest file 'Adafruit_SSD1306.egg-info/SOURCES.txt'
writing manifest file 'Adafruit_SSD1306.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-armv6l/egg
running install_lib
running build_py
creating build/bdist.linux-armv6l
creating build/bdist.linux-armv6l/egg
creating build/bdist.linux-armv6l/egg/Adafruit_SSD1306
copying build/lib.linux-armv6l-2.7/Adafruit_SSD1306/__init__.py -> build/bdist.linux-armv6l/egg/Adafruit_SSD1306
copying build/lib.linux-armv6l-2.7/Adafruit_SSD1306/SSD1306.py -> build/bdist.linux-armv6l/egg/Adafruit_SSD1306
byte-compiling build/bdist.linux-armv6l/egg/Adafruit_SSD1306/__init__.py to __init__.pyc
byte-compiling build/bdist.linux-armv6l/egg/Adafruit_SSD1306/SSD1306.py to SSD1306.pyc
creating build/bdist.linux-armv6l/egg/EGG-INFO
copying Adafruit_SSD1306.egg-info/PKG-INFO -> build/bdist.linux-armv6l/egg/EGG-INFO
copying Adafruit_SSD1306.egg-info/SOURCES.txt -> build/bdist.linux-armv6l/egg/EGG-INFO
copying Adafruit_SSD1306.egg-info/dependency_links.txt -> build/bdist.linux-armv6l/egg/EGG-INFO
copying Adafruit_SSD1306.egg-info/requires.txt -> build/bdist.linux-armv6l/egg/EGG-INFO
copying Adafruit_SSD1306.egg-info/top_level.txt -> build/bdist.linux-armv6l/egg/EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating 'dist/Adafruit_SSD1306-1.6.1-py2.7.egg' and adding 'build/bdist.linux-armv6l/egg' to it
removing 'build/bdist.linux-armv6l/egg' (and everything under it)
Processing Adafruit_SSD1306-1.6.1-py2.7.egg
Copying Adafruit_SSD1306-1.6.1-py2.7.egg to /usr/local/lib/python2.7/dist-packages
Adding Adafruit-SSD1306 1.6.1 to easy-install.pth file

Installed /usr/local/lib/python2.7/dist-packages/Adafruit_SSD1306-1.6.1-py2.7.egg
Processing dependencies for Adafruit-SSD1306==1.6.1
Searching for Adafruit-GPIO>=0.6.5
Best match: Adafruit-GPIO 0.6.5
Downloading https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.6.5
Processing master
Writing /tmp/easy_install-a5FjZ1/adafruit-Adafruit_Python_GPIO-22a1ff4/setup.cfg
Running adafruit-Adafruit_Python_GPIO-22a1ff4/setup.py -q bdist_egg --dist-dir /tmp/easy_install-a5FjZ1/adafruit-Adafruit_Python_GPIO-22a1ff4/egg-dist-tmp-JFomQG
zip_safe flag not set; analyzing archive contents...
Adding Adafruit-GPIO 1.0.3 to easy-install.pth file

Installed /usr/local/lib/python2.7/dist-packages/Adafruit_GPIO-1.0.3-py2.7.egg
Searching for adafruit-pureio
Reading https://pypi.python.org/simple/adafruit-pureio/
Best match: Adafruit-PureIO 0.2.1
Downloading https://pypi.python.org/packages/55/fa/99b1006fb4bb356762357b297d8db6ec9ffa13af480692ab72aa4a0dd0c4/Adafruit_PureIO-0.2.1.tar.gz#md5=5b3276059eb55d6c37429a8413a92029
Processing Adafruit_PureIO-0.2.1.tar.gz
Writing /tmp/easy_install-nEJy4w/Adafruit_PureIO-0.2.1/setup.cfg
Running Adafruit_PureIO-0.2.1/setup.py -q bdist_egg --dist-dir /tmp/easy_install-nEJy4w/Adafruit_PureIO-0.2.1/egg-dist-tmp-xqp_ez
zip_safe flag not set; analyzing archive contents...
Adding Adafruit-PureIO 0.2.1 to easy-install.pth file

Installed /usr/local/lib/python2.7/dist-packages/Adafruit_PureIO-0.2.1-py2.7.egg
Searching for spidev==3.0
Best match: spidev 3.0
Adding spidev 3.0 to easy-install.pth file

Using /usr/lib/python2.7/dist-packages
Finished processing dependencies for Adafruit-SSD1306==1.6.1
gej@rpi-zw3:~/Adafruit_Python_SSD1306 $ 
```


