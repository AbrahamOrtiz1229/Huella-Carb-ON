//Incluir librerias para funcionamiento del código.
#include <WiFi.h>
#include <PubSubClient.h>
#include <Firebase_ESP_Client.h>
#include <addons/TokenHelper.h>

//Da el token generation process info.
#include "addons/TokenHelper.h"
//Da el RTDB payload printing info and other helper functions.
#include "addons/RTDBHelper.h"

// Se pone la información de la red de internet a conectarse
#define WIFI_SSID "HackPuebla101"
#define WIFI_PASSWORD "nefer.aton.rure"

// Insert Firebase project API Key
#define API_KEY "AIzaSyBbuUlvoFJ3S6HQrB7NT3GtvKE4IRBcdkw"


// Insert RTDB URLefine the RTDB URL */
#define DATABASE_URL "https://carbon-footprint-856d0-default-rtdb.firebaseio.com"


//Define Firebase Data object
FirebaseData fbdo;

FirebaseAuth auth;
FirebaseConfig config;
//Variables for Firebase
unsigned long sendDataPrevMillis = 0;
float floatValue;
bool signupOK = false;

//Variables para definir los pines de los electrónicos.
int refri = 12;
int micro = 14;
int tv = 27;
int foco = 26;
int aire = 25;


// Funciones que envian los datos al respectivo apartado del electrónico.
// El parámetro es el valor que se va a subir.
void sendValRefri(float count){
  Firebase.RTDB.setInt(&fbdo, "T-Systems/W_Refri", count);
}

void sendValMicro(float count){
  Firebase.RTDB.setInt(&fbdo, "T-Systems/W_Microondas", count);
}

void sendValTv(float count){
  Firebase.RTDB.setInt(&fbdo, "T-Systems/W_Tv", count);
}

void sendValFocos(float count){
  Firebase.RTDB.setInt(&fbdo, "T-Systems/W_Focos", count);
 
}

void sendValAire(float count){
  Firebase.RTDB.setInt(&fbdo, "T-Systems/W_Aire", count);
}

// Funciones que leen la energía del electrónico desde la base de datos.

float getValRefriW(){
  float focoW;
  if (Firebase.RTDB.getFloat(&fbdo, "T-Systems/W_Refri")) {
     focoW = fbdo.floatData();
     return focoW;
  }
}

float getValMicroW(){
  float focoW;
  if (Firebase.RTDB.getFloat(&fbdo, "T-Systems/W_Microondas")) {
     focoW = fbdo.floatData();
     return focoW;
  }
}

float getValTvW(){
  float focoW;
  if (Firebase.RTDB.getFloat(&fbdo, "T-Systems/W_Tv")) {
     focoW = fbdo.floatData();
     return focoW;
  }
}

float getValFocosW(){
  float focoW;
  if (Firebase.RTDB.getFloat(&fbdo, "T-Systems/W_Focos")) {
     focoW = fbdo.floatData();
     return focoW;
 
  }
}

float getValAireW(){
  float focoW;
  if (Firebase.RTDB.getFloat(&fbdo, "T-Systems/W_Aire")) {
     focoW = fbdo.floatData();
     return focoW;
  }
}

// Función que lee si se tiene encendido o apagago el electrónico.
String getValRefri(){
  String efoco;
  if (Firebase.RTDB.getString(&fbdo, "T-Systems/E_Refri")) {
     if (fbdo.dataType() == "string") {
       efoco = fbdo.stringData();
       return efoco;
     }
  }
}

String getValMicro(){
  String efoco;
  if (Firebase.RTDB.getString(&fbdo, "T-Systems/E_Micro")) {
     if (fbdo.dataType() == "string") {
       efoco = fbdo.stringData();
       return efoco;
     }
  }
}

String getValTv(){
  String efoco;
  if (Firebase.RTDB.getString(&fbdo, "T-Systems/E_Tv")) {
     if (fbdo.dataType() == "string") {
       efoco = fbdo.stringData();
       return efoco;
     }
  }
}
String getValFocos(){
  String efoco;
  if (Firebase.RTDB.getString(&fbdo, "T-Systems/E_Focos")) {
     if (fbdo.dataType() == "string") {
       efoco = fbdo.stringData();
       return efoco;
     }
  }
}

String getValAire(){
  String efoco;
  if (Firebase.RTDB.getString(&fbdo, "T-Systems/E_Aire")) {
     if (fbdo.dataType() == "string") {
       efoco = fbdo.stringData();
       return efoco;
     }
  }
}


void setup() {
  //Se conecta a internet
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED){
    delay(100);
  }
  //Se conecta a Firebase 
  config.api_key = API_KEY;
  config.database_url = DATABASE_URL;
  if (Firebase.signUp(&config, &auth, "", "")){
    signupOK = true;
  }
  config.token_status_callback = tokenStatusCallback; //see addons/TokenHelper.h
  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);

  // Se declaran como salida los pines de los electrónicos.

  pinMode(refri, OUTPUT);
  pinMode(micro, OUTPUT);
  pinMode(tv, OUTPUT);
  pinMode(foco, OUTPUT);
  pinMode(aire, OUTPUT);
  Serial.begin(9600);
}

void loop() {

  //Se declaran las variables que tendrán el voltaje
  float foco_con, refri_con, micro_con, tv_con, aire_con;

  // Se ve si está prendido o apagado el electrónico según la base de datos.
  if (getValFocos() == "1"){//Si está prendido se suma la energía y se prende.
    digitalWrite(foco, HIGH);
    foco_con = getValFocosW(); //Se lee la variable en base de datos
    foco_con = foco_con+0.0002777; //Se le suma la energía  (el factor a sumar sería el que detecta el sensor)
    sendValFocos(foco_con);  //Se manda el dato actualizado a la base de datos
    
  }else{ //Si está apagado se apaga el electrónico
    digitalWrite(foco, LOW);
    
  }
  //Se hace exactamente lo mismo con los demás electrónicos.
  if (getValRefri() == "1"){
    digitalWrite(refri, HIGH);
    refri_con = getValRefriW();
    refri_con = refri_con+0.0011111;
    sendValRefri(refri_con); 
    
  }else{
    digitalWrite(refri, LOW);
    
  }
  if (getValMicro() == "1"){
    digitalWrite(micro, HIGH);
    micro_con = getValMicroW();
    micro_con = micro_con+0.025;
    sendValMicro(micro_con); 
    
  }else{
    digitalWrite(micro, LOW);
    
  }
  if (getValTv() == "1"){
    digitalWrite(tv, HIGH);
    tv_con = getValTvW();
    tv_con = tv_con+0.001944;
    sendValTv(tv_con); 
    
  }else{
    digitalWrite(tv, LOW);
    
  }
  if (getValAire() == "1"){
    digitalWrite(aire, HIGH);
    aire_con = getValAireW();
    aire_con = aire_con+0.055555;
    sendValAire(aire_con); 
    
  }else{
    digitalWrite(aire, LOW);
    
  }

  //Un pequenio delay
  delay(100);
}
