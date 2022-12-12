# MakerspaceRubiksCubeSolver
Rubik's cube solving algorithm
Interacting with physical robot
Includes OpenCV algorithm with deployment on Raspberry Pi and Stepper motor control

Place cube on robot with white side up

            U0 U1 U2
            U3 U4 U5
            U6 U7 U8

L0 L1 L2    F0 F1 F2    R0 R1 R2    B0 B1 B2
L3 L4 L5    F3 F4 F5    R3 R4 R5    B3 B4 B5
L6 L7 L8    F6 F7 F8    R6 Ry R8    B6 B7 B8

            D0 D1 D2
            D3 D4 D5
            D6 D7 D8


go through each side 
add array of colors for each side in cube palatte
feed this to cube algorithm 
cube algorithm to motor control