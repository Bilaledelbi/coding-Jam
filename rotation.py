import pygame
import time


def play(av0 = 0,F = [], i = 0, d = []):
	pygame.init()

	WIDTH = 640
	HEIGHT = 480

	WIN = pygame.display.set_mode((WIDTH, HEIGHT))

	x = 300
	y = 200
	teta = 0
	tetas = 0
	tetas0 = av0
	forces = F
	dr = d
	MF = 0
	I = i #(3.4 * (1)/4) circle
	j = 0
	for i in forces:
	    MF += (i * dr[j])
	    j+=1

	a = MF/I

	start = time.time()

	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		end = time.time()
		t = end - start
		print(t)
		teta = ((0.5*a*t**2) + tetas0 * t)  *57.296
		tetas = a*t + tetas0
		if(I == (3.4 * (1)/4)):
			img = pygame.image.load("rot assets/ball.png")
		else:
			img = pygame.image.load("rot assets/rectangle.png")
			#no picture yet
		img = pygame.transform.rotate(img, teta)
		WIN.fill((0,255,255))
		WIN.blit(img, (x - int(img.get_width()/2), y - int(img.get_height()/2)))

		pygame.display.update()




	pygame.quit()
