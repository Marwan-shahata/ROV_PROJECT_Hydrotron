# Serial Motor

import serial
global  ser2_status,ser2


max_get_data = 12
var_res_str = [""] * (max_get_data + 1)
var_res_int = [0] * (max_get_data + 1)
cont = 0
var = 0
ser2_status=False


port_ser2_name = "COM5" # Serial Motor



# Example usage:
def try_connect():
    global ser2,ser2_status
    if ser2_status==False:
        # Port is available, connect to it here
        try:
            ser2 = serial.Serial(port_ser2_name, baudrate=9600, timeout=1)
            #ser2_status=True
        except:
            ser2_status=False
            # print("canot connect")
    


def clear_string():
    global var_res_str
    var_res_str = [""] * (max_get_data + 1)

def Get_Data_With_Format(header, delimiter, terminator):
    global cont, var, var_res_str, var_res_int,ser2_status,ser2
    try:
        ser2_status=True
        
        while ser2.in_waiting > 0:
            c = ser2.read().decode() # read one byte from serial buffer
            if c == header:
                cont = 1
                var = 1
                clear_string()
            elif c == delimiter:
                var += 1
            elif cont == 1 and c != header and c != delimiter and c != terminator:
                var_res_str[var] += c
            elif cont == 1 and c == terminator:
                for i in range(1, var + 1):
                    var_res_int[i] = int(var_res_str[i])
                clear_string()
                cont = 0
                var = 0
    except:
        #print("Cheek ser2")
        ser2_status=False

def Get_Var(index):
    return var_res_int[index]

def write(data):
    global ser2_status,ser2
    try:
        ser2.write(data.encode())
        ser2_status=True
    except:
        ser2_status=False
        #print("Cheek ser2")

def Get_status():
    global ser2_status
    return ser2_status


                
