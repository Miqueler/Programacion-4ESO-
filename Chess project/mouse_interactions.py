import pygame as pg

def click_detector():
    if pg.mouse.get_pressed()[0]:
        is_click=True
    else:
        is_click=False
    return is_click

def single_click_detecter(counter):
    x=click_detector()
    if x and counter==0:
        counter=1
    elif x and counter==1:
        counter=2
    if not x:
        counter=0
    return counter

def find_piece(board):
    mouse_pos=pg.mouse.get_pos()
    coords=[mouse_pos[0]//80,mouse_pos[1]//80]
    if board[coords[1]][coords[0]]!="#":
        return board[coords[1]][coords[0]]


def draw_in_cursor(pieces_list,screen,board,piece):
    real_mouse_pos=pg.mouse.get_pos(board)
    mouse_pos=[int(real_mouse_pos[0])-40,int(real_mouse_pos[1])-40]
    if piece=="#":
        pass
    elif piece=="R":
        screen.blit(pieces_list[0].surface,mouse_pos)
    elif piece=="N":
        screen.blit(pieces_list[1].surface,mouse_pos)
    elif piece=="B":
        screen.blit(pieces_list[2].surface,mouse_pos)
    elif piece=="Q":
        screen.blit(pieces_list[3].surface,mouse_pos)
    elif piece=="K":
        screen.blit(pieces_list[4].surface,mouse_pos)
    elif piece=="P":
        screen.blit(pieces_list[5].surface,mouse_pos)          
    elif piece=="r":
        screen.blit(pieces_list[6].surface,mouse_pos)
    elif piece=="n":
        screen.blit(pieces_list[7].surface,mouse_pos)
    elif piece=="b":
        screen.blit(pieces_list[8].surface,mouse_pos)
    elif piece=="q":
        screen.blit(pieces_list[9].surface,mouse_pos)
    elif piece=="k":
        screen.blit(pieces_list[10].surface,mouse_pos)
    elif piece=="p":
        screen.blit(pieces_list[11].surface,mouse_pos)