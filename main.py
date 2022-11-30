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

		pygame.display.update()



#게임 시작
startGame()
# pg 종료
pygame.quit()