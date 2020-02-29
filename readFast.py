import pygame, time
from pynput import keyboard
pygame.init()
x,y = 500,500

def pressed(key):
	print('pressed')
	if str(key) == 'Key.space':
		if spacePress == True:
			spacePress = False
			return spacePress 
		else: 
			spacePress = True
			return spacePress

def rotate(Givenlist, shift):
		return Givenlist[shift:] + Givenlist[:shift]

class readText:
	def __init__(self,textFile,WPM,fontSize=None):
		self.fontSize = fontSize or 50
		self.textFile = textFile
		self.WPM = WPM
		self.delay = 1/(self.WPM/60)

	def readText(self):
		spacePress = False
		text = open(self.textFile,"r",encoding="utf8")
		font = pygame.font.Font('freesansbold.ttf', self.fontSize) 
		display_surface = pygame.display.set_mode((x, y))
		pygame.display.set_caption('textFile') 
		textLines = text.readlines()
		running = True
		wordRemain = ['1','2','3','4','5']
		yValues = [400,300,200,100]	

		listener = keyboard.Listener(on_press=pressed)
		listener.start()

		for line in textLines:
			stringSplit = line.split()
			for i in range(len(stringSplit)):
				if spacePress == False:
					wordRemain = rotate(wordRemain,-1)
					wordRemain[0] = stringSplit[i]
					display_surface.fill((255,255,255)) 
					for g in range(len(yValues)):
						textfont = font.render(wordRemain[g-1], True, (0,0,0), (255,255,255))
						textRect = textfont.get_rect() 
						textRect.center = (x/2,yValues[g-1])
						display_surface.blit(textfont, textRect) 
					pygame.display.flip()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						running = False
				if running == False:
					break	
				time.sleep(self.delay)
			if running == False:
				break
		text.close()

filePath = 'C:/Users/James Rossano/Documents/My_Shit/Programming_Files/BraveNewWorld.txt'
file = readText(filePath,200,40)
file.readText()
