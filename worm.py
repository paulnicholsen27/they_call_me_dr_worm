import pygame
import random
import os
#pygame.init()
pygame.font.init()
os.system("clear")


class Worm:
	just_eaten = False
	def __init__(self, surface):
		self.surface = surface
		self.x = surface.get_width()/2
		self.y = surface.get_height()/2
		self.length = 1
		self.grow_to = 50
		self.vx = 0
		self.vy = -1
		self.body = []
		self.crashed = False
		self.color = 0, 150, 0
		
	def key_event(self,event):
		if event.key == pygame.K_UP:
			if self.vy == 1:
				return
			else:
				self.vx = 0
				self.vy = -1
		elif event.key == pygame.K_DOWN:
			if self.vy == -1:
				return
			else:
				self.vx = 0
				self.vy = 1
		elif event.key == pygame.K_LEFT:
			if self.vx == 1:
				return
			else:
				self.vx = -1
				self.vy = 0
		elif event.key == pygame.K_RIGHT:
			if self.vx == -1:
				return
			else:
				self.vx = 1
				self.vy = 0
			
	def move(self):
		self.x += self.vx
		self.y += self.vy
		
		if (self.x, self.y) in self.body:
			self.crashed = True
			
		self.body.insert(0, (self.x, self.y))
		
		if self.grow_to > self.length:
			self.length += 1
		
		if len(self.body) > self.length: 
			self.body.pop()
		
	def draw(self):
		worm_size = 3	
		if self.just_eaten:
			for x, y in self.body:
				pygame.draw.rect(self.surface, self.color, (x, y, worm_size, worm_size), 0)
			self.just_eaten = False
		else:
			x, y = self.body[0]
			pygame.draw.rect(self.surface, self.color, (x, y, worm_size,worm_size), 0)
			x,y = self.body[-1]	
			pygame.draw.rect(self.surface, (0,0,0), (x, y, worm_size,worm_size), 0)

	def position(self):
		return self.x, self.y
		
	def eat(self):
		self.grow_to += new_cookie.size * 10
		
class Food:
	def __init__(self, surface):
		self.size = random.randint(20,30)
		self.surface = surface
		self.x = random.randint(5, surface.get_width() - 10 - self.size)
		self.y = random.randint(5, surface.get_height() - 10 - self.size)
		while self.position_checker():
			self.x = random.randint(5, surface.get_width() - 10 - self.size)
			self.y = random.randint(5, surface.get_height() - 10 - self.size)
	
	def draw(self):
		resized_cookie = pygame.Surface((self.size, self.size))
		pygame.transform.scale(cookie, (self.size, self.size), resized_cookie)
		resized_cookie.set_colorkey((0,0,0))
		screen.blit(resized_cookie, (self.x, self.y))
		
	def position(self):
		return self.x, self.y

	def check_if_eaten(self, x, y):
		if x < self.x or x > self.x + self.size or y < self.y or y > self.y + self.size:
			return False
		else:
			return True
			
	def position_checker(self):
		for i in range(self.size):
			if (self.x+i,self.y+i) in w.body:
				return True
			elif (self.x+i,self.y+i) in score_locations:
				return True
		for j in range(self.size-1, -1, -1):
			if (self.x+self.size - j,self.y+j) in w.body:
				return True
			elif (self.x+self.size - j,self.y+j) in score_locations:
				return True
		return False
		
	def erase(self):
		pygame.draw.rect(self.surface, (0,0,0), (self.x, self.y, self.size, self.size), 0)

class Points:
	def __init__(self, surface):
		self.surface = surface
		self.score = 0
		self.font = pygame.font.Font(None, 50)

	
	def display(self):
		score_display = "Score: " + str(self.score)
		score_display = font.render(score_display, True, (0, 0, 250), (0,0,0))
		score_display.set_colorkey((0,0,0))
		scoreRect = score_display.get_rect(topleft = (460,10))
		screen.fill((0,0,0), scoreRect)
		screen.blit(score_display, scoreRect)		

	
	def update(self):
		self.score += new_cookie.size * speed
	
		
		
print("Choose a difficulty level by typing a number. ")
need_speed = True
while need_speed:
	try:
		speed = int(raw_input("1 - Easy  2 - Medium  3 - Hard  4 - Insane: "))
	except ValueError:
		speed = 0
	if speed in range(1, 5):
		need_speed = False
	else:
		print "Please input a number from 1 to 4."
		
FPS = 60
pygame.init()
boing = pygame.mixer.Sound("bounce.wav")
gameover = pygame.mixer.Sound("gameover.wav")		
width = 640
height = 400

screen = pygame.display.set_mode((width, height))
pygame.mouse.set_visible(False)
pygame.display.set_caption('Feed the Worm!')
clock = pygame.time.Clock()
running = True

cookie = pygame.image.load('cookie.bmp').convert()
cookie.set_colorkey(cookie.get_at((0,0)))
cookierect = cookie.get_rect()
score_locations = []
for i in range (0, 40):
	for j in range (460, width):
		score_locations.append((i,j))

w = Worm(screen)
new_cookie = Food(screen)
score_total = Points(screen)

while running:
	for instance in range(speed + 1):
		w.move() 
		w.draw()
	font = pygame.font.Font(None, 32)
	score_total.display()
	new_cookie.draw()
	if w.crashed or w.x<=0 or w.x >= width - 1 or w.y<=0 or w.y >= height -1:

		gameover.play()
		font = pygame.font.Font(None, 80)
		end_game = font.render("Game Over!", True, (255, 0, 0), (0,0,0))
		end_game.set_colorkey((0,0,0))
		endRect = end_game.get_rect(centerx = width/2, centery = height / 2)
		screen.blit(end_game, endRect)
		pygame.display.flip()
 		pygame.time.delay(3500)
		running = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			w.key_event(event)

	if new_cookie.check_if_eaten(w.x, w.y):
		w.eat()
		new_cookie.erase()
		score_total.update()
		boing.play()
		w.just_eaten = True
		new_cookie = Food(screen)

	pygame.display.flip()
	clock.tick(60)