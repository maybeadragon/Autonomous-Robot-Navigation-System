def check_ahead(nav_base):
    if nav_base.check_distance() < nav_base.robot_length:
        nav_base.slow_down()
    if nav_base.check_distance() > nav_base.robot_length*2 and nav_base.robot.get_speed() < 300:
        nav_base.speed_up()
    return
def run_navigation(nav_base):
    return