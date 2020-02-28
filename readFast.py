import pygame, time
from pynput import keyboard
pygame.init()	
x,y = 500,500
WPM = 200
delay = 1/(WPM/60)
spacePress = False

def pressed(key):
	global spacePress
	if str(key) == 'Key.space':
		if spacePress == True:
			spacePress = False
		else:
			spacePress = True

def rotate(Givenlist, shift):
	return Givenlist[shift:] + Givenlist[:shift]

display_surface = pygame.display.set_mode((x, y))
pygame.display.set_caption('Read Lines') 
font = pygame.font.Font('freesansbold.ttf', 50) 
book = open("BraveNewWorld.txt","r",encoding="utf8") 
bookLines = book.readlines()
running = True
wordRemain = ['1','2','3','4','5']
yValues = [400,300,200,100]	

listener = keyboard.Listener(on_press=pressed)
listener.start()
for line in bookLines:
	stringSplit = line.split()
	for i in range(len(stringSplit)):
		if spacePress == False:
			wordRemain = rotate(wordRemain,-1)
			wordRemain[0] = stringSplit[i]
			display_surface.fill((255,255,255)) 
			for g in range(len(yValues)):
				text = font.render(wordRemain[g-1], True, (0,0,0), (255,255,255))
				textRect = text.get_rect() 
				textRect.center = (x/2,yValues[g-1])
				display_surface.blit(text, textRect) 
			pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		if running == False:
			break	
		time.sleep(delay)
	if running == False:
		break
book.close()
