# CS-350
# CS 350 Milestone Three — Morse Code LED Controller

## Project Summary and Problem Solved

This project involved creating Python code to control red and blue LEDs to blink Morse code messages. The red LED represented dots and the blue LED represented dashes, following Morse code timing standards (dot: 500ms, dash: 1500ms). A state machine was implemented to manage LED blinking patterns and switch messages smoothly on button press without interrupting the current message. Additionally, a 16x2 LCD display was integrated to show the Morse code message and provide debugging feedback. The project solved the challenge of designing an interactive embedded system interface that communicates via LED signals.

## What I Did Particularly Well

- Developed a robust and non-blocking state machine to control the LED patterns and message transitions.  
- Integrated the 16x2 display effectively for real-time feedback and debugging information.  
- Applied coding best practices, including clear formatting, comprehensive commenting, and modular design for readability and maintainability.

## Areas for Improvement

- Enhance responsiveness by incorporating interrupt-driven or asynchronous programming techniques.  
- Improve LCD user interface for clearer and more detailed user feedback.  
- Expand error handling and input validation for more robust operation.

## Tools and Resources Added to My Support Network

- Python libraries: `GPIOZero` for GPIO control, and libraries for LCD interfacing.  
- Use of `draw.io` for designing state machine diagrams.  
- Learning about state machine design patterns and embedded system timing considerations.

## Transferable Skills

- Designing and implementing state machines for embedded hardware control.  
- Managing timing and concurrency in hardware-software interfaces.  
- Writing maintainable Python code to interface with physical components.  
- Debugging and providing user feedback via displays.

## Maintainability, Readability, and Adaptability

- Code structured with modular functions and clear state transitions to simplify updates.  
- Detailed inline comments and documentation for future maintainers.  
- Separation of hardware control and application logic to ease adaptation for other hardware.  
- Consistent naming conventions and adherence to Python coding standards.

