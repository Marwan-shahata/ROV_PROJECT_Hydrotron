#include <SoftwareSerial.h>

SoftwareSerial mySerial(3, 2);




void servo_test_forward(int motor_forward) {

  mySerial.print("servo 1,2,3,4 motor_forward: ");
  mySerial.println(motor_forward);
}
void servo_test_backward(int motor_Backward) {

 

  mySerial.print("servo 1,2,3,4 motor_Backward: ");
  mySerial.println(motor_Backward);
}

void servo_test_R(int motor_I, int motor_R) {
 

  mySerial.print("servo 1,2 motor_R: ");
  mySerial.print(motor_R);
  mySerial.print("servo 3,4 motor_R: ");
  mySerial.println(motor_I);

}
void servo_test_L(int motor_I, int motor_R) {
  

  mySerial.print("servo 1,2 motor_I: ");
  mySerial.print(motor_I);
  mySerial.print("servo 3,4 motor_I: ");
  mySerial.println(motor_R);

}
void servo_test_up(int motor_U) {

 
  mySerial.print("servo 5,6 motor_U: ");
  mySerial.println(motor_U);
}
void servo_test_down(int motor_D) {

  
  mySerial.print("servo 5,6 motor_D: ");
  mySerial.println(motor_D);
}



void Debug_setup(){
  mySerial.begin(9600);
}
void Debug_loop() {

  

  if ((y1 < 70) && (!(x2 > 100 || x2 < 70)) && (!(y3 > 0)) && (!(x3 > 0))) {
    servo_test_forward(forw_);
  } else if ((y1 > 100) && (!(x2 > 100 || x2 < 70)) && (!(y3 > 0)) && (!(x3 > 0))) {
    servo_test_backward(back_);
    
  } else if ((x2 < 70) && (!(y1 > 100 || y1 < 70)) && (!(y3 > 0)) && (!(x3 > 0))) {
    servo_test_R(right, right_1);
    

  } else if ((x2 > 100) && (!(y1 > 100 || y1 < 70)) && (!(y3 > 0)) && (!(x3 > 0))) {
    servo_test_L(left, left_1);
    
  } else if ((y3 > 0) && (!(x3 > 0)) && (!(y1 > 100 || y1 < 70)) && (!(x2 > 100 || x2 < 70))) {
    servo_test_up(DOWN);
    //servo_test_up_test(DOWN);

  } else if ((x3 > 0) && (!(y3 > 0) && (!(y1 > 100 || y1 < 70)) && (!(x2 > 100 || x2 < 70)))) {
    servo_test_down(UP);

  } else {
    //servo_test_stop();
  }
}


void emergency_action(long interval1, long interval2){
 
  if(step_emergency_action==1){time_emergency_action=millis();step_emergency_action=2; mySerial.println("emergency_action");} 
  if(step_emergency_action==2&&millis()-time_emergency_action>=interval1){step_emergency_action=3;}
  if(step_emergency_action==3){servo_test_up(1800);}
  if(step_emergency_action==3&&millis()-time_emergency_action>=interval2){step_emergency_action=4;}
  if(step_emergency_action==4){servo_test_up(1500);}

}

 /*
    mySerial.print(x3);mySerial.print(" ,");
     mySerial.print(UP);mySerial.print(" ,");
      mySerial.print(y3);mySerial.print(" ,");
     mySerial.print(DOWN);mySerial.print(" ,");
     mySerial.println("-");
  */

  /*
   mySerial.print("forw_back= ");mySerial.print(forw_back);mySerial.print(" ,");
   mySerial.print("right= ");mySerial.print(right);mySerial.print(" ,");
   mySerial.print("left= ");mySerial.print(left);mySerial.print(" ,");
   mySerial.print("UP= ");mySerial.print(UP);mySerial.print(" ,");
   mySerial.print("DOWN= ");mySerial.print(DOWN);mySerial.println(" ,");

*/

  //Put_Serial_Data('#', '|', '*');


  /*mySerial.print(var_res_int[1]);mySerial.print(" ,");
    mySerial.print(var_res_int[2]);mySerial.print(" ,");
    mySerial.print(var_res_int[3]);mySerial.print(" ,");
    mySerial.print(var_res_int[4]);mySerial.print(" ,");
    mySerial.print(var_res_int[5]);mySerial.print(" ,");
    mySerial.print(var_res_int[6]);mySerial.print(" ,");
    mySerial.print(var_res_int[7]);mySerial.print(" ,");
    mySerial.println(var_res_int[8]);*/