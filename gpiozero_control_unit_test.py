from gpiozero_deepseek_DigitalOutputDevice import StepperMotor

import enum
 
class Sign(enum.IntEnum):
    EXTRUDE = 1
    BACK = -1



def moving(rotate,delay,direction=1):

    # 旋转6圈（快速）挤出方向
    rotates=direction*rotate
    motor.move_revolutions(rotates, delay)  
    # 旋转6圈（快速）挤出方向
    # motor.move_revolutions(6, delay=0.0002)
    

    # 顺时针旋转90度（中等速度）
    # motor.move_degrees(90, delay=0.001)
    # 顺时针旋转360度（快速度）
    # motor.move_degrees(360, delay=0.0005)
    # # 逆时针旋转1圈（快速）
    # motor.move_revolutions(1, delay=0.0005)

    # # 逆时针旋转1圈（快速）
    # motor.move_revolutions(-1, delay=0.0005)

    # 旋转3圈（快速） 挤出方向
    # motor.move_revolutions(3, delay=0.001)

    # # 旋转3圈（快速）后退方向
    # motor.move_revolutions(-3, delay=0.001)


    # # 旋转3圈（快速）后退方向
    # motor.move_revolutions(-3, delay=0.0002)

    # # 逆时针旋转3圈（快速）
    # motor.move_revolutions(3, delay=0.00015)

    # # 逆时针旋转3圈（快速）
    # motor.move_revolutions(-3, delay=0.00015)


    # # 逆时针旋转1圈（快速）
    # motor.move_revolutions(1, delay=0.0002)

    # # 逆时针旋转1圈（快速）
    # motor.move_revolutions(-1, delay=0.0002)


    # # 逆时针旋转1圈（快速）
    # motor.move_revolutions(1, delay=0.0001)

    # # 逆时针旋转1圈（快速）
    # motor.move_revolutions(-1, delay=0.0001)



    # # 精确移动800步（慢速）
    # motor.move_steps(800, delay=0.002)

    print(f"当前位置: {motor.get_position()}步")
    motor.set_position(0)  # 重置位置

if __name__ == "__main__":
    print("start moving")
    # 初始化电机
    motor = StepperMotor(dir_pin=20, step_pin=21, spr=1600)
    direction = Sign.EXTRUDE
    # direction = Sign.BACK
    rotate = 1
    delay = 0.0002
    moving(rotate,delay,direction)