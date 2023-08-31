
import Serial_1
import Serial_2
import valves
import pygame
import time
import os

#############################################################
global returned_dic
###################
global roll_val
global pitch_val
global yaw_val
global accx
global accy
global accz
global patm
global depth
global uw
global temp
global warning
global front_1
global front_2
global Rear_1
global Rear_2
global up_1
global up_2
global valve1
global valve2
global valve3
global valve4
###################
global ser1_status
global ser2_status
global IMU_status
global Pressure_status
global joystick_status
###################
global joystick

global y1
global x2
global x3
global y3
global AB
global BB
global XB
global YB
global LB
global RB
#############################################################
roll_val=1
pitch_val=2
yaw_val=3
accx=4
accy=5
accz=6
patm=7
depth=8
uw=9
temp=10
warning=11
front_1=12
front_2 = 13
Rear_1 = 14
Rear_2=15
up_1=16
up_2=17
valve1=0
valve2=0
valve3=0
valve4=0

y1=0
x2=0
x3=0
y3=0



AB=0
BB=0
XB=0
YB=0
LB=0
RB=0

###################
ser1_status = False
ser2_status=False
IMU_status= False
Pressure_status= False
joystick_status= False
#############################################################
def map_RPM(value, input_min, input_max, output_min, output_max):
    output_value = (value - input_min) * (output_max - output_min) / (input_max - input_min) + output_min
    RPM = (-1.5933631381478e-5)*(output_value**3) + 0.0720860955611188*(output_value**2) - 98.9465426312546*output_value + 39966.4666710835
    return RPM

def Serial_1_try_connect():
    if Serial_1.Get_status()==False:
        Serial_1.try_connect()

def Serial_2_try_connect():
    if Serial_2.Get_status()==False:
        Serial_2.try_connect()
        

def Serial_1_Get_status():
    return Serial_1.Get_status()

def Serial_2_Get_status():
    return Serial_2.Get_status()

def return_data():
    global returned_dic
    # print(returned_dic)
    return returned_dic

    
#############################################################



# initialize the joystick module
pygame.init()


Serial_1.try_connect()
Serial_2.try_connect()


