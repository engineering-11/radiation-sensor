# radiation-sensor
This repository contains a script for using the radiation detection module.

1. Obtain a fully soldered radiation detector and a 5-wire female to female connector.
2. If you are working with a smaller pi hat, connect each of the five wires in the following pairs: "NS" to "N", "GND" to "-", "SIG" to "S", "GND" to "-", and "+V" to "+"
3. Check that all wires are connected in parralel and with no crossovers.
4. If you are working with a larger pi hat, plug the 5 pins on the radiation detector into the 5 sockets on the board next to the two resistors with the arrow next to it. Make sure the sensor is hanging over the board itself in the direction of the arrow is pointing in.
5. Once the required prgram has been pulled from github, run the command: cd radiation-sensor
6. Run the program by typing: python3 radiationcode.py 
7. Once run, the unit will collect counts over a period of 1000s, then end. The time stamps for the counts will be printed the the screen and saved to one file.
