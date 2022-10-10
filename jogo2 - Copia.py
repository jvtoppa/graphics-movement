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
    for x in range(16):
        menino = Image(Point(400, 300), "D:\\graphics\\" + str(x) + ".gif")
        lst.append(menino)
    num = 0
    lc = 0
    dc = 0
    rc = 0
    uc = 0
    lst[0].draw(win)
    while win.closed == False:
        
        keyCheck = win.checkKey()
        #Baixo
        if keyCheck == 'Down':
                if dc == 0:
                    num = 0
                lc = 0
                rc = 0
                uc = 0
                lst[0].undraw()
                for x in range(4, 15):
                    lst[x].undraw()
                #Animacao pra baixo
                lst[num].move(0,10)
                lst[num].undraw()
                lst[num-1].undraw()
                lst[num].draw(win)

                if num < len(lst) - 1 and num == 3:
                    num = 0
                else:
                    num += 1
                lst[num - 2].undraw()
                lst[num + 1].undraw()
                lst[num + 2].undraw()
                dc += 1
                
        #Esquerda        
        elif keyCheck == 'Left':
            dc = 0 
            rc = 0
            uc = 0
            if lc == 0:
                num = 4
            #Animação pra esquerda
            lst[num].move(-10,0)
            for x in range(4):
                lst[x].undraw()
                
            for x in range(8, 15):
                lst[x].undraw()
            lst[num].draw(win)

            if num < len(lst) - 1 and num == 7:
                num = 4
            else:
                num += 1
            lst[num - 2].undraw()
            lst[num + 1].undraw()
            lst[num + 2].undraw()
            lc += 1
        #Direita
        elif keyCheck == 'Right':
            lc = 0
            dc = 0
            uc = 0
            if rc == 0:
                num = 8
            for x in range(8):
                lst[x].undraw()
            for x in range(12, 15):
                lst[x].undraw()
            #Animação pra direita
            lst[num].move(10,0)
            lst[num].undraw()
            lst[num].draw(win)

            if num < len(lst) - 1 and num == 11:
                num = 8
            else:
                num += 1
            lst[num - 2].undraw()
            lst[num + 1].undraw()
            lst[num + 2].undraw()
            rc += 1

        #Cima
        elif keyCheck == 'Up':
            dc = 0
            rc = 0
            lc = 0
            if uc == 0:
                num = 11
            lst[num].move(0,-10)
            #Animação pra cima
            for x in range(12):
                lst[x].undraw()
            lst[num].undraw()
            if num != 16:
                num += 1
            if num == 16:
                num = 12
                lst[14].undraw()
            print(num)
            lst[num].draw(win)

            uc += 1
        
        


        win.update()
        time.sleep(framerate)

Main("Labirinto", width, height)