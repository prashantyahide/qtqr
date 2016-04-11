# IMPORTANT NOTICE #

This project now is part of a bigger one (python-qr-tools) and has moved to the launchpad platform:

> Sourcecode: https://code.launchpad.net/~qr-tools-developers/qr-tools/trunk

> Downloads: https://launchpad.net/qr-tools/+download

> Stable PPA: https://launchpad.net/~qr-tools-developers/+archive/qr-tools-stable

> Dilay PPA: https://launchpad.net/~qr-tools-developers/+archive/daily/

**I'll keep updating the googlecode project in addition to the Launchpad one for a while, but eventually I'll stop and carry on with Launchpad only. No more updates are coming to googlecode. Please use the launchpad page instead. Thank you!**

> IF YOU FIND THIS SOFTWARE USEFULL, PLEASE SEND ME SOME [FEEDBACK](mailto:algozino@gmail.com)! I'LL APPRECIATE IT! :D

# QtQR 1.0 released! #
Today I'm releasing the 1.0 version of this software, I think it has the basic functionality working OK. Please try it and fill an issue if you find a bug or there is a feature you would like to see implemented.

## News ##
_May 6th, 2011: Fixed Bug when opening QtQR from gnome menu (or redirecting the output to a file) and decoding non-ascii text. There's no download yet available. Please clone the repo._

_April 26, 2011: QtQR 1.0: Fixed bug with non-ascii characters. Now you can encode and decode QR Codes with non-ascii chars. Fixed typo bug in opening urls, mailto's, etc. I recommend you to update to the latest version_

_April 21, 2011: Bug Fixes: Show message when there's no symbol to decode in file instead of an Exception._

_April 16, 2011: Minor Bug Fixes: Chenged Yes | No Decode Message buttons for Ok button when there's no action to do._

_April 14, 2011: New package to download with the changes. Better decoding, now it shows the data type, the content and prompt for a default action, i.e., open url, send e-mail, etc._

_April 12, 2011: Imported new changes from Launchpad. Now you can encode diferent data types (text, urls, sms, etc.)._

_April 4, 2011: I've imported the latest version from Launchpad. You can download it from the Downloads section or folowing the link in the side bar (qtqr-latest.tar.lzma)._

## Instructions ##

  * Make sure you have installed all the dependencies: `qrencode` and `python-zbar`.

  * Decompress _qtqr-latest.tar.lzma_ to a directory, for example `/home/me/qtqr`.
  * Open a terminal and `cd` to the dir you decompressed the file: `cd /home/me/qtqr`
  * run: `python qtqr.py`
  * ???
  * profit!

> Here you can see a list of the KeyboardShortcuts.

## Introduction ##

QtQR is a GUI front-end for linux's qrencode made in Python & Qt, based on the work of David Green: https://launchpad.net/qr-code-creator/ and inspired by http://www.omgubuntu.co.uk/2011/03/how-to-create-qr-codes-in-ubuntu/

This is FREE SOFTWARE: GNU GPLv3
copyright (C) 2011 Ramiro Algozino

UNDER DEVELOPMENT! USE AT YOUR OWN RISK!

## Dependencies ##

  * zbar for decoding
  * PIL for decoding
  * PyQt4
  * Python 2.6

## Screenshot ##

![http://qtqr.googlecode.com/hg/screenshot.png](http://qtqr.googlecode.com/hg/screenshot.png)

## Screencast ##

See QtQR in action:

<a href='http://www.youtube.com/watch?feature=player_embedded&v=wyGKPh1cBbk' target='_blank'><img src='http://img.youtube.com/vi/wyGKPh1cBbk/0.jpg' width='425' height=344 /></a>

Watch on YouTube: http://www.youtube.com/watch?v=wyGKPh1cBbk

**NOTE:** (The screencast is not from the latest version)