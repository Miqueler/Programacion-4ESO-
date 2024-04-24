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
    elif not x and counter==2:
        counter=3
    elif not x and counter==3:
        counter=0
    return counter

def find_piece(board):
    mouse_pos=pg.mouse.get_pos()
    coords=[mouse_pos[0]//80,mouse_pos[1]//80]
    if board[coords[1]][coords[0]]!="#":
        piece=board[coords[1]][coords[0]]
        board[coords[1]].pop(coords[0])
        board[coords[1]].insert(coords[0],"#")
        return (piece,board,coords)


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
    return board

def place_pieces(board,coords,piece):
    mouse_pos=pg.mouse.get_pos()
    round_mouse_pos=[mouse_pos[0]//80,mouse_pos[1]//80]
    if piece!="#":
        if piece.isupper() and board[round_mouse_pos[1]][round_mouse_pos[0]].islower() or piece.islower() and board[round_mouse_pos[1]][round_mouse_pos[0]].isupper():
            board[round_mouse_pos[1]].pop(round_mouse_pos[0])
            board[round_mouse_pos[1]].insert(round_mouse_pos[0],piece)
        elif board[round_mouse_pos[1]][round_mouse_pos[0]]=="#":
            board[round_mouse_pos[1]].pop(round_mouse_pos[0])
            board[round_mouse_pos[1]].insert(round_mouse_pos[0],piece)
        else:
            board[coords[1]].pop(coords[0])
            board[coords[1]].insert(coords[0],piece)