# 18bit
# 게임 방법
# 하늘에서 떨어지는 피구공을 피하는 게임
# 캐릭터를 방향키로 좌우 이동
# 피구공을 피하면 점수가 올라감
# 피구공에 맞게되면 게임이 끝남
import pygame   # 1. pygame 선언
import time
import sys
import random
import threading
import os
from db import DBHelper
from tkinter import *
from tkinter.simpledialog import *

db = DBHelper()


pygame.init()  # 2. pygame 초기화
# color
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
# 파일경로
now_path = os.path.dirname(__file__)
image_file_path = os.path.join(now_path, "img")
bgm_file_path = os.path.join(now_path, "bgm")
# 배경 이미지
startbackground = pygame.image.load(os.path.join(image_file_path, "start_img.jpg"))
background = pygame.image.load(os.path.join(image_file_path, "background.png"))
def display(color_=False):
    if color_: Game_screen.fill(color_)  # color 인수로 들어오면 color색으로 화면 덮기
    pygame.display.update()  # 창 띄우기
def Open_screen(img, caption, size=[640,640]):  # 창 만들기(배경색,캡션이름,해상도)
    global Game_screen
    Game_screen = pygame.display.set_mode(size)
    pygame.display.set_caption(caption)
    Game_screen.blit(img, (0, 0))
def Open_text(Font_size, string, Font, color, xy):  # 텍스트 띄우기(글씨크기,문구,폰트,색,좌표)
    text_box = pygame.font.SysFont(Font, Font_size)
    text = text_box.render(string, True, color)
    Game_screen.blit(text, xy)
    display()
def KEY_CHECK():
    for event in pygame.event.get():  # 나가기 누를때 종료
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_ESCAPE]:  # ESC 누르면 종료
        pygame.quit()
        sys.exit()
    return key_pressed  # 누른 키 리스트 반환


def Game_over():
    Open_text(72, "Game Over!", "Bold", Red, (180, 180))
    pygame = Tk();
    pygame.geometry("300x200")
    list_listbox = Listbox(pygame)
    Name = askstring("18bit 랭킹", "이름을 입력하세요")
    db.insert(Name, Character.score)
    saying_tb = db.select()
    for i in range(len(saying_tb)):
        list_listbox.insert(i, f'{saying_tb[i][0]}. {saying_tb[i][1]}')
    list_listbox.pack()
    pygame.mainloop()
    time.sleep(3)
    pygame.quit()
    sys.exit()



class character:
    def __init__(self, address):
        self.image = pygame.image.load(address)
        self.pos_x = 260  # 초기 위치
        self.speed = 10  # 속력
        self.score = 0
    def pos(self):  # 좌표 반환
        return (self.pos_x, 500)
    def pos_loop(self):  # 캐릭터 화면 벗어나면 반대편에서 나오기
        if self.pos_x < -60:
            self.pos_x = 840 + self.pos_x
        elif self.pos_x > 780:
            self.pos_x = self.pos_x - 840
    def move(self, key_pressed):  # 방향키 확인 후 캐릭터 위치 조정
        if key_pressed[pygame.K_LEFT]:
            self.pos_x = self.pos_x - self.speed
        elif key_pressed[pygame.K_RIGHT]:
            self.pos_x = self.pos_x + self.speed
        self.pos_loop()
class ball:
    def __init__(self, item_number):
        self.item_number = item_number
        if item_number == 0:  # 아이템 넘버0 = 공
            self.image = pygame.image.load(os.path.join(image_file_path, "ball.png"))
        self.pos_x = random.randrange(0, 8) * 100 + 25  # 공 x좌표 랜덤설정(간격100)
        self.pos_y = 10
        self.initial_speed = random.randrange(2, 6)
    def speed(self):
        self.total_speed = self.initial_speed + balls_change_speed
        if self.total_speed > 50:
            self.total_speed = 50
        return self.total_speed
    def pos(self):
        return [self.pos_x, self.pos_y]
def ball_create():
    balls.append(ball(0))  # 공 만들어서 리스트에 추가
    threading.Timer(1, ball_create).start()  # 1초마다 반복
