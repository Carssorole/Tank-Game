import pygame 

pygame.init() 

color = (255,255,255) 
rect_color = (255,0,0) 

# CREATING CANVAS 
canvas = pygame.display.set_mode((500, 500)) 
  
# TITLE OF CANVAS 
pygame.display.set_caption("The Scrummest Tanker") 
exit = False

while not exit: 
	canvas.fill(color) 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			exit = True

	pygame.draw.rect(canvas, rect_color, 
					pygame.Rect(30,30,60,60))
	rect_color = (0,0,255) 
	pygame.draw.rect(canvas, rect_color, 
					pygame.Rect(100,100,90,90))
	pygame.display.update() 

    