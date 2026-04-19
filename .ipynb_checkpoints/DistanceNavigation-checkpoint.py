import time
from NavigationBase import NavigationBase
class DistanceNavigation(NavigationBase):
    def __init__(self,robot,camera=None):
        super().__init__(robot,camera)
        self.nav_type = "distance"
        self.slowing = False
        self.left = False
        self.right = False
    def check_ahead(self):
        if self.check_distance() <= self.robot_length*2:
            self.slow_down()
            self.slowing = True
        if self.check_distance() <= self.robot_length*2:
            self.stop(self.check_distance())
            self.slowing = True
        if self.check_distance() > self.robot_length*2 and self.robot.get_speed() < 300:
            self.speed_up()
            self.slowing = False
    def check_right(self):
        self.servo.rotate_servo(50)
        if self.check_distance() < self.robot_length*0.5:
            self.shift_left()
            self.left = True
        self.left = False
        #nav_base.servo.rotate_servo(85)
    def check_left(self):
        self.servo.rotate_servo(100)
        if self.check_distance() < self.robot_length*0.5:
            self.shift_right()
            self.right = True
        self.right = False
        #self.servo.rotate_servo(85)
    def run_navigation(self):
        speed = self.robot.get_speed()
        if not self.left or not self.right:
            self.check_ahead()
            self.emergency_stop()
            time.sleep(0.01)
        if not self.slowing:
            if not self.right:
                self.check_right()
                self.emergency_stop()
                time.sleep(0.01)
            if not self.left:
                self.check_left()
                self.emergency_stop()
                time.sleep(0.01)
        self.servo.rotate_servo(85)
        self.robot.set_speed(speed)
    