def Colide_Check(character_pos_x, index):  # 충돌하면 game_over
    global balls
    global balls_change_speed
    if len(balls) - 1 < index: return 0
    if 480 < balls[index].pos_y < 560:
        if balls[index].pos_x - 91 < character_pos_x < balls[index].pos_x + 50:  # 충돌인경우
            if balls[index].item_number == 0:  # 공에 부딪히면
                bgm2 = pygame.mixer.Sound(os.path.join(bgm_file_path, "crash.wav"))  # 효과음
                bgm2.play()
                if len(hearts) > 1:
                    del hearts[len(hearts) - 1]
                    time.sleep(0.5)
                    balls.remove(balls[index])
                else:
                    Game_over()  # 하트 없으면 게임오버
            else:
                Character.score = Character.score + len(balls) - 1
                balls = []
class heart:
    def __init__(self, index):
        self.pos_x = 40 * index + 15
        self.pos_y = 10
        self.image = pygame.image.load(os.path.join(image_file_path, "heart1.png"))
    def pos(self):
        return [self.pos_x, self.pos_y]
def falling_ball(index):
    if index == len(balls): return 0  # 리스트 아웃 오브 레인지 방지
    Game_screen.blit(balls[index].image, balls[index].pos())  # 화면에 공 나타내기
    balls[index].pos_y = balls[index].pos_y + balls[index].speed()  # 좌표 조정
    falling_ball(index + 1)
    # 재귀함수 호출(바로 다음 인덱스로 가기 때문에 리스트 끝에 도달 후 밑에 코드 실행)
    Colide_Check(Character.pos_x, index)
    # 마지막 인덱스부터 먼저 실행 하고 첫 번째 인덱스가 마지막으로 실행
def main():
    # 초기 화면
    Open_screen(startbackground, "18bit")
    Open_text(25, "Press spacebar to start!", "Monospace", White, (130, 300))
    # 스페이스바 대기
    Run = False
    while not Run:
        pressed = KEY_CHECK()  # 키 누르는지 확인
        if pressed[pygame.K_SPACE]:  # 스페이스바 눌렀을 때
            Run = True
            display(White)  # 하얀 바탕으로 덮기
            Open_text(72, "Start!", "Bold", Black, (255, 255))  # 1초 동안 start! 문구 나타내기
            time.sleep(1)
            display(White)
            pygame.mixer.music.load(os.path.join(bgm_file_path, "backgroundmusic.mp3"))
            pygame.mixer.music.play(-1)
    # 게임 중
    global Character
    Character = character(os.path.join(image_file_path, "character.png"))  # 캐릭터 생성
    global balls_change_speed
    balls_change_speed = 0
    global balls
    balls = []  # 전체 공 관리할 리스트
    global hearts
    hearts = [heart(0), heart(1), heart(2)]
    global falling_item
    falling_item = False
    clock = pygame.time.Clock()
    ball_create()
    while Run:
        pressed = KEY_CHECK()  # 키 누르는지 확인
        Character.move(pressed)  # 캐릭터 이동
        Game_screen.blit(Character.image, Character.pos())
        for x in range(len(hearts)):
            Game_screen.blit(hearts[x].image, hearts[x].pos())  # 하트 표시
        falling_ball(0)  # 떨어지는 공 좌표 조정 및 충돌 확인
        balls.sort(key=lambda ball: ball.pos_y, reverse=True)
        # 바닥에 가까운 순으로 공 정렬
        while len(balls) and balls[0].pos_y > 560:  # 바닥 도달한 공 있으면
            if balls[0].item_number == 0:
                Character.score = Character.score + 1  # 점수 추가
            else:
                falling_item = False
            balls.remove(balls[0])  # 전체 공 리스트에서 빼고
            if Character.score % 10 == 0 and Character.score:  # 10점마다 속도업
                balls_change_speed = balls_change_speed + 1
        Open_text(48, "SCORE : {}".format(Character.score), "Bold", Black, (280, 0))
        Open_screen(background,"")
        clock.tick(30)
main()