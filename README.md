# pi_extruder

resberry Pi 5 drived linear motion module as extruder


## environment setup
```
conda activate gzero_env
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
```


## commands
默认状态限位未被触发时，为高电平，输出为3.3v信号；当限位触发时，信号线输出电压为低电压(小于1.5v)
监控上下限开关的状态，打印GPIO状态
```
python print_gpio_in.py
```
电机运动测试
(gzero_env) xl@raspberrypi:~/Desktop/pi_extruder$

```
python gpiozero_control_unit_test.py
```
旋转圈数:
motor.move_revolutions(6, delay=0.0002)
旋转角度:
motor.move_degrees(90, delay=0.001)


## tkinter-学习笔记

#### 介绍
tkinter学习笔记
学习过程的记录，记录了学习中的源码

#### 软件架构
软件架构说明


#### 安装教程

1.  xxxx
2.  xxxx
3.  xxxx

#### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request