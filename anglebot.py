from turtle_move import TurtleMove
reached_end_goal = False

# A variable to keep track of whether we are heading away from the start point.
heading = 0
# To 
snag_counter = 0 
collisions = []

bob = TurtleMove()
right(degrees=45)
straight_line_counter = 0
while not reached_end_goal:
    if straight_line_counter > 10:
        snag counter += 1
        bob.backward(2)
        bob.left(degrees=45)
    elif not in_collision():
        bob.forward(1)
        straight_line_counter += 1
        continue
    else:
        straight_line_counter = 0
        collison_point = bob.get_collision()
        collisions.append(collision_point)
        bob.backward(2)
        if collision_point = 1:
            bob.left(degrees=90)
            heading += 90
        if collision_point = 2:
            bob.right(degrees=90)
            heading += -90
        if collision_point = 3:
            bob.left(degrees=45)
            heading += 45

    
    