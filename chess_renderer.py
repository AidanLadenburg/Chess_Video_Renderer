import pygame
from PIL import Image
from numpy import array
import os
import math
import sys
import time


import_folder = "frames"
export_folder = "out"

print(sys.argv, end = " ")
multiplier = 5 #Raising this will increase the # of pieces used to fill the space
resolution = (1920, 1080) #Change to desired img size | Please use the same Ratio as the input imgs or it will clip | Also, please use standard img resolutions or things could get messy
gcd = math.gcd(resolution[0], resolution[1]) #Calc GCD to find the appropriate tile size | Non-Standard Img resulutions may make this freak out
board_size = (int(resolution[0]/gcd)*multiplier,int(resolution[1]/gcd)*multiplier)

tile_size = (resolution[0]/board_size[0])



pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
running = True

#colors (Add more colors if you want to change the tile color scheme)
white = (235, 236, 208)
green = (119, 149, 86)

beige = (240, 217, 181)
brown = (181, 136, 99)

pieces = {"k":"black_king.png", "q":"black_queen.png", "b":"black_bishop.png", "n":"black_knight.png", "r":"black_rook.png", "p":"black_pawn.png",
          "K": "white_king.png", "Q":"white_queen.png", "B":"white_bishop.png", "N":"white_knight.png", "R":"white_rook.png", "P":"white_pawn.png"}

def draw_check():
    for i in range(board_size[0]):
        for j in range(board_size[1]):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, beige, (i*tile_size, j*tile_size, tile_size, tile_size))
            else:
                pygame.draw.rect(screen, brown, (i*tile_size, j*tile_size, tile_size, tile_size))


def place_pieces(layout):
    pygame.display.set_caption(f"Placing Pieces For Frame {k}")
    row=0
    for item in layout:
        column = 0
        for piece in [*item]:
            if piece.isnumeric():
               column+=int(piece)
            else:
                place = pygame.image.load(f'./imgs-80px/{pieces[piece]}').convert_alpha()
                place = pygame.transform.smoothscale(place, (tile_size,tile_size))
                screen.blit(place, ((column*tile_size),(row*tile_size)))
                column+=1
        row+=1



def render_frame(img):
    pygame.display.set_caption(f"Calculating Chess Frame {k}")
    
    frame = Image.open(f'./{import_folder}/{img}').convert('L') #Convert to Grayscale
    wpercent = (board_size[0]/float(frame.size[0]))
    hsize = int((float(frame.size[1])*float(wpercent)))
    frame = frame.resize((board_size[0],hsize))
    #frame.show() #if you want to see what the image looks like after processing

    layout = ""
    arr = array(frame)
    for i in arr: #If getting poor results, change the piece thresholds here
        for j in i:
            if j > 160:
                layout+="P"
            elif j>120:
                layout+="B"
            elif j>100:
                layout+="Q"
            elif j>60:
                layout+="q"
            elif j>20:
                layout+="b"
            else:
                layout+="p"
        layout+="/"
        
    layout = layout.split("/")
    #print(layout) #if you want to see the text representation of the img
    place_pieces(layout)      


while running:
    k=0
    frames = sorted(os.listdir(f"./{import_folder}"))
    draw_check()

    for img in frames:
        draw_check()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        render_frame(img)
    
        pygame.display.update()
        pygame.image.save(screen, f"./{export_folder}/{img}")
        
        k+=1
        
    running=False

pygame.quit()