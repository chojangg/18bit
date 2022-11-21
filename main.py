# 18bit
# 게임 방법
# 하늘에서 떨어지는 피구공을 피하는 게임
# 캐릭터를 방향키로 좌우 이동
# 피구공을 피하면 점수가 올라감
# 피구공에 맞게되면 게임이 끝남


import pygame as pg
pg.init()
disw,dish = 640,640
ourScreen = pg.display.set_mode((disw,dish))
pg.display.set_caption('18bit')
finish = False

myimg = pg.image.load('img/backgroud.png')
def useimg(x,y):
	ourScreen.blit(myimg,(x,y))

x,y = (disw*0.003),(dish*0.003)

while not finish:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			finish =True
		ourScreen.fill((0,0,0))
		useimg(x,y)
		pg.display.flip()