if mouse_holding_piece==True:
            real_mouse_pos=pg.mouse.get_pos()
            if test==False:
                fuck_off=board[mouse_pos[1]//80][mouse_pos[0]//80]
                board[mouse_pos[1]//80].pop(mouse_pos[0]//80)
                board[mouse_pos[1]//80].insert(mouse_pos[0]//80,"#")
                test=True

            print(fuck_off)
            if fuck_off=="#":
                pass
            elif fuck_off=="R":
                screen.blit(pieces_list[0].surface,real_mouse_pos)
                pieces_list[0].pos=(real_mouse_pos)
            elif fuck_off=="N":
                screen.blit(pieces_list[1].surface,real_mouse_pos)
                pieces_list[1].pos=(real_mouse_pos)
            elif fuck_off=="B":
                screen.blit(pieces_list[2].surface,real_mouse_pos)
                pieces_list[2].pos=(real_mouse_pos)
            elif fuck_off=="Q":
                screen.blit(pieces_list[3].surface,real_mouse_pos)
                pieces_list[3].pos=(real_mouse_pos)
            elif fuck_off=="K":
                screen.blit(pieces_list[4].surface,real_mouse_pos)
                pieces_list[4].pos=(real_mouse_pos)
            elif fuck_off=="P":
                screen.blit(pieces_list[5].surface,real_mouse_pos)
                pieces_list[5].pos=(real_mouse_pos)            
            elif fuck_off=="r":
                screen.blit(pieces_list[6].surface,real_mouse_pos)
                pieces_list[6].pos=(real_mouse_pos)
            elif fuck_off=="n":
                screen.blit(pieces_list[7].surface,real_mouse_pos)
                pieces_list[7].pos=(real_mouse_pos)
            elif fuck_off=="b":
                screen.blit(pieces_list[8].surface,real_mouse_pos)
                pieces_list[8].pos=(real_mouse_pos)
            elif fuck_off=="q":
                screen.blit(pieces_list[9].surface,real_mouse_pos)
                pieces_list[9].pos=(real_mouse_pos)
            elif fuck_off=="k":
                screen.blit(pieces_list[10].surface,real_mouse_pos)
                pieces_list[10].pos=(real_mouse_pos)
            elif fuck_off=="p":
                screen.blit(pieces_list[11].surface,real_mouse_pos)
                pieces_list[11].pos=(real_mouse_pos)
