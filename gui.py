#! python3
# mouseNow.py - Displays the mouse cursor's current position.
import pyautogui
print('Press Ctrl-C to quit.')
i=0
j=0
try:
	while True:

		# TODO: Get and print the mouse coordinates.
		x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
		
        #print('\b' * len(positionStr), end='', flush=True)
        print(positionStr)
        pyautogui.moveRel(1, 0, duration=0.25)
		#pyautogui.moveTo(100, 100, duration=0.25)
except KeyboardInterrupt:
	print('\nDone.')