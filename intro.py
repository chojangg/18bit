import pygame
import tkinter as tk


pygame.init()

# width, length = 640,640
#
# ourScreen = pygame.display.set_mode((width,length))
# pygame.display.set_caption('18bit')
# finish = False
# myimg = pygame.image.load('img/start_img.jpg')
#
# def useimg(x,y):
# 	ourScreen.blit(myimg,(x,y))
#
# x,y = (width*0.003),(length*0.003)
#
# while not finish:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			finish =True
# 		ourScreen.fill((0,0,0))
# 		useimg(x,y)
# 		pygame.display.flip()



window = tk.Tk()
window.geometry('500x400')
startbtn_img = tk.PhotoImage(file="img/start_img.jpg")
startbtn = tk.Button(window, image=startbtn_img, command=window.destroy)
startbtn.place(x=0, y=0)

window.mainloop()