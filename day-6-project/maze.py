#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turnRight():
    turn_left()
    turn_left()
    turn_left()

def turnLeft():
    turn_left()

moves = 0
#  front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
while at_goal() != True:
    if wall_on_right() == True and front_is_clear() == True:
        move()
    elif right_is_clear() == True and wall_in_front() == True:
        turnRight()
        if right_is_clear() == True and front_is_clear() == True:
            move()
            if wall_on_right() == True and front_is_clear() == True:
                move()
            elif right_is_clear() == True and front_is_clear() == True:
                turnRight()
                move()
    elif wall_on_right() == True and wall_in_front() == True:
        turnLeft()
    elif right_is_clear() == True and front_is_clear() == True and is_facing_north() == True:
        move()
    elif right_is_clear() == True and front_is_clear() == True and is_facing_north() != True:
        turnRight()

