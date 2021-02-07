import pygame
import ball

pygame.init()
#getting screen size
monitor_size=pygame.display.Info()
glob_width=monitor_size.current_w
glob_height=(monitor_size.current_h-70)

#creating game window
screen=pygame.display.set_mode((glob_width,glob_height))
pygame.display.set_caption("PONGER v 0.02")

#loading background image,scaling to monitor
bckgrnd=pygame.image.load("TEXTURES/space.jpg")
bckgrnd=pygame.transform.scale(bckgrnd,(glob_width,glob_height))

#starting players parameters
P1_y=glob_height/3
P2_y=glob_height/3
P1_points=0
P2_points=0

#Creating ball and it's basic parameters
meteoroid=ball.Ball(13,3,(glob_width/2),(glob_height/2)) #radius,speed,x,y

#TEXTURING BALL WORK IN PROGRESS
meteoroid_img=pygame.image.load("TEXTURES/moon.png")
meteoroid_img=pygame.transform.scale(meteoroid_img,(400,400))

#point counters
myfont=pygame.font.SysFont('Arial',30)

#game pause boolean
paused = False

#MAIN LOOP
run=True
while run:
	for event in pygame.event.get():
		#exiting game via x in window
		if event.type==pygame.QUIT:
			run=False
		#KEYBOARD USAGE
		if event.type==pygame.KEYDOWN: #KEYUP #key.get_pressed()
			#escape turns game off
			if event.key==pygame.K_ESCAPE:
				run=False
			#p pauses game	
			if event.key==pygame.K_p:
				paused = not paused

		#player movement
		pressed_keys=pygame.key.get_pressed()
		if pressed_keys[pygame.K_w]:
				P1_y-=10				
				if P1_y<0: P1_y=0				
		if pressed_keys[pygame.K_s]:
				P1_y+=10
				if P1_y>((5/6)*glob_height):P1_y=((5/6)*glob_height)
		if pressed_keys[pygame.K_KP8]:
				P2_y-=10
				if P2_y<0: P2_y=0
		if pressed_keys[pygame.K_KP5]:
				P2_y+=10
				if P2_y>((5/6)*glob_height):P2_y=((5/6)*glob_height)


	#pausing game
	if not paused:
		#Ball movement
		meteoroid.move_vertical(glob_height)
		meteoroid.move_horizontal()

		#hitting left racket		
		if meteoroid.x<meteoroid.radius:	
			P2_points=meteoroid.hit_racket(P1_y,glob_height,glob_width,P2_points)				

		#hitting right racket		
		if meteoroid.x>=(glob_width-meteoroid.radius):
			P1_points=meteoroid.hit_racket(P2_y,glob_height,glob_width,P1_points)		

		#background graphics
		screen.blit(bckgrnd,(0,0))
		#TEXTURING BALL WORK IN PROGRESS
		screen.blit(meteoroid_img,((glob_width/2-200,0)))
		#players point counters
		counter_P1=myfont.render(str(P1_points),False,(255,255,255))
		counter_P2=myfont.render(str(P2_points),False,(255,255,255))
		screen.blit(counter_P1,(glob_width/4,0))
		screen.blit(counter_P2,((3/4)*glob_width,0))

		#drawing rackets
		pygame.draw.rect(screen,(255,255,255),(0,P1_y,glob_width/100,glob_height/6))
		pygame.draw.rect(screen,(255,255,255),((99/100)*glob_width,P2_y,glob_width/100,glob_height/6))		
		pygame.draw.circle(screen,(255,255,255),(meteoroid.x,meteoroid.y),meteoroid.radius*2,0)
		pygame.display.update()


#closing screen
pygame.display.flip()