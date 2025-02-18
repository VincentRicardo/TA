import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Int32
import math
from adafruit_servokit import ServoKit
import time

kit1 = ServoKit(channels=16, address=0x41)
kit2 = ServoKit(channels=16, address=0x40)

def wait(waktu):
    flag = True
    myTime = time.time()
    while flag == True:
        currentTime = time.time()
        if currentTime - myTime < waktu:
            flag = True
        elif currentTime - myTime >= waktu:
            flag = False

delay = 0.2

class MyNode(Node):
    def __init__(self):
        super().__init__("tripod_gait_node")
        self.subscriber_angle = self.create_subscription(Int32MultiArray, "/tripod_angle_", self.move, 1)

    def move(self, message = Int32MultiArray):
        #femur 1 3 5 ngangkat
        kit1.servo[7].angle = 170 #femur1
        kit1.servo[6].angle = 180 #tibia1
        kit1.servo[1].angle = 170 #femur3
        kit1.servo[0].angle = 180 #tibia3
        kit2.servo[11].angle = 10 #femur5
        kit2.servo[12].angle = 0 #tibia5
        wait(delay)

        #coxa 1 3 5 maju
        kit1.servo[8].angle = 90 + message.data[3] #coxa1
        kit1.servo[2].angle = 90 + message.data[6] #coxa3
        kit2.servo[10].angle = 90 - message.data[0+9] #coxa5
        wait(delay)
        

        #femur 1 3 5 turun dan tibia turun sekalian adjust ngambil kaki
        kit1.servo[6].angle = message.data[12+9] - message.data[5] #tibia1
        kit1.servo[0].angle = message.data[14+9] - message.data[8] #tibia3
        kit2.servo[12].angle = ((180 - message.data[10+9]) + message.data[2+9]) #tibia5
        kit1.servo[7].angle = message.data[11+9] + message.data[4] #femur1
        kit1.servo[1].angle = message.data[13+9] + message.data[7] #femur3
        kit2.servo[11].angle = ((180 - message.data[9+9] )- message.data[1+9]) #femur5
        wait(delay)
        
        #coxa femur tibia 1 3 5 balik ke posisi awal
        kit1.servo[8].angle = 90 #coxa1
        kit1.servo[7].angle = message.data[11+9] #femur1
        kit1.servo[6].angle = message.data[12+9] #tibia1

        kit1.servo[2].angle = 90 #coxa3
        kit1.servo[1].angle = message.data[13+9] #femur3
        kit1.servo[0].angle = message.data[14+9] #tibia3

        kit2.servo[10].angle = 90 #coxa5
        kit2.servo[11].angle = 180 - message.data[9+9] #femur5
        kit2.servo[12].angle = 180 - message.data[10+9] #tibia5

        #femur 2 4 6 ngangkat
        kit1.servo[4].angle = 170 #femur2
        kit1.servo[3].angle = 180 #tibia2
        kit2.servo[14].angle = 10 #femur4
        kit2.servo[15].angle = 0 #tibia4
        kit2.servo[8].angle = 10 #femur6
        kit2.servo[9].angle = 0 #tibia6
        wait(delay)

        #coxa 2 4 6 maju
        kit1.servo[5].angle = 90 + message.data[0] #coxa2
        kit2.servo[13].angle = 90 - message.data[6+9] #coxa4
        kit2.servo[7].angle = 90 - message.data[3+9] #coxa6
        wait(delay)

        #femur 2 4 6 turun dan tibia turun sekalian adjust ngambil kaki
        kit1.servo[3].angle = message.data[10+9] - message.data[2] #tibia2
        kit2.servo[15].angle = ((180 - message.data[14+9]) + message.data[8+9]) #tibia4
        kit2.servo[9].angle = ((180 - message.data[12+9]) + message.data[5+9]) #tibia6
        kit1.servo[4].angle = message.data[9+9] + message.data[1] #femur2
        kit2.servo[14].angle = ((180 - message.data[13+9]) - message.data[7+9]) #femur4
        kit2.servo[8].angle = ((180 - message.data[11+9]) - message.data[4+9]) #femur6
        wait(delay)

        #coxa femur tibia 2 4 6 balik ke poisi awal
        kit1.servo[5].angle = 90 #coxa2
        kit1.servo[4].angle = message.data[9+9] #femur2
        kit1.servo[3].angle = message.data[10+9] #tibia2

        kit2.servo[13].angle = 90 #coxa4
        kit2.servo[14].angle = 180 - message.data[13+9] #femur4
        kit2.servo[15].angle = 180 - message.data[14+9] #tibia4

        kit2.servo[7].angle = 90 #coxa6
        kit2.servo[8].angle = 180 - message.data[11+9] #femur6
        kit2.servo[9].angle = 180 - message.data[12+9] #tibia6


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

