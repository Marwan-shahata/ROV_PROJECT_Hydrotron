import time
global start_time_AB
global flag_AB
global start_time_BB
global flag_BB
global start_time_XB
global flag_XB
global start_time_YB
global flag_YB
global start_time_LB
global flag_LB
global start_time_RB
global flag_RB

global valve1
global valve2
global valve3
global valve4



valve1=False
valve2=False
valve3=False
valve4=False


def process(AB,BB,XB,YB,LB,RB):
    global start_time_AB
    global flag_AB
    global start_time_BB
    global flag_BB
    global start_time_XB
    global flag_XB
    global start_time_YB
    global flag_YB
    global start_time_LB
    global flag_LB
    global start_time_RB
    global flag_RB

    global valve1
    global valve2
    global valve3
    global valve4
#########################################################################################
################################ YB valve3 Toggle #######################################
    if  (YB==True) and (time.time()-start_time_YB>=0.25) and (flag_YB == True):
        valve3= not valve3       
        flag_YB=False

    if YB==False:
        start_time_YB = time.time()
        flag_YB=True
#########################################################################################
################################ XB valve4 Toggle #######################################
    if (XB==True) and (time.time()-start_time_XB>=0.25) and (flag_XB == True):
        valve4= not valve4       
        flag_XB=False

    if XB==False:
        start_time_XB = time.time()
        flag_XB=True
#########################################################################################

#######################################################################################################
################################  valve2 (BB Latch/ AB UnLatch) #######################################
    if  (BB==True) and (AB==False) and  (time.time()-start_time_BB>=0.25) :
        valve2= False
    
    if BB==False:
        start_time_BB = time.time()
        flag_BB=True

    if (AB==True) and (BB==False) and (time.time()-start_time_AB>=0.25):
        valve2=True 
        start_time_AB = time.time()

    if AB==False:
        start_time_AB = time.time()
        flag_AB=True
 
#######################################################################################################
################################  valve1 (RB Latch/ LB UnLatch) #######################################
    if  (RB==True) and (LB==False) and  (time.time()-start_time_RB>=0.25) :
        valve1= True
    
    if RB==False:
        start_time_RB = time.time()
        flag_RB=True

    if (LB==True) and (RB==False) and  (time.time()-start_time_LB>=0.25):
        valve1=False 
        start_time_LB = time.time()

    if LB==False:
        start_time_LB = time.time()
        flag_LB=True
       
    # Return the computed values as a tuple
    return valve1,valve2,valve3,valve4