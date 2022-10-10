import time
import wx
from graphics import *

app = wx.App(False)
width, height = wx.GetDisplaySize()


def Main (Titulo: str, W: int, H:int):
    win = GraphWin(Titulo, W, H, autoflush=False)
    win.setBackground('black')
    framerate = 1/10

    lst = []
    lst1 = []
    lst2 = []
    lst3 = []
    for x in range(4):
        menino = Image(Point(400, 300), "D:\\graphics\\" + str(x) + ".gif")
        lst.append(menino)
    for j in range(4, 8):
        menino1 = Image(Point(400, 300), "D:\\graphics\\" + str(j) + ".gif")
        lst1.append(menino1)
    for i in range(8, 12):
        menino2 = Image(Point(400, 300), "D:\\graphics\\" + str(i) + ".gif")
        lst2.append(menino2)
    for w in range(12, 16):
        menino3 = Image(Point(400, 300), "D:\\graphics\\" + str(w) + ".gif")
        lst3.append(menino3)
    print(lst3)
    num = 0
    lst[0].draw(win)
    while win.closed == False:
        keyCheck = win.checkKey()
        #Baixo
        if keyCheck == 'Down':
                #Animacao pra baixo
                for x in range(4):
                    lst1[x].undraw()
                    lst2[x].undraw()
                    lst3[x].undraw()
                lst[num].undraw()
                lst[num].draw(win)

                if not num < len(lst) - 1:
                    num = 0
                else:
                    num += 1
                lst[num - 2].undraw()
                lst[num].undraw()
        #Esquerda        
        elif keyCheck == 'Left':
            #Animação pra esquerda
            for x in range(4):
                lst[x].undraw()
                lst2[x].undraw()
                lst3[x].undraw()
            lst1[num].undraw()
            lst1[num].draw(win)

            if not num < len(lst1) - 1:
                num = 0
            else:
                num += 1
            lst1[num - 2].undraw()
            lst1[num].undraw()
        #Direita
        elif keyCheck == 'Right':
            #Animação pra direita
            for x in range(4):
                lst[x].undraw()
                lst1[x].undraw()
                lst3[x].undraw()
            lst2[num].undraw()
            lst2[num].draw(win)

            if not num < len(lst2) - 1:
                num = 0
            else:
                num += 1
            lst2[num - 2].undraw()
            lst2[num].undraw()

        #Cima
        elif keyCheck == 'Up':
            #Animação pra cima
            for x in range(4):
                lst[x].undraw()
                lst2[x].undraw()
                lst1[x].undraw()
            lst3[num].undraw()
            lst3[num].draw(win)

            if not num < len(lst3) - 1:
                num = 0
            else:
                num += 1
            lst3[num - 2].undraw()
            lst3[num].undraw()
        
        


        win.update()
        time.sleep(framerate)

Main("Labirinto", width, height)