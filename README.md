# radiation-sensor
This repository contains a script for using the radiation detection module.

1. Obtain a fully soldered radiation detector and a 5-wire female to female connector.
2. Connect each of the five wires in the following pairs: "NS" to "N", "GND" to "-", "SIG" to "S", "GND" to "-", and "+V" to "+"
3. Check that all wires are connected in parralel and with no corssovers.
4. Once the required prgram has been pulled from github, run the command: cd radiation-sensor
5. Run the program by typing: python3 radiationcode.py 
6. Once run, the unit will collect counts over a period of 1000s, then end. The time stamps for the counts will be printed the the screen and saved to one file.
