from pynput.mouse import Button,Controller
mouse=Controller()
mouse.position=(0,0)
for i in range(500):
	for j in range (500):
		mouse.move(1,0)
	mouse.position=(0,i+1)
		