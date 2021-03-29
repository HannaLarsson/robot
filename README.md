# robot
Control program for a robot that moves in a two dimensional room (rectangular or circular). 

The robot moves in the room by interpreting a string of commands in either Swedish or English:
- Swedish: V: Turn left, H: Turn right, G: Move forward (Example string VGGHGHGHGG)
- English L: Turn left, R: Turn right, F: Move forward (Example string LFFRFRFRFF)

When the robot runs out of commands, it reports its current square (x,y) and direction/heading using the following letters:
N: North, Ö: East, S: South, V: West

When the program starts, the robot is always facing north.

The room can be either rectangular or circular.
