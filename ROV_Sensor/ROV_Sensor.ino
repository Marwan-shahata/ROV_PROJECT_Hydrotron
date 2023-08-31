#include <SFE_BMP180.h>

#include <MPU9250_WE.h>

#include <Wire.h>


#include <SoftwareSerial.h>

SoftwareSerial mySerial(3, 2);

#include "Serial_Get_Data.h"

#include "Serial_Put_Data.h"

/////////////BMb180///////////////
SFE_BMP180 pressure;
#define ALTITUDE 11.0 // Altitude of suz, CO. in meters a5le b21y altutude alex 5 meters
char status;
double T, P, p0, a, depth;
///////////MPU9250///////////
#define MPU9250_ADDR 0x68
float ax, ay, az, gx, gy, gz, mx, my, mz;
float mag_norm;
float accAngleX, accAngleY, gyroAngleX, gyroAngleY, gyroAngleZ;
float elapsedTime, currentTime, previousTime;
float alpha = 0.96;
MPU9250_WE myMPU9250 = MPU9250_WE(MPU9250_ADDR);
/////////////////////////////////////

////////////SOLINOID////////////////////////////

int valve1, valve2, valve3, valve4; // Initialize valve state to closed

#define valve1Pin 9
#define valve2Pin 8
#define valve3Pin 7
#define valve4Pin 6
bool valve1State = 0;
bool valve2State = 0;
bool valve3State = 0;
bool valve4State = 0;
/////////////////////////////////////////

////////////FLAG////////////////////////////
bool flag_BMP180 = 0;
bool flag_MPU9250 = 0;

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  Wire.begin();

  //Serial.println("Begin");
  if (pressure.begin()) {
    //Serial.println("BMP180 init success");
    flag_BMP180 = 1;
  } else {
    //Serial.println("BMP180 init fail\n\n");
    flag_BMP180 = 0;
    //while(1); // Pause forever.
  }

  if (!myMPU9250.init()) {
    //Serial.println("MPU9250 does not respond");
    flag_MPU9250 = 0;
  } else {
    //Serial.println("MPU9250 is connected");
    flag_MPU9250 = 1;
  }
  if (!myMPU9250.initMagnetometer()) {
    //Serial.println("Magnetometer does not respond");
  } else {
    //Serial.println("Magnetometer is connected");
  }
  //Serial.println("Position you MPU9250 flat and don't move it - calibrating...");
  delay(1000);
  myMPU9250.autoOffsets();
  // Serial.println("Done!");
  myMPU9250.enableGyrDLPF();
  myMPU9250.setGyrDLPF(MPU9250_DLPF_6);
  myMPU9250.setSampleRateDivider(5);
  myMPU9250.setGyrRange(MPU9250_GYRO_RANGE_250);
  myMPU9250.setAccRange(MPU9250_ACC_RANGE_2G);
  myMPU9250.enableAccDLPF(true);
  myMPU9250.setAccDLPF(MPU9250_DLPF_6);
  myMPU9250.setMagOpMode(AK8963_CONT_MODE_100HZ);
  delay(200);

  ////////////SOLINOID////////////////////////////
  pinMode(valve1Pin, OUTPUT);
  pinMode(valve2Pin, OUTPUT);
  pinMode(valve3Pin, OUTPUT);
  pinMode(valve4Pin, OUTPUT);

}

void loop() {
  Get_Serial_Data('#', '|', '*');
  delay(1);

  mySerial.print(var_res_int[1]);
  mySerial.print(" ,"); //BY
  mySerial.print(var_res_int[2]);
  mySerial.print(" ,"); //BX
  mySerial.print(var_res_int[3]);
  mySerial.print(" ,"); //BA
  mySerial.print(var_res_int[4]);
  mySerial.println(" ,"); //BB

  valve1 = var_res_int[1];
  valve2 = var_res_int[2];
  valve3 = var_res_int[3];
  valve4 = var_res_int[4];

  ////////////SOLINOID Latch////////////////////////////
  ////////////////////valve 1//////////////////

 
  digitalWrite(valve1Pin, valve1);

  ////////////////////valve 2//////////////////

  
  digitalWrite(valve2Pin, valve2);
  ////////////////////valve 3//////////////////
  
  digitalWrite(valve3Pin, valve3);
  ////////////////////valve 4//////////////////
  
  digitalWrite(valve4Pin, valve4);

  status = pressure.startTemperature();
  if (status != 0) {
    // Wait for the measurement to complete:
    delay(status);
    status = pressure.getTemperature(T);
  }

  status = pressure.startPressure(3);
  if (status != 0) {
    delay(status);
    status = pressure.getPressure(P, T);
  }
  if (status != 0) {
    p0 = pressure.sealevel(P, ALTITUDE);
    a = pressure.altitude(P, p0);
    depth = ((p0 - P) / 100) * 0.0101972;
  }

  xyzFloat gValue = myMPU9250.getGValues();
  xyzFloat gyr = myMPU9250.getGyrValues();
  xyzFloat magValue = myMPU9250.getMagValues();
  float temp = myMPU9250.getTemperature();
  float resultantG = myMPU9250.getResultantG(gValue);
  ax = gValue.x;
  ay = gValue.y;
  az = gValue.z;
  mag_norm = sqrt(mx * mx + my * my + mz * mz);
  /*float mx_norm = mx / mag_norm ;
  float  my_norm = my / mag_norm ;
  float mz_norm = mz / mag_norm ;*/

  float pitch = myMPU9250.getPitch();
  float pitch_2 = -180 * atan(gValue.x / sqrt(gValue.y * gValue.y + gValue.z * gValue.z)) / M_PI;
  float roll = myMPU9250.getRoll();
  float roll_2 = 180 * atan(gValue.y / sqrt(gValue.x * gValue.x + gValue.z * gValue.z)) / M_PI;
  // float yawX = mx_norm*cos(pitch) + my_norm*sin(pitch)*sin(roll) + mz_norm*sin(pitch)*cos(roll) ;
  //float yawY = my_norm*cos(roll) - mz_norm*sin(roll) ;
  //float yaw =  atan2(-yawX ,yawY)*180/M_PI; 
  float my_norm = (my * cos(roll)) - (mz * sin(roll));
  float mx_norm = (mx * cos(pitch)) + (my * sin(roll) * sin(pitch)) + (mz * cos(roll) * sin(pitch));

  //float yaw_2 = 180 * atan (gValue.z/sqrt(gValue.x*gValue.x +gValue.z*gValue.z))/M_PI;
  float yaw = atan2(my_norm, mx_norm);

  var_send_int[1] = (P * 1000);
  var_send_int[2] = (p0 * 1000);
  var_send_int[3] = depth * 100;
  var_send_int[4] = T * 10;
  var_send_int[5] = ax * 98;
  var_send_int[6] = ay * 98;
  var_send_int[7] = az * 98;
  var_send_int[8] = pitch;
  var_send_int[9] = roll;
  var_send_int[10] = yaw;
  var_send_int[11] = flag_BMP180;
  var_send_int[12] = flag_MPU9250;

  Put_Serial_Data('#', '|', '*');

}