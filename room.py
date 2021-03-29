import sys
from math import hypot

class Room:
    # A room has a size (Rectangular tuple (x, y), circular int), and a shape.
    def __init__(self, size, shape):
        self.size = None
        self.shape = None
        if shape in ("RC"):
            self.shape = shape
            if shape is "R":
                if size[0] > 0 and size[1] > 0:
                    self.size = size
                else:
                    print("Error: given size is illegal.")
            elif shape is "C":
                if size > 0:
                    self.size = size
                else:
                    print("Error: given size is illegal.")
        else:
            print("Error: given shape is illegal.")
        self.robot = None

    def get_start_position(self):
    # Return the robot's starting position in (x,y) format.
        return self.robot.get_start_position()

    def contains(self, position):
    # Return True if the given position is part of the room. If a circular room, only whole squares are part of the room.
        size = self.get_size()
        x = position[0]
        y = position[1]
        
        result = False

        if self.get_shape() is "R":
            if x >= 0 and x < size[0] and y >= 0 and y < size[1]:
                result = True
            else:
                result = False
        elif self.get_shape() is "C":
            if x >= 0:
                if y >= 0:        
                    if hypot(x+1, y+1) <= self.get_radius():
                        result = True
                    else:
                        result = False
                else:
                    if hypot(x+1, y-1) <= self.get_radius():
                        result = True
                    else:
                        result = False
            else:
                if y >= 0:
                    if hypot(x-1, y+1) <= self.get_radius():
                        result = True
                    else:
                        result = False
                else:
                    if hypot(x-1, y-1) <= self.get_radius():
                        result = True
                    else:
                        result = False
        else:
            print("Error: room has illegal shape.")
        return result
        
    def get_size(self):
    # Return the size of the room        
        return self.size

    def set_size(self, x, y=None):
    # Set the size of the room. Must be positive integers. 
    # If circular room, the size is doubled since the given x is the radius.
        if self.get_shape() is "R":
            if (x <= 0) or (y <= 0):
                print("New size of room too small, must be positive integers.")
            elif not isinstance(x, int):
                print("Invalid type for given x value for size of room.")
            elif not isinstance(y, int):
                print("Invalid type for given y value for size of room.")
            else:                
                self.size = (x, y)
        else:
            if (x <= 0):
                print("New size of room too small, must be positive integers.")
            elif not isinstance(x, int):
                print("Invalid type for given x value for size of room.")
            else:
                self.size = x*2

    def get_shape(self):
    # Return the shape of the room (R: rectangular, C: circular)
        return self.shape

    def set_shape(self, shape):
    # Set the shape of the room (R: rectangular, C: circular)
        if isinstance(shape, str) and shape in ("RC") and shape:
            self.shape = shape
        else:
            print("Given shape not valid. Can be rectangular ('R') or circular ('C').")

    def get_radius(self):
    # Return the actual radius of the circle around the room. Should only be used for circular rooms.
        if isinstance(self.get_size(), int):
            if self.get_size() > 0:
                return hypot(self.get_size(), 1)
            else:
                return 0

    def get_robot(self):
    # Return the robot object
        return self.robot

    def set_robot(self, robot):
    # Set the given robot as the room's robot.
        if isinstance(robot, Robot):
            self.robot = robot
        else:
            print("Not valid robot object.")

    def control_robot(self, instr):
    # Move the robot in a room given a string with either Swedish or English instructions. 
    # Return True if successful, otherwise False.
        robot = self.get_robot()
        result = False
        if robot:
            if robot.is_valid_instr(instr):
                for letter in instr:
                    direction = robot.get_direction()
                    if letter in "GF":
                        position = robot.get_position()
                        x = position[0]
                        y = position[1]
                        if direction is 0:
                            if self.contains((x, y-1)):
                                robot.set_position((x, y-1))
                                result = True
                        elif direction is 1:
                            if self.contains((x+1, y)):
                                robot.set_position((x+1, y))
                                result = True
                        elif direction is 2:
                            if self.contains((x, y+1)):
                                robot.set_position((x, y+1))
                                result = True
                        elif direction is 3:
                            if self.contains((x-1, y)):
                                robot.set_position((x-1, y))
                                result = True                         
                    elif letter in "VL":
                        robot.set_direction((direction-1)%4)
                        result = True
                    elif letter in "HR":
                        robot.set_direction((direction+1)%4)
                        result = True
                    else:
                        print("Error: Illegal instructions given.")
                        result = False
                print("Robot's position and direction: " + str(robot.get_position()) + " " + robot.get_direction_letter())
            else:
                print("Error: Illegal instructions given.")
                result = False
        else:
            print("Error: The room has no robot.")
            result = False
        return result


class Robot:
    # The robot always faces north (N) at the start. It needs a start position (x,y).
    def __init__(self, start_position):
        self.direction = 0
        self.position = None

        if start_position[0] >= 0 and start_position[1] >= 0:
                self.position = start_position
        else:
            print("Error: The given start position is invalid")

        self.start_position = start_position

    def get_position(self):
    # Return the position (x,y) of the robot
        return self.position
    
    def get_start_position(self):
    # Return the start position (x,y) of the robot
        return self.start_position
    
    def get_direction(self):
    # Return the direction ("N" north: 0, "Ö" east: 1, "S" south: 2, "V" west: 3) of the robot as a number
        return self.direction
    
    def set_direction(self, direction):
    # Set the direction ("N" north, "Ö" east, "S" south, "V" west) of the robot
        self.direction = direction

    def get_direction_letter(self):
    # Return the direction ("N" north: 0, "Ö" east: 1, "S" south: 2, "V" west: 3) of the robot as a letter
        direction_text = "N"
        if self.get_direction() is 1:
            direction_text = "Ö"
        elif self.get_direction() is 2:
            direction_text = "S"
        elif self.get_direction() is 3:
            direction_text = "V"
        else:
            print("Error")
        return direction_text

    def set_position(self, position):
    # Set the position (x,y) of the robot
        self.position = position

    def get_number_of_instr(self, instr):
    # Return the number of instructions 
        return len(instr)

    def is_empty_string(self, instr):
        # Return true if the string is empty
        result = True
        if self.get_number_of_instr(instr) is 0:
            result = True
        else:
            result = False
        return result  

    def is_eng_instr(self, instr):
        # Return true if the instructions should be evaluated as English
        result = False
        if not self.is_empty_string(instr):
            first_letter = instr[0]
            if first_letter in "LRF":
                result = True
            else:
                result = False  
        else:
            result = False
        return result

    def is_swe_instr(self, instr):
        # Return true if the instructions should be evaluated as Swedish
        result = False
        if not self.is_empty_string(instr):
            first_letter = instr[0]
            if first_letter in "VHG":
                result = True
            else:
                result = False  
        else:
            result = False
        return result      

    def is_valid_instr(self, instr):
        # Return true if the given instructions consist of only the right letters (VHG or LRF)
        result = False
        if isinstance(instr, str):
            if self.is_swe_instr(instr):
                for letter in instr:
                    if letter not in "VHG":
                        return False
                result = True

            if self.is_eng_instr(instr):
                for letter in instr:
                    if letter not in "LRF":
                        return False
                result = True

        return result


def main():
    robot = Robot((1,2))
    room = Room((5,5), "R")
    room.set_robot(robot)
    room.control_robot("HGHGGHGHG") # Should print (1, 3) N

    robot = Robot((0,0))
    room = Room((10), "C")
    room.set_robot(robot)
    room.control_robot("RRFLFFLRF") # Should print (3, 1) Ö


if __name__ == "__main__":
    main()

