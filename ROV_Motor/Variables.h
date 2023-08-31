unsigned long previousMillis = 0; // variable to store the last time the function was called
int previousValue = 0; // variable to store the previous value of the input variable
unsigned long startTime;
unsigned long endTime;

int y1, x2, x3, y3;
short toggle_ACK,joystick_ACK;


int x2_1, x2_2;
int ch;
int motor_forward;
int motor_Backward;
int motor_I;
int motor_R;
int motor_U;
int motor_D;

//int motor_stop;
//int forw_back;

int forw_;
int back_;
int left;
int left_1;
int right;
int right_1;
int UP;
int DOWN;

//////solinoid //////
int BA;
int BB;
int BX;
int BY;


short is_ok_flag=0;

short is_ok=0;

short step_emergency_action=1;
long time_emergency_action=0;