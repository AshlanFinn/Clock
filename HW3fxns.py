import turtle
import time
import sys

def turtle_init(color,bgcolor,pensize, speed, shape):
    '''
    Creates a screen and turtle object.
    @param (color,bgcolor,pensize,speed,shape) -- input turtle characteristics
    @return, (turtle,window) 
    '''
    window = turtle.Screen()
    window.bgcolor(bgcolor)
    turtle.mode('logo')
    
    terrapin = turtle.Turtle()
    terrapin.ht()
    terrapin.color(color)
    terrapin.pensize(pensize)
    terrapin.shape(shape)
    terrapin.speed(speed)
    terrapin.penup()
    
    return (terrapin,window)

def draw_clock(terrapin,radius,pos_neg,message):
    
    terrapin.forward(radius)
    terrapin.left(90)
    terrapin.pendown()
    terrapin.pensize(2)
    terrapin.circle(radius,None,12)
    terrapin.penup()
    terrapin.home()

    terrapin.forward(radius-100)
    terrapin.left(90)
    terrapin.pendown()
    terrapin.circle(radius-100)
    terrapin.penup()
    terrapin.pensize(3)
    terrapin.home()
    
    if pos_neg == '+':
        numbers = range(1,13)
    else:
        numbers = range(-12,0)
        message = message[::-1].swapcase()
        
    for num in numbers:
        terrapin.right(num * 30)
        terrapin.forward(radius-100)
        terrapin.dot(10)
        terrapin.forward(50)
        terrapin.write(num,False,'center',('Courier',35,'normal'))
        terrapin.home()

    terrapin.forward(radius)
    terrapin.write(message,False,'center',('Courier',30,'normal'))
    terrapin.home()
        
    
def clock_hands(terrapin, time, disp_hh, disp_mm, radius):
    """
    Draws hour and minute hands corresponding to a set of time parameters
    @param 1: terrapin_, a turtle
    @param 2: time_, list of time parameters
    @param 3: radius, length of minute hand
    @return none
    """
    time = list(time)
    mm = (time[4] + disp_mm) % 60
    hh = (time[3] + disp_hh + (time[4] + disp_mm)/60) % 12 
    terrapin.pendown()
    terrapin.right(hh * 30)
    terrapin.forward(radius/2)
    terrapin.stamp()
    terrapin.home()
    
    terrapin.right(mm*6)
    terrapin.forward(radius-5)
    terrapin.stamp()
    terrapin.home()
    terrapin.penup()

def validate_text(response, values, is_case_sensitive):
    '''
    Validate a text response
    '''
    if is_case_sensitive and response in values:
        return True
        
    if not is_case_sensitive:
        response = response.lower()
        values = [x.lower() for x in values]
        if response in values:
            return True
    return False


def convert_validate_int(s):
    '''
    converts a string to a int if possible, and if not returns None:
    @params s -- input string
    @returns, int or None

    '''
    if len(s) >= 1 and s[0] == '-':
        if s[1:].isdigit():
            return int(s)
    elif s.isdigit():
        return int(s)
    else:
        return None #s does not represent any kind of int




##DEBUG##

#DEBUG = True
#while DEBUG:
#    (ruth,canvas) = turtle_init("purple", "white", 3,0, "classic" )
# 
#    joe = ruth.clone()
 #   time_params = time.localtime()
#    disp = 0
 #   radius = 200
#    clock_hands(ruth, time_params, 0,0, radius  )
#    draw_clock(joe,radius+100,'+','Hello World')
 #   break


    