# loop to continuously read the joystick values and send them to Arduino
def Run():
    #############################################################
    global returned_dic
    ###################
    global roll_val
    global pitch_val
    global yaw_val
    global accx
    global accy
    global accz
    global patm
    global depth
    global uw
    global temp
    global warning
    global front_1
    global front_2
    global Rear_1
    global Rear_2
    global up_1
    global up_2
    global valve1
    global valve2
    global valve3
    global valve4
    ###################
    global ser1_status
    global ser2_status
    global IMU_status
    global Pressure_status
    global joystick_status
    ###################
    global joystick

    global y1
    global x2
    global x3
    global y3
    global AB
    global BB
    global XB
    global YB
    global LB
    global RB
        
    
    #############################################################
    
    try:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        pygame.event.get()
        joystick_status=True
        
    
    except:
        # joystick.quit()
        joystick_status=False

    # print(pygame.joystick.get_count())

    



    if joystick_status==True:
        
   
            y1=joystick.get_axis(1) 
            # print(y1)
            x2=joystick.get_axis(2) 
            x3=joystick.get_axis(4)
            y3=joystick.get_axis(5)

            # print(y1,x2,x3,y3)
            
            AB=joystick.get_button(0)
            BB=joystick.get_button(1)
            XB=joystick.get_button(2)
            YB=joystick.get_button(3)
            LB=joystick.get_button(4)
            RB=joystick.get_button(5)

    if(x3==0 and y3==0):
        joystick_status=False

    



    # read the joystick axes and normalize their values to between 0 and 180
    BUTTON_FORW_BACK= int(y1 * 90 + 90) #0
    BUTTON_LR = int(x2 * 90 + 90) #2
    BUTTON_UP = int(y3 * 90 + 90) #4
    BUTTON_DOWN = int(x3* 90 + 90) #5
    # readRPM values to between 0 and 3075

    print(BUTTON_FORW_BACK,BUTTON_LR,BUTTON_UP,BUTTON_DOWN)

    forw_ = map_RPM(BUTTON_FORW_BACK, 70, 0, 1500, 1850)
    back_ = map_RPM(BUTTON_FORW_BACK, 100, 180, 1500, 1150)
    right = map_RPM(BUTTON_LR, 70, 0, 1500, 1850)
    right_1 = map_RPM(BUTTON_LR, 70, 0, 1500, 1150)
    left = map_RPM(BUTTON_LR, 100, 180, 1500, 1150)
    left_1 = map_RPM(BUTTON_LR, 100, 180, 1500, 1850)
    UP = map_RPM(BUTTON_UP, 90, 170, 1500, 1850)
    DOWN = map_RPM(BUTTON_DOWN, 90, 170, 1500, 1150)
    
    if (BUTTON_FORW_BACK < 70 and not (BUTTON_LR > 100 or BUTTON_LR < 70) and not BUTTON_DOWN > 0 and not BUTTON_UP > 0):
        front_1=forw_
        front_2 = forw_
        Rear_1 = forw_
        Rear_2=forw_
        up_1=0
        up_2=0
        
    elif (BUTTON_FORW_BACK > 100 and not (BUTTON_LR > 100 or BUTTON_LR < 80) and not BUTTON_DOWN > 0 and not BUTTON_UP > 0):
        front_1=back_
        front_2 = back_
        Rear_1 = back_
        Rear_2=back_
        up_1=0
        up_2=0
    elif (BUTTON_LR < 70 and not (BUTTON_FORW_BACK > 100 or BUTTON_FORW_BACK < 70) and not BUTTON_DOWN > 0 and not BUTTON_UP > 0):
        front_1=right
        front_2 = right
        Rear_1 = right_1
        Rear_2=right_1
        up_1=0
        up_2=0
    elif (BUTTON_LR > 100 and not (BUTTON_FORW_BACK > 100 or BUTTON_FORW_BACK < 70) and not BUTTON_DOWN > 0 and not BUTTON_UP > 0):
        front_1=left
        front_2 = left
        Rear_1 = left_1
        Rear_2=left_1
        up_1=0
        up_2=0
    elif (BUTTON_DOWN > 0 and not BUTTON_UP > 0 and not (BUTTON_FORW_BACK > 100 or BUTTON_FORW_BACK < 70) and not (BUTTON_LR > 100 or BUTTON_LR < 70)):
        up_1=DOWN
        up_2=DOWN
    elif (BUTTON_UP > 0 and not BUTTON_DOWN > 0 and not (BUTTON_FORW_BACK > 100 or BUTTON_FORW_BACK < 70) and not (BUTTON_LR > 100 or BUTTON_LR < 70)):
        up_1=UP
        up_2=UP
    else:
        front_1=0
        front_2 = 0
        Rear_1 = 0
        Rear_2=0
        up_1=0
        up_2=0
    

    data_motors="#"+str(BUTTON_FORW_BACK)+"|"+str(BUTTON_LR)+"|"+str(BUTTON_UP)+"|"+str(BUTTON_DOWN)+"|"+str((time.time()*20)%2)+"|"+str(int(joystick_status))+"*"+'\n'
    Serial_2.write(data_motors)   

    #print()

    data_valves="#"+str(int(valve1))+"|"+str(int(valve2))+"|"+str(int(valve3))+"|"+str(int(valve4))+"*"+'\n'
    Serial_1.write(data_valves)
    


    Serial_1.Get_Data_With_Format('#', '|', '*')

    #print(Serial_1.Get_Var(8))

    patm=Serial_1.Get_Var(1)/1000
    uw = Serial_1.Get_Var(2)/1000
    depth = Serial_1.Get_Var(3)/100
    temp=Serial_1.Get_Var(4)/10

    accx=Serial_1.Get_Var(5)/98
    accy=Serial_1.Get_Var(6)/98
    accz=Serial_1.Get_Var(7)/98

    pitch_val=Serial_1.Get_Var(8)
    roll_val=Serial_1.Get_Var(9)
    yaw_val=Serial_1.Get_Var(10)

   
    ser1_status=Serial_1.Get_status()
    ser2_status=Serial_2.Get_status()

    valve1=valves.process(AB,BB,XB,YB,LB,RB)[0]
    valve2=valves.process(AB,BB,XB,YB,LB,RB)[1]
    valve3=valves.process(AB,BB,XB,YB,LB,RB)[2]
    valve4=valves.process(AB,BB,XB,YB,LB,RB)[3]

    if ser1_status == True:
        Pressure_status=Serial_1.Get_Var(11)
        IMU_status=Serial_1.Get_Var(12)
    else:
        Pressure_status=0
        IMU_status=0




    returned_dic={'Roll': roll_val , 
                  'Pitch': pitch_val,
                  'Yaw': yaw_val,
                  'Accelx': round(accx,3) ,
                  'Accely': round(accy,3),
                  'Accelz': round(accz,3),
                  'patm': patm,
                  'depth': depth,
                  'underwater': uw,
                  'temp': temp ,
                  'ser1_status' : ser1_status , 
                  'ser2_status' :ser2_status ,
                  'IMU_status' : IMU_status ,
                  'Pressure_status' : Pressure_status,
                  'joystick_status' : joystick_status,
                  'front_1' : int(front_1) ,
                  'front_2' : int(front_2) ,
                  'Rear_1' : int(Rear_1) ,
                  'Rear_2' : int(Rear_2) ,  
                  'up_1' : int(up_1) ,
                  'up_2' : int(up_2) ,                                           
                  'valve1' : bool(valve1) ,                                           
                  'valve2' : bool(valve2) ,                                           
                  'valve3' : bool(valve3) ,                                           
                  'valve4' : bool(valve4) ,                                                                                                       
                  }


    if Serial_1.Get_status()==False:
        Serial_1_try_connect()

    if Serial_2.Get_status()==False:
        Serial_2_try_connect()

    os.system('cls' if os.name=='nt' else 'clear')
    print(return_data())

    # print(valve1,valve2,valve3,valve4)
  
    time.sleep(0.01)

while True:
    Run()


    '''
    To write:
    Serial_x.write(data)  for example : "#1|2|3*"

    To read:
    Serial_x.Get_Data_With_Format(header, delimiter, terminator)  for example: Serial_1.Get_Data_With_Format('#', '|', '*')
    Serial_1.Get_Var(index) for example: Serial_1.Get_Var(2)



    
    # Serial_1.write(data_valves)   
    # Serial_1.Get_Data_With_Format('#', '|', '*')
    
    # pressure_abs=Serial_1.Get_Var(1)
    # pressure_sealevel = Serial_1.Get_Var(2)
    # DEPTH = Serial_1.Get_Var(3)
    # TEMPERATURE=Serial_1.Get_Var(4)
    # acc_x=Serial_1.Get_Var(5)
    # acc_y=Serial_1.Get_Var(6)
    # acc_z=Serial_1.Get_Var(7)
    # pitch=Serial_1.Get_Var(8)
    # roll=Serial_1.Get_Var(9)
    # yaw=Serial_1.Get_Var(10)
    #FLAG_bmp=Serial_1.Get_Var(11)
    #FLAG_MPU=Serial_1.Get_Var(12)



    # print(pressure_abs ,pressure_sealevel,DEPTH,TEMPERATURE,acc_x,acc_y,acc_z,pitch,roll,yaw)
    

    '''

