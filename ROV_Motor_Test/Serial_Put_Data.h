#define max_send_data 10
int var_send_int[max_send_data+1];
String datos;

void Put_Serial_Data(char header,char delimiter,char terminator){
  
datos+=header;

for(int i=1;i<=max_send_data;i++){
  datos+=(String)var_send_int[i];
  if(i!=max_send_data){datos+=delimiter;} 
  }
  
  datos+=terminator;
  Serial.println(datos);
  datos="";
}
