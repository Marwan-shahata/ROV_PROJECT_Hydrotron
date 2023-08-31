# Serial Sensor / Valves

import serial
global  ser1_status,ser1


max_get_data = 12
var_res_str = [""] * (max_get_data + 1)
var_res_int = [0] * (max_get_data + 1)
cont = 0
var = 0
ser1_status=False


port_ser1_name = "COM3" # Serial Sensor / Valves



# Example usage:
def try_connect():
    global ser1,ser1_status
    if ser1_status==False:
        # Port is available, connect to it here
        try:
            ser1 = serial.Serial(port_ser1_name, baudrate=9600, timeout=1)
            #ser1_status=True
        except:
            ser1_status=False
            # print("canot connect")
    


def clear_string():
    global var_res_str
    var_res_str = [""] * (max_get_data + 1)

def Get_Data_With_Format(header, delimiter, terminator):
    global cont, var, var_res_str, var_res_int,ser1_status,ser1
    try:
        ser1_status=True
        
        while ser1.in_waiting > 0:
            c = ser1.read().decode() # read one byte from serial buffer
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
        #print("Cheek ser1")
        ser1_status=False

def Get_Var(index):
    return var_res_int[index]

def write(data):
    global ser1_status,ser1
    try:
        ser1.write(data.encode())
        ser1_status=True
    except:
        ser1_status=False
        #print("Cheek ser1")

def Get_status():
    global ser1_status
    return ser1_status


                
