import random

class Ball:
    def __init__(self,radius,speed,x,y):
        self.radius=radius
        self.speed=speed
        self.x=x
        self.y=y        
        self.move_up=random.choice([True,False])
        self.move_right=random.choice([True,False])          

    def change_y_direction(self,up):
        if((up==True or up==False)):
            self.move_up=up                     
        else:
            print("Bad direction arguments!\n");

    def change_x_direction(self,right):
        if((right==True or right==False)):
            self.move_right=right                       
        else:
            print("Bad direction arguments!\n");

    def move_vertical(self,glob_height):
        if self.y<self.radius:self.move_up=False
        if self.y>(glob_height-self.radius):self.move_up=True

        if self.move_up: self.y-=self.speed
        else :self.y+=self.speed

    def move_horizontal(self):
        if self.move_right: self.x+=self.speed
        else :self.x-=self.speed      

    def hit_racket(self,racket_Y,glob_height,glob_width,points):#change to racket height, add start position function
        if (self.y+self.radius)>=racket_Y:
                if self.y<=(racket_Y+self.radius+glob_height/6):
                    self.move_right=not self.move_right
                   
                else:
                    self.x=glob_width/2
                    self.y=glob_height/2
                    points+=1

                    self.move_up=random.choice([True,False])
                    self.move_right=random.choice([True,False])

        return points

                          