# TFT-Console
A small console with 6 buttons and a 2.8" touch screen, powered with a raspberry pi pico.
<img width="785" height="744" alt="image" src="https://github.com/user-attachments/assets/36f0b92d-af6d-4a90-b34a-b5a1e7ac4145" />

This is my project for the Displays week. It is a small game console, with 6 Cherry MX switches as controls, a Raspberry Pi Pico to control the display, and a 2.8 inch TFT touch screen. 
I wanted this to be more than just a game console. It's going to have a few apps like drawing, games, and other utilities like a stopwatch or a clock.
Unfortunately, I wasn't able to find a 3D model for the screen, which is why I only have a render of the PCB.

****PCB and Schematic****

Below are the PCB and the Schematic. I had to learn a lot about TFT screens and how to wire them up to make these. I wanted to make the board as compact as possible, and to save money on PCB costs as the price gets higher if a side is more than 100mm long. Because of this, I decided to put the raspberry pi pico on the back, behind the screen. For the PCB, the only warnings I had were silkscreen clipped errors, which can be ignored.
<img width="970" height="757" alt="image" src="https://github.com/user-attachments/assets/41b1d8ea-d23c-4ad6-8926-56c93e193ddd" />

This is the schematic. At first I had a bunch of errors because I tried to connect 2 labels to the same pin, but then I realized I had to combine both pins into one, and I got 0 errors.
<img width="1076" height="725" alt="image" src="https://github.com/user-attachments/assets/bc363f7a-c5e9-41e1-9c83-7f1a4c1b44f8" />


**Firmware**

For the firmware, I didn't make the whole console with apps and stuff yet, cuz it's hard to test if parts of the code work, and I don't want to accidentally build on something that won't work. For that reason, I made a placeholder code that displays six different colored counters on the screen that is tied to a respective one of my Cherry MX switches, and when each button is pressed, its counter goes up. Its a simple code, and doesn't do much, but its not a bad start and it'll be good for testing my screen and buttons.
<img width="376" height="708" alt="image" src="https://github.com/user-attachments/assets/5ea56cec-b705-46cc-b172-9cbfe8490017" />


**BOM**

I bought my main parts on Aliexpress and the PCB on JLCPCB. The raspberry pi pico was very cheap, coming to only $1.55. The TFT on the other hand, wasn't so cheap, coming to $10.44, which is understandable being the main component of the project. The PCB costed $4, and $1.50 for shipping. For the Cherry MX switches, I'm going to be using some of the leftover switches from my previous project the MIDI keypad to save money. That brings the total to $19.29, althouhg prices are subject to change.
<img width="899" height="416" alt="image" src="https://github.com/user-attachments/assets/e3389e97-2498-450d-beda-dacfa1c088bf" />


Well, this project was really fun, and I learnt so much from it. I got into the new territory of screens and displays, and its the first time I've used python to code instead of C++. I also learned new things in Kicad, even though I used it for a few other projects. This week was lovely, and I'm happy and thankful that half-life was able to give me this opportunity. Thank you!
