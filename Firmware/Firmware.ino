#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define ENCODER_CLK 9  // Rotate one way
#define ENCODER_DT  10  // Rotate the other way
#define ENCODER_SW  8  // Button
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1  // or -1 if reset pin is not used

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

int counter = 0;
int lastClkState;
bool lastButtonState = HIGH;
unsigned long lastButtonPress = 0;
int total = 0;
int faceColor1 = 1;
static const unsigned char PROGMEM happyFacepixel[] = {0xe0};

void sendValue(int value) {
  unsigned long now = millis();
  Serial.println(value);
}

int reciveValue() {
  Serial.setTimeout(2000);
  Serial.println("Waiting for int...");
  while (true) {
    while (Serial.available()) {
      char c = Serial.read();
      Serial.print("Char received: ");
      Serial.println(c);
      }
    }
  }



void drawSad (void) {
    display.clearDisplay();
    display.fillRect(39, 22, 12, 10, 1);
    display.fillRect(79, 22, 11, 10, 1);
    display.fillRect(58, 23, 14, 6, faceColor1);
    display.fillRect(53, 29, 24, 4, 1);
    display.fillRect(51, 33, 8, 7, 1);
    display.fillRect(71, 33, 8, 7, 1);
    display.fillRect(54, 40, 22, 4, 1);
    display.fillRect(62, 33, 6, 7, 1);
    display.fillRect(74, 9, 5, 5, 1);
    display.fillRect(79, 12, 15, 5, 1);
    display.fillRect(51, 9, 5, 5, 1);
    display.fillRect(36, 12, 15, 5, 1);
    display.fillRect(57, 47, 16, 4, 1);
    display.fillRect(54, 50, 4, 4, 1);
    display.fillRect(72, 50, 4, 4, 1);

    display.display();
}


void drawDead(void) {
    display.clearDisplay();
    display.fillRect(58, 23, 14, 6, faceColor1);
    display.fillRect(53, 29, 24, 4, 1);
    display.fillRect(51, 33, 8, 7, 1);
    display.fillRect(71, 33, 8, 7, 1);
    display.fillRect(54, 40, 22, 4, 1);
    display.fillRect(62, 33, 6, 7, 1);
    display.setTextColor(1);
    display.setTextSize(3);
    display.setTextWrap(false);
    display.setCursor(37, 7);
    display.print("X");
    display.setCursor(78, 7);
    display.print("X");
    display.drawRect(53, 50, 1, 4, 1);
    display.drawRect(76, 50, 1, 4, 1);
    display.fillRect(57, 47, 16, 4, 1);
    display.fillRect(51, 54, 4, 4, 1);
    display.fillRect(54, 50, 4, 4, 1);
    display.fillRect(75, 54, 4, 4, 1);
    display.fillRect(72, 50, 4, 4, 1);

    display.display();
}


void drawHappy(void) {
    display.clearDisplay();
    display.fillRect(58, 23, 14, 6, faceColor1);
    display.fillRect(53, 29, 24, 4, 1);
    display.fillRect(51, 33, 8, 7, 1);
    display.fillRect(71, 33, 8, 7, 1);
    display.fillRect(54, 40, 22, 4, 1);
    display.fillRect(62, 33, 6, 7, 1);
    display.drawRect(53, 50, 1, 4, 1);
    display.drawRect(76, 50, 1, 4, 1);
    display.fillRect(57, 50, 16, 4, 1);
    display.fillRect(50, 50, 4, 4, 1);
    display.fillRect(54, 50, 4, 4, 1);
    display.setTextColor(1);
    display.setTextSize(3);
    display.setTextWrap(false);
    display.setCursor(38, 6);
    display.print("$");
    display.fillRect(76, 50, 4, 4, 1);
    display.fillRect(72, 50, 4, 4, 1);
    display.fillRect(69, 54, 10, 5, 1);
    display.setCursor(77, 6);
    display.print("$");
    display.fillRect(75, 59, 3, 5, 1);
    display.fillRect(50, 47, 3, 3, 1);
    display.drawBitmap(50, 53, happyFacepixel, 3, 1, 0);

    display.display();
}
int Layer_3_color = 1;

void drawNeutralMid(void) {
    display.clearDisplay();
    display.fillRect(58, 23, 14, 6, faceColor1);
    display.fillRect(53, 29, 24, 4, 1);
    display.fillRect(51, 33, 8, 7, 1);
    display.fillRect(71, 33, 8, 7, 1);
    display.fillRect(54, 40, 22, 4, 1);
    display.fillRect(62, 33, 6, 7, 1);
    display.drawRect(53, 50, 1, 4, 1);
    display.drawRect(76, 50, 1, 4, 1);
    display.fillRect(57, 50, 16, 4, 1);
    display.fillRect(80, 14, 13, 12, 1);
    display.fillRect(50, 50, 4, 4, 1);
    display.fillRect(54, 50, 4, 4, 1);
    display.fillRect(37, 14, 13, 12, 1);
    display.fillRect(76, 50, 4, 4, 1);
    display.fillRect(72, 50, 4, 4, 1);

    display.display();
}

void setup() {
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // 0x3C is common I2C address
  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
  display.setTextWrap(true);
  display.setTextSize(2);

  pinMode(ENCODER_CLK, INPUT_PULLUP);
  pinMode(ENCODER_DT, INPUT_PULLUP);
  pinMode(ENCODER_SW, INPUT_PULLUP);

  Serial.begin(9600);
  drawNeutralMid();
  lastClkState = digitalRead(ENCODER_CLK);
}

void showFaces(int& tot, int cou){
  if(tot < 0){
    drawDead();
  }else if (cou == 0 ){
    display.clearDisplay();
    display.setCursor(17, 15); 
    display.setTextSize(2);
    display.print("Balance: ");
    display.setCursor(10, 33);
    display.print(tot);
    display.display();
    delay(2000);
    drawNeutralMid();
  }else if(cou < 0){
    drawSad();
    delay(2000);
    display.clearDisplay();
    display.setCursor(17, 15); 
    display.setTextSize(2);
    display.print("Balance: ");
    display.setCursor(10, 33);
    display.print(tot);
    display.display();
    delay(2000);
    drawNeutralMid();
  }else if(cou > 0){
    drawHappy();
    delay(2000);
    display.clearDisplay();
    display.setTextSize(2);
    display.setCursor(17, 15); 
    display.print("Balance: ");
    display.setCursor(10, 33);
    display.print(tot);
    display.display();
    delay(2000);
    drawNeutralMid();
  }

}
void loop() {
  display.clearDisplay();
  int currentClkState = digitalRead(ENCODER_CLK);

  if (currentClkState != lastClkState) {
    display.clearDisplay();
    if (digitalRead(ENCODER_DT) != currentClkState) {
      counter +=10;
    } else {
      counter -= 10;
    }
    display.setCursor(10, 25);
    display.print(counter);
    display.display();
  }
  lastClkState = currentClkState;

  // Handle Button
  bool buttonState = digitalRead(ENCODER_SW);
  if (buttonState == LOW && lastButtonState == HIGH) {
    if (millis() - lastButtonPress > 200) {
      display.clearDisplay();
      sendValue(counter);
      total += counter ;//reciveValue()
      showFaces(total , counter);
      lastButtonPress = millis();
      counter = 0;
    }
  }
  lastButtonState = buttonState;
}
