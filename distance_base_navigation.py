
def check_ahead(nav_base):
    if nav_base.check_distance() < nav_base.robot_length:
        nav_base.slow_down()
    if nav_base.check_distance() > nav_base.robot_length*2 and nav_base.robot.get_speed() < 300:
        nav_base.speed_up()
def check_right(nav_base):
    nav_base.servo.rotate_servo(120)
    #if nav_base.check_distance() < nav_base.robot_length:
    #    nav_base.slow_down()
    #if nav_base.check_distance() > nav_base.robot_length*2 and nav_base.robot.get_speed() < 300:
    #    nav_base.speed_up()
    nav_base.servo.rotate_servo(80)
def check_right(nav_base):
    nav_base.servo.rotate_servo(40)
    #if nav_base.check_distance() < nav_base.robot_length:
    #    nav_base.slow_down()
    #if nav_base.check_distance() > nav_base.robot_length*2 and nav_base.robot.get_speed() < 300:
    #    nav_base.speed_up()
    nav_base.servo.rotate_servo(80)
def run_navigation(nav_base):
    return