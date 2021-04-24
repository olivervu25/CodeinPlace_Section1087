from karel.stanfordkarel import *

# File: HospitalKarel.py
# -----------------------------
# Here is a place to program your Section problem

def main():
    while front_is_clear(): 
        if beepers_present(): 
            build_hospital() 
            turn_left()
        if front_is_clear():
            move()

def build_hospital(): 
    turn_left()
    put_2_beepers() 
    turn_right()
    move() 
    turn_right() 
    put_beeper()
    put_2_beepers() 

def put_2_beepers(): 
    for i in range(2): 
        move()
        put_beeper()  

def turn_right(): 
    for i in range(3): 
        turn_left() 

if __name__ == '__main__':
    run_karel_program('HospitalKarel2.w')