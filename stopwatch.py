# template for "Stopwatch: The Game"
import simplegui


# define global variables
interval = 100
counter = 0 
position = [100, 100]
width = 200
height = 100
stopper = False
success_score = 0
total_score = 0
a= 0
b = 0
c = 0
d = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global a,b,c,d
    a = t/600
    b = ((t //10) % 60) // 10
    c = ((t //10) % 60) % 10
    d = (t  % 10)
    return str(a) + ":" + str(b) + str(c) +"." + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def resetter():
    global counter, stopper
    counter = 0
    stopper = False
    total_score = 0
    success_score = 0

def starter():
    timer.start()
    global stopper
    timer.start()
    stopper = False
    
    
def stop_it():
    global d, total_score, success_score, stopper
    if stopper == False:
        total_score += 1
        if d == 0:
            success_score +=1
    stopper = True
    timer.stop()
    
    
    
    
# define event handler for timer with 0.1 sec interval

def tick():
    global counter
    counter += 1
   
    #print(counter)

# define draw handler

def draw(canvas):
    global counter
    global total_score
    canvas.draw_text((format(counter)), position, 36, "Red")
    canvas.draw_text(str(success_score) + "/" + str(total_score), [170, 20], 18, "White" )
    
# create frame
frame = simplegui.create_frame("Stopwatch", width, height)

# register event handlers

timer = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw)

#event handlers for buttons:
frame.add_button("Start", starter, 100)
frame.add_button("Stop", stop_it, 100)
frame.add_button("reset", resetter, 100)

# start frame
frame.start()



