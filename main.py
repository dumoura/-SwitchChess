import asyncio
import pygame
import sys
import random

from const import *
from game import Game
from square import Square
from move import Move

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Switch Chess')
        self.game = Game()
        self.switch_players = False

    def flip_coin(self):
        result = random.choice(["heads", "tails"])
        pygame.display.set_caption(f"Coin flip result: {result}! ")
        print(f"Coin flip result: {result}! ")
        return result

    def switch_player_positions(self):
        board = self.game.board
        
        for row in range(ROWS):
            for col in range(COLS):
                square = board.squares[row][col]
                
                if square.has_piece():
                    piece = square.piece

                    if piece.color == "white":
                        piece.color = "black"
                    else:
                        piece.color = "white"

    async def mainloop(self):
        
        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while True:
            # show methods
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_hover(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():

                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    # if clicked square has a piece ?
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        # valid piece (color) ?
                        if piece.color == game.next_player:
                            board.calc_moves(piece, clicked_row, clicked_col, bool=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            # show methods 
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                
                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # show methods
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)
                
                # click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        # create possible move
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        # valid move ?
                        if board.valid_move(dragger.piece, move):
                            # normal capture
                            captured = board.squares[released_row][released_col].has_piece()
                            board.move(dragger.piece, move)
                            
                            board.set_true_en_passant(dragger.piece)                            

                        # sounds
                            game.play_sound(captured)
                        # show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)

                     # flip coin after each full move
                            if game.move_count % 2 == 0:
                                flip_result = self.flip_coin()

                                if flip_result == "tails":
                                    game.next_player = "white"

                                else:
                                    game.next_player = "black"


                                if self.switch_players:
                                    self.switch_player_positions()

                            if game.move_count % 2 == 1:
                                if self.switch_players:
                                    self.switch_player_positions()

                                else:
                                    self.switch_players = True

# next turn
                            game.move_count += 1
                            game.last_move = move
                            game.next_turn()
            
                    dragger.undrag_piece()

            # key press
                elif event.type == pygame.KEYDOWN:
                
                # changing themes
                    if event.key == pygame.K_t:
                        game.change_theme()

                 # changing themes
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger

            # quit application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            pygame.display.update()
            await asyncio.sleep(0)

main = Main()
asyncio.run(main.mainloop())

