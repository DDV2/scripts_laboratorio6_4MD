  #include <Wire.h>
    #include <Adafruit_MLX90614.h>
    Adafruit_MLX90614 mlx = Adafruit_MLX90614();
    int i=0;
    int L=5;
    float Tamb=0;
    float Tobj=0;
    void setup() {
      Serial.begin(57600);
//      Serial.println("Adafruit MLX90614 test");  
      mlx.begin();  
      
    }
void loop() {
// envía datos sólo si los recibe:
if (Serial.available()) {
// lee el byte de entrada:
switch (Serial.read()){ case '0': 
for (i=1;i<=L;i++)
        {Tamb=Tamb+mlx.readAmbientTempC();
          Tobj=Tobj+mlx.readObjectTempC();
          }
          
 //    Serial.print("Ambient = "); 
 //      Serial.print(Tamb/L); 
 //     Serial.print("*C\tObject = "); Serial.print(Tobj/L); Serial.println("*C");
      Serial.print(Tobj/L);
      Serial.print(" ");
    //   Serial.print(" "); 
      Serial.print(Tamb/L); 
      Serial.println();
      Tamb=0;
      Tobj=0;
//Serial.println();

}
}}
