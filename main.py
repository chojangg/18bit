# 18bit
# 게임 방법
# 하늘에서 떨어지는 피구공을 피하는 게임
# 캐릭터를 방향키로 좌우 이동
# 피구공을 피하면 점수가 올라감
# 피구공에 맞게되면 게임이 끝남

import pygame  # 1. pygame 선언
import random
import os

pygame.init()  # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언

size = [640,640]
screen = pygame.display.set_mode((size))
pygame.display.set_caption('18bit')

done = False
clock = pygame.time.Clock()
FONT_NAME = 'arial'

myimg = pygame.image.load('img/backgroud.png')
start = pygame.image.load('img/start_img.jpg')
def startGame():
	ball_image = pygame.image.load('img/ball.png')
	ball_image = pygame.transform.scale(ball_image, (70, 70))
	balls = []

	for i in range(5):
		rect = pygame.Rect(ball_image.get_rect())
		rect.left = random.randint(0, size[0])
		rect.top = -100
		dy = random.randint(3, 6)
		balls.append({'rect': rect, 'dy': dy})

	person_image = pygame.image.load('img/character.png')
	person_image = pygame.transform.scale(person_image, (130, 130))
	person = pygame.Rect(person_image.get_rect())
	person.left = size[0] // 2 - person.width // 2
	person.top = size[1] - person.height
	person_dx = 0
	person_dy = 0

	# time = 50000
	# start_ticks = pygame.time.get_ticks()

	global done
	while not done:
		clock.tick(30)
		screen.blit(myimg, (0, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
				break
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					person_dx = -15
				elif event.key == pygame.K_RIGHT:
					person_dx = 15
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					person_dx = 0
				elif event.key == pygame.K_RIGHT:
					person_dx = 0

		for bomb in balls:
			bomb['rect'].top += bomb['dy']
			if bomb['rect'].top > size[1]:
				balls.remove(bomb)
				rect = pygame.Rect(ball_image.get_rect())
				rect.left = random.randint(0, size[0])
				rect.top = -100
				dy = random.randint(3, 9)
				balls.append({'rect': rect, 'dy': dy})

		person.left = person.left + person_dx

		if person.left < 0:
			person.left = 0
		elif person.left > size[0] - person.width:
			person.left = size[0] - person.width

		screen.blit(person_image, person)

		for bomb in balls:
			if bomb['rect'].colliderect(person):
				done = True
			screen.blit(ball_image, bomb['rect'])

		# #제한 시간
		# elapsed_time = (pygame.time.get_ticks() - start_ticks / 1000)
		#
		# timer = game_font.render(str(int(time - elapsed_time)), True,
		# 					 (255, 0, 0))
		# screen.blit(timer, (10, 10))
		#
		# if time - elapsed_time <= 0:
		# 	print("타임아웃")

		pygame.display.update()

def main_menu():
    while True:
        screen.blit(start, (0, 0))

        # MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = (pygame.image.load("img/btn_start.png"))

        for button in [PLAY_BUTTON]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput():
                    startGame()
                    # sys.exit()

    pygame.display.update()

# def score(self):
# 	self.score = 0
#
#
# def update(self):
# 	# Game Loop - Update
# 	...
#
# 	# If player reached top 1/4 of screen
# 	if self.player.rect.top <= size / 4:
# 		self.player.pos.y += abs(self.player.vel.y)
# 		for plat in self.platforms:
# 			plat.rect.y += abs(self.player.vel.y)
# 			if plat.rect.top >= size:
# 				plat.kill()
# 				self.score += 10
#
# def draw_text(self, text, size, color, x, y):
#         font = pygame.font.Font(self.font_name, size)
#         text_surface = font.render(text, True, color)
#         text_rect = text_surface.get_rect()
#         text_rect.midtop = (x, y)
#         self.screen.blit(text_surface, text_rect)
#
# class Game:
#     def __init__(self):
#         # initialize game window, etc
#         ...
#         self.font_name = pygame.font.match_font(FONT_NAME)
#
#
# def draw(self):
# 	# Game Loop - Draw
# 	self.all_sprites.draw(self.screen)
# 	self.draw_text(str(self.score), 22, size / 2, 15)  ###
#
# 	# *after* drawing everything, flip the display
# 	pygame.display.flip()


#게임 시작
startGame()
# pg 종료
pygame.quit()