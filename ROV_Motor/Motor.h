#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;

void servos_forward(int motor_forward) {

  servo1.writeMicroseconds(motor_forward);
  servo2.writeMicroseconds(motor_forward);
  servo3.writeMicroseconds(motor_forward);
  servo4.writeMicroseconds(motor_forward);
}
void servos_backward(int motor_Backward) {

  servo1.writeMicroseconds(motor_Backward);
  servo2.writeMicroseconds(motor_Backward);
  servo3.writeMicroseconds(motor_Backward);
  servo4.writeMicroseconds(motor_Backward);
}

void servos_R(int motor_I, int motor_R) {
  servo1.writeMicroseconds(motor_R);
  servo2.writeMicroseconds(motor_R);
  servo3.writeMicroseconds(motor_I);
  servo4.writeMicroseconds(motor_I);
}
void servos_L(int motor_I, int motor_R) {
  servo1.writeMicroseconds(motor_I);
  servo2.writeMicroseconds(motor_I);
  servo3.writeMicroseconds(motor_R);
  servo4.writeMicroseconds(motor_R);
}
void servos_up(int motor_U) {

  servo5.writeMicroseconds(motor_U);
  servo6.writeMicroseconds(motor_U);
}
void servos_down(int motor_D) {

  servo5.writeMicroseconds(motor_D);
  servo6.writeMicroseconds(motor_D);
}

void Motor_setup() {

  servo1.attach(9); //front_2
  servo1.writeMicroseconds(1500);

  servo2.attach(5); //rear_2
  servo2.writeMicroseconds(1500);

  servo3.attach(6); //rear_1...rear_2
  servo3.writeMicroseconds(1500);

  servo4.attach(11); //front_1...up_2
  servo4.writeMicroseconds(1500);

  servo5.attach(3); //up rov...rear_2
  servo5.writeMicroseconds(1500);

  servo6.attach(10); //up rov6..front_1
  servo6.writeMicroseconds(1500);

}

void servos_stop() {

  servo1.writeMicroseconds(1500);
  servo2.writeMicroseconds(1500);
  servo3.writeMicroseconds(1500);
  servo4.writeMicroseconds(1500);
  servo5.writeMicroseconds(1500);
  servo6.writeMicroseconds(1500);
}

void RUN_Motor_For_1_Minute() {
  /*startTime = millis(); // Get the current time
  endTime = 30000; //  for the end time 
  while (millis() < endTime) { // Loop until run the end time is reached
    //servo5.writeMicroseconds(1800);
    // servo6.writeMicroseconds(1800);
    //mySerial.println("Check Comm.");
  }

  //servo5.writeMicroseconds(1500);
  //servo6.writeMicroseconds(1500);
  //mySerial.println("Comm Need Mintanance.");
  */
}





void Motor_loop() {
  if ((y1 < 70) && (!(x2 > 100 || x2 < 70)) && (!(y3 > 0)) && (!(x3 > 0))) {
    servos_forward(forw_);
  } else if ((y1 > 100) && (!(x2 > 100 || x2 < 70)) && (!(y3 > 0)) && (!(x3 > 0))) {
    servos_backward(back_);
    
  } else if ((x2 < 70) && (!(y1 > 100 || y1 < 70)) && (!(y3 > 0)) && (!(x3 > 0))) {
    servos_R(right, right_1);
    

  } else if ((x2 > 100) && (!(y1 > 100 || y1 < 70)) && (!(y3 > 0)) && (!(x3 > 0))) {
    servos_L(left, left_1);
    
  } else if ((y3 > 0) && (!(x3 > 0)) && (!(y1 > 100 || y1 < 70)) && (!(x2 > 100 || x2 < 70))) {
    servos_up(UP);

  } else if ((x3 > 0) && (!(y3 > 0) && (!(y1 > 100 || y1 < 70)) && (!(x2 > 100 || x2 < 70)))) {
    servos_down(DOWN);

  } else {
    servos_stop();
  }
}

void emergency_action(long interval1, long interval2){
 
  if(step_emergency_action==1){time_emergency_action=millis();step_emergency_action=2;servos_stop();} 

  if(step_emergency_action==2&&millis()-time_emergency_action>=interval1){step_emergency_action=3;}

  if(step_emergency_action==3){servos_up(1800);}

  if(step_emergency_action==3&&millis()-time_emergency_action>=interval2){step_emergency_action=4;}

  if(step_emergency_action==4){servos_up(1500);}

}