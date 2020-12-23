import pygame as py
import math
import random
import sys
from queue import Queue

width = 600

py.init();
screen = py.display.set_mode((width,width));

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)



class Node():
    def __init__(self,row,col,width):
        self.row = row;
        self.col = col;
        self.width = width
        self.x = row*width;
        self.y = col*width;
        self.color = WHITE;
        self.neighbour = [];

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE


    def draw(self,screen):
        py.draw.rect(screen,self.color,(self.x,self.y,self.width,self.width));





def algorithm():
    pass






def make_grid(row,width):
    grid = []
    gap = width//row;
    for i in range(row):
        grid.append([])
        for j in range(row):
            node = Node(i,j,gap)
            grid[i].append(node);

    return grid

def draw_grid(screen,row,width):
    gap = width//row;
    for i in range(row):
        py.draw.line(screen,GREY,(0,i*gap),(width,i*gap))
        for j in range(row):
            py.draw.line(screen,GREY,(j*gap,0),(j*gap,width))



def draw(screen,grid,rows,width):
    screen.fill(WHITE);
    for row in grid:
        for node in row:
            node.draw(screen);

    draw_grid(screen,rows,width)
    py.display.update();




def get_clicked(pos,rows,width):
    gap = width//rows;
    y,x = pos
    row = y//gap
    col = x//gap

    return row,col




py.display.set_caption('Yogendra Visualization on BFS');

node = Node(5,5,10);



def main(screen,width):
    rows = 30
    grid = make_grid(rows,width);
    start = None;
    end = None;
    run = True;
    started = False;
    game_flag = False;
    

    
    while run:
        draw(screen,grid,rows,width)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False;

            if started:
                continue;

            if py.mouse.get_pressed()[0]:
                pos = py.mouse.get_pos();
                row,col = get_clicked(pos,rows,width)
                node = grid[row][col];

                if not start and node!=end:
                    Queue.put(node);
                    
                    start = node;
                    start.make_start();

                elif not end and node!=start:
                    end = node;
                    end.make_end();

                elif node!=start and node!=end:
                    node.make_barrier();

            
            if py.mouse.get_pressed()[2]:
                pos = py.mouse.get_pos();
                row,col = get_clicked(pos,rows,width)
                node = grid[row][col];
                node.reset();
                if node == start:
                    start = None;
                elif node == end:
                    end = None;


            if event.type == py.KEYDOWN:
                if event.type == py.K_SPACE:
                    start_flag = True;





    if start_flag:
        
                
        
        



main(screen,width)
py.quit()
