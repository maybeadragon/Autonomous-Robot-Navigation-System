import time
def check_ahead(nav_base):
    if nav_base.check_distance() < nav_base.robot_length:
        nav_base.slow_down()
    if nav_base.check_distance() > nav_base.robot_length*2 and nav_base.robot.get_speed() < 300:
        nav_base.speed_up()
def check_right(nav_base):
    nav_base.servo.rotate_servo(70)
    #if nav_base.check_distance() < nav_base.robot_length*0.25:
        #nav_base.shift_left()
    #nav_base.servo.rotate_servo(85)
def check_left(nav_base):
    nav_base.servo.rotate_servo(100)
    #if nav_base.check_distance() < nav_base.robot_length*0.25:
        #nav_base.shift_right()
    #nav_base.servo.rotate_servo(85)
def run_navigation(nav_base):
    while True:
        #check_ahead(nav_base)
        #time.sleep(0.25)
        #if nav_base.nav_done: 
        #    break
        check_right(nav_base)
        time.sleep(1)
        check_left(nav_base)
        time.sleep(1)
        nav_base.servo.rotate_servo(85)
        break
    