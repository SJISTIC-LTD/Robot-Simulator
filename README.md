# Robot-Simulator
The simulator I built is written in Python and very cleverly dubbed Sobot Rimulator. You can find v1.0.0 on GitHub. It does not have a lot of bells and whistles but it is built to do one thing very well: provide an accurate simulation of a mobile robot and give an aspiring roboticist a simple framework for practicing robot software programming. While it is always better to have a real robot to play with, a good Python robot simulator is much more accessible and is a great place to start.In real-world robots, the software that generates the control signals (the “controller”) is required to run at a very high speed and make complex computations. This affects the choice of which robot programming languages are best to use: Usually, C++ is used for these kinds of scenarios, but in simpler robotics applications, Python is a very good compromise between execution speed and ease of development and testing.


In this tutorial, I will be describing the robot control software architecture that comes with v1.0.0 of Sobot Rimulator, and providing snippets from the Python source (with slight modifications for clarity). However, I encourage you to dive into the source and mess around. The simulator has been forked and used to control different mobile robots, including a Roomba2 from iRobot. Likewise, please feel free to fork the project and improve it.

The control logic of the robot is constrained to these Python classes/files:

models/supervisor.py—this class is responsible for the interaction between the simulated world around the robot and the robot itself. It evolves our robot state machine and triggers the controllers for computing the desired behavior.
models/supervisor_state_machine.py—this class represents the different states in which the robot can be, depending on its interpretation of the sensors.
The files in the models/controllers directory—these classes implement different behaviors of the robot given a known state of the environment. In particular, a specific controller is selected depending on the state machine.
