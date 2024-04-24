import pygame as pg
def draw_base(screen):
    square_counter=0
    square_y=0
    for i in range(8):
        if square_counter%2!=0:
            square_color=(124,149,93)
        else:
            square_color=(238,238,213)
        square_x=0
        for i in range(8):
            pg.draw.rect(screen,square_color,[square_x,square_y,80,80])
            square_x+=80
            if square_color==(238,238,213):
                square_color=(124,149,93)
            else:
                square_color=(238,238,213)
        square_y+=80
        square_counter+=1


def draw_pieces(screen,board,pieces_list):
    p_x=0
    p_y=0
    for i in board:
        p_x=0
        for q in i:
            if q=="#":
                pass
            elif q=="R":
                screen.blit(pieces_list[0].surface,(p_x,p_y))
                pieces_list[0].pos=(p_x,p_y)
            elif q=="N":
                screen.blit(pieces_list[1].surface,(p_x,p_y))
                pieces_list[1].pos=(p_x,p_y)
            elif q=="B":
                screen.blit(pieces_list[2].surface,(p_x,p_y))
                pieces_list[2].pos=(p_x,p_y)
            elif q=="Q":
                screen.blit(pieces_list[3].surface,(p_x,p_y))
                pieces_list[3].pos=(p_x,p_y)
            elif q=="K":
                screen.blit(pieces_list[4].surface,(p_x,p_y))
                pieces_list[4].pos=(p_x,p_y)
            elif q=="P":
                screen.blit(pieces_list[5].surface,(p_x,p_y))
                pieces_list[5].pos=(p_x,p_y)            
            elif q=="r":
                screen.blit(pieces_list[6].surface,(p_x,p_y))
                pieces_list[6].pos=(p_x,p_y)
            elif q=="n":
                screen.blit(pieces_list[7].surface,(p_x,p_y))
                pieces_list[7].pos=(p_x,p_y)
            elif q=="b":
                screen.blit(pieces_list[8].surface,(p_x,p_y))
                pieces_list[8].pos=(p_x,p_y)
            elif q=="q":
                screen.blit(pieces_list[9].surface,(p_x,p_y))
                pieces_list[9].pos=(p_x,p_y)
            elif q=="k":
                screen.blit(pieces_list[10].surface,(p_x,p_y))
                pieces_list[10].pos=(p_x,p_y)
            elif q=="p":
                screen.blit(pieces_list[11].surface,(p_x,p_y))
                pieces_list[11].pos=(p_x,p_y)
            p_x+=80
        p_y+=80



    