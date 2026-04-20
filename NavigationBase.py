import cv2
import time
from AccidentError import AccidentError
class NavigationBase:
    def __init__(self,robot,camera=None):
        self.robot = robot
        if camera is not None: self.camera = cv2.VideoCapture(camera)
        else: self.camera = None
        self.robot_location = []
        self.servo = robot.init_servo('SERVO1')
        self.servo.rotate_servo(85)
        self.distance_sensor = robot.init_distance_sensor('AD2')
        self.wheel_circumference = 8.22504
        self.turn_radius = 1.5
        self.robot_length = 9
        self.nav_done = False
        self.dist_left = 0
        self.robot.steer(100,100)
        self.robot.set_speed(300)
        self.obstacle_count = 0
        self.accidents = 0
    def check_distance(self):
        return self.distance_sensor.read_inches()
    def emergency_stop(self):
        dist_to_stop = self.robot.get_speed() * (self.wheel_circumference/360)
        if self.check_distance() < (dist_to_stop*0.25):
            self.robot.stop()
            self.accidents += 1
            raise AccidentError("Emergency stop performed.")
    def stop(self,dist_to_stop=0):
        #curr_speed = self.robot.get_speed()
        #degrees_until_stop = (dist_to_stop/self.wheel_circumference) * 360
        #sec_until_stop = degrees_until_stop / curr_speed
        #speed_step = int((curr_speed - 10) / sec_until_stop) # degrees per second to decrease by - 
        #while curr_speed>=10:
        #    self.slow_down(speed_step)
        #    time.sleep(0.9)
        self.robot.stop()
    def slow_down(self,step=125):
        curr_speed = self.robot.get_speed()
        if curr_speed-step <= 0: 
            self.robot.set_speed(0)
        else: self.robot.set_speed(curr_speed-step)
    def speed_up(self,step=50):
        self.robot.steer(100,100)
        curr_speed = self.robot.get_speed()
        if curr_speed < 300: self.robot.set_speed(curr_speed+step)
    def shift_left(self):
        self.robot.steer(90,100)
        time.sleep(0.1)
        self.robot.steer(100,100)
    def shift_right(self):
        self.robot.steer(100,90)
        time.sleep(0.1)
        self.robot.steer(100,100)
    def forward(self,distance):
        self.dist_left = distance
        self.robot.drive_inches(distance,blocking=False)
    def update_distance(self, distance):
        self.dist_left = distance
    def turn(self,angle):
        self.robot.orbit(angle,self.turn_radius*2.54,blocking=False)
    def nav_finished(self):
        self.nav_done = True
