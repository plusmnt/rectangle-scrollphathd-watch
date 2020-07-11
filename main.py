import time
import scrollphathd
from datetime import datetime


# get location of the light in 17*7 matrix
# sx: digit x location
# n: number to draw (0-12)
def get_loc(sx,n):

	# start from zero as 12
	if n ==12:
		n=0
	if n ==0 or n == 6:
		y=1
		if n ==6:
			y =5
		return sx+1,y
	if n <= 5:
		y =n
		x=sx+2
		return x,y
	if n >=7:
		y =12-n
		x =sx
		return x,y

# Draw the surface and the time
def show_time():
	# get current device time
	now=datetime.now()

	#Draw 3 rectangles background
	#sq: will give 1, 7, 13 as x starting point
	for sq in range(1, 15, 6):
		for sx in range(sq,sq+3):
			for sy in range(1,6):
				if sx ==sq+1 :
					if sy !=1 and sy !=5:
						continue
				scrollphathd.set_pixel(sx,sy,0.13)
	#Draw ':'
	scrollphathd.set_pixel(5,2,0.13)
	scrollphathd.set_pixel(5,4,0.13)
	scrollphathd.set_pixel(11,2,0.13)
	scrollphathd.set_pixel(11,4,0.13)
	#set the time
	#print("Now:",now)
	# divide by 5 and add 0.5 to show the upper value, 
	#e.g. 33,34 = 35 instead of 30
	second_12_base=int(now.second/5+0.5)
	second_x,second_y=get_loc(13,second_12_base)
	scrollphathd.set_pixel(second_x,second_y,0.5)

	minute_12_base=int(now.minute/5+0.5)
	minute_x,minute_y=get_loc(7,minute_12_base)
	scrollphathd.set_pixel(minute_x,minute_y,0.5)

	hour=now.hour
	if hour >12: #convert from 24 to 12 hour
		hour=hour-12
	hour_x,hour_y=get_loc(1,hour)
	scrollphathd.set_pixel(hour_x,hour_y,0.5)

	scrollphathd.show()



print("""
watch started
     
 000   000   000
 0 0 0 0 0 0 0 0
 0 0   0 0   0 0
 0 0 0 0 0 0 0 0
 000   000   000
 
Press ctrl + c to exit.

""")

while True:
	show_time()
	time.sleep(1)
