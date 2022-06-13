import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time
def motor1_forward():
    # define GPIO pins Motor1
    direction_1 = 22  # Direction (DIR) GPIO Pin
    step_1 = 23  # Step GPIO Pin
    EN_pin_1 = 24  # enable pin (LOW to enable)
    # Declare a instance of class pass GPIO pins numbers and the motor_1 type
    mymotor_1test = RpiMotorLib.A4988Nema(direction_1, step_1, (21,21,21), "DRV8825")
    GPIO.setup(EN_pin_1, GPIO.OUT)  # set enable pin1 as output

    # Actual motor1 control
    ###########################
    #
    GPIO.output(EN_pin_1, GPIO.LOW)  # pull enable to low to enable motor
    mymotor_1test.motor_go(False,  # True=Clockwise, False=Counter-Clockwise
                           "Full",  # Step type (Full,Half,1/4,1/8,1/16,1/32)
                           200,  # number of steps
                           .0005,  # step delay [sec]
                           False,  # True = print verbose output
                           .05)  # initial delay [sec]
    GPIO.cleanup()  # clear GPIO allocations after run


def motor2_forward():
    #define GPIO pins Motor2
    direction_2 = 5 # Direction (DIR) GPIO Pin
    step_2 = 6 # Step GPIO Pin
    EN_pin_2 = 13 # enable pin (LOW to enable)


    # Declare a instance of class pass GPIO pins numbers and the motor_2 type
    mymotor_2test = RpiMotorLib.A4988Nema(direction_2, step_2, (21,21,21), "DRV8825")

    GPIO.setup(EN_pin_2,GPIO.OUT) # set enable pin2 as output

    # Actual motor2 control
    ###########################
    #
    GPIO.output(EN_pin_2,GPIO.LOW) # pull enable to low to enable motor
    mymotor_2test.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                         "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                         200, # number of steps
                         .0005, # step delay [sec]
                         False, # True = print verbose output
                         .05) # initial delay [sec]

    GPIO.cleanup()  # clear GPIO allocations after run