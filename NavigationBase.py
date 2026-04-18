import cv2
from AccidentError import AccidentError
class NavigationBase:
    def __init__(self,robot,camera=None):
        self.robot = robot
        if camera is not None: self.camera = cv2.VideoCapture(camera)
        else: self.camera = None
        self.robot_location = []
        self.servo = robot.init_servo('SERVO1')
        self.servo.rotate_servo(80)
        self.distance_sensor = robot.init_distance_sensor('I2C')
        self.wheel_circumference = 8.22504
        self.turn_radius = 1.5
        self.robot_length = 9
    def check_distance(self):
        return self.distance_sensor.read_inches()
    def emergency_stop(self):
        dist_to_stop = self.robot.get_speed() * (self.wheel_circumference/360)
        if self.distance_sensor.read_inches() < (dist_to_stop*0.75):
            self.robot.stop()
            raise AccidentError("Emergency stop performed.")
    def stop(self,dist_to_stop):
        curr_speed = self.robot.get_speed()
        degrees_until_stop = (dist_to_stop/self.wheel_circumference) * 360
        sec_until_stop = degrees_until_stop / curr_speed
        speed_step = (curr_speed - 10) / sec_until_stop # degrees per second to decrease by - 
        while curr_speed>=10:
            self.slow_down(self,speed_step)
        self.robot.stop()
    def slow_down(self,step=10):
        curr_speed = self.robot.get_speed()
        self.robot.set_speed(curr_speed-step)
    def speed_up(self,step=10):
        curr_speed = self.robot.get_speed()
        self.robot.set_speed(curr_speed+step)
    def shift_left(self):
        self.robot.turn_degrees(-5,blocking=False)
    def shift_right(self):
        self.robot.turn_degrees(5,blocking=False)
    def forward(self,distance):
        self.robot.drive_inches(distance,blocking=False)
    def turn(self,angle):
        self.robot.orbit(angle,self.turn_radius*2.54,blocking=False)
