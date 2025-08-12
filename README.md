# CS-350
# CS 350 Final Project — Smart Thermostat Prototype

## Project Summary and Problem Solved

The final project was to build a smart thermostat prototype that reads room temperature using the AHT2 sensor via I2C, controls heating and cooling LEDs, and allows the user to adjust the temperature set point with buttons. A state machine managed the system states: off, heating, and cooling. The system displayed the current temperature, set point, and date/time on a 16x2 LCD and simulated sending data to a server via UART. The project addressed the challenge of integrating multiple hardware peripherals into a cohesive embedded system meeting specific business requirements.

## What I Did Particularly Well

- Successfully integrated multiple peripherals: I2C temperature sensor, GPIO LEDs and buttons, UART communication, and LCD display.  
- Designed and implemented a state machine that accurately represented system states and ensured smooth transitions.  
- Delivered a comprehensive technical report comparing hardware architectures and recommending a solution aligned with business goals.

## Areas for Improvement

- Could improve power management and energy efficiency considerations for production use.  
- Expand security features related to cloud connectivity and data transmission.  
- Enhance user interface on the LCD for clearer instructions and error messages.

## Tools and Resources Added to My Support Network

- GPIOZero library for button and LED control.  
- `smbus2` for I2C communication with temperature sensor.  
- UART serial communication methods for simulating data transmission.  
- Research on embedded architectures: Raspberry Pi, Microchip, and Freescale.

## Transferable Skills

- Embedded systems programming integrating sensors, actuators, and communication protocols.  
- State machine design for managing complex system states and user inputs.  
- Technical documentation and comparative hardware analysis based on business and technical criteria.  
- Applying coding best practices to hardware interfacing projects.

## Maintainability, Readability, and Adaptability

- Modularized code with clear separation between hardware initialization, state machine logic, and user interface components.  
- Well-commented code adhering to Python formatting standards for maintainability.  
- Flexibility to adapt the code to different hardware architectures by abstracting peripheral interfaces.  
- Thorough documentation of system design and operational logic to support future development and maintenance.

