this will be the tutorial !

if you dont have a habit of reading : you can see the youtube video :-
video

just try this, experiment and share any new ideas.


-first install thonny
-now install the micropython firmware on pico
(i am not going to give a tutorial for the above you can use youtube)
-using thonny put main.py in raspberry pi pico storage. (without renaiming it)
-now find the port your pico is connected to like COM5 or something, you have to find it and change the line in the readings and controller.py
-also you need python, python packages vgamepad, pyserial.
-when you try to install vgamepad you will see a pop up installer on windows , install it (these are the drivers required for virtual gamepad)
-now set up the mpu6050 wiring :-
 1. you can wire using any correct pins on pico using pinout diagrams just keep in mind you would have to cange the pins in main.py.
 2. if you dont want to change main.py:-
     -just connect vcc to any 3v3 out.
     -connect GND to any ground pin.
     -SCL to GPIO pin 27
     -SDA to GPIO pin 26
-now save the files till here and disconnect pi pico and reconnect the main.py should run automatically
-make sure no other apps are accessing the pi pico serial console not even thonny.
-now run readings and controller.py.
-this will automatically create a new virtual gamepad if you have done everything correctly.
-if you move the y axis of the mpu6050 the left joystick will move.
