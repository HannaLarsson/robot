import unittest
from room import Room
from room import Robot

class TestRobotMethods(unittest.TestCase):
    # Test robot methods 


    # Test robot instructions
    def test_get_number_of_instr(self):
        robot = Robot((1,1))
        self.assertEqual(robot.get_number_of_instr(""), 0)
        self.assertEqual(robot.get_number_of_instr("V"), 1)
        self.assertNotEqual(robot.get_number_of_instr("VV"), 1)

    def test_is_eng_instr(self):
        robot = Robot((1,1))
        self.assertEqual(robot.is_eng_instr("LRL"), True)
        self.assertEqual(robot.is_eng_instr("LB"), True)

        # Test invalid English instructions
        self.assertEqual(robot.is_eng_instr("VRL"), False)
        self.assertEqual(robot.is_eng_instr(""), False)

    def test_is_swe_instr(self):
        robot = Robot((1,1))
        self.assertEqual(robot.is_swe_instr("VHV"), True)
        self.assertEqual(robot.is_swe_instr("VB"), True)

        # Test invalid Swedish instructions
        self.assertEqual(robot.is_swe_instr("LRL"), False)
        self.assertEqual(robot.is_swe_instr(""), False)

    def test_is_valid_instr(self):
        robot = Robot((1,1))
        self.assertEqual(robot.is_valid_instr("VHVG"), True)
        self.assertEqual(robot.is_valid_instr("RLRF"), True)

        # Test invalid instructions
        self.assertEqual(robot.is_valid_instr("VHN"), False)
        self.assertEqual(robot.is_valid_instr(False), False)
        self.assertEqual(robot.is_valid_instr("RLRFB"), False)
        self.assertEqual(robot.is_valid_instr(""), False)

class TestRoomMethods(unittest.TestCase):
    # Test room methods
    
    def test_get_start_position(self):
        robot = Robot((1,1))
        room = Room((10,9), "R")
        room.set_robot(robot)

        self.assertEqual(room.get_start_position(), (1,1))
        self.assertNotEqual(room.get_start_position(), (2,2))

    def test_contains(self):
        robot = Robot((1,1))
        room = Room((10,9), "R")

        # Test valid coordinates for square room
        self.assertEqual(room.contains((1,2)), True)
        self.assertEqual(room.contains((9,8)), True)
        self.assertEqual(room.contains((0,0)), True)

        # Test invalid coordinates for square room
        self.assertEqual(room.contains((100,2)), False)
        self.assertEqual(room.contains((2,11)), False)
        self.assertEqual(room.contains((-1,2)), False)
        self.assertEqual(room.contains((2,-1)), False)
        self.assertEqual(room.contains((8,9)), False)

        # Test valid coordinates for circular room
        room = Room(10, "C")
        self.assertEqual(room.contains((1,2)), True)
        self.assertEqual(room.contains((-1,2)), True)
        self.assertEqual(room.contains((2,-1)), True)
        self.assertEqual(room.contains((6,-6)), True)
        self.assertEqual(room.contains((-6,-6)), True)
        self.assertEqual(room.contains((-6,6)), True)
        self.assertEqual(room.contains((7,5)), True)

        # Test invalid coordinates for circular room
        self.assertEqual(room.contains((100,2)), False)
        self.assertEqual(room.contains((2,11)), False)
        self.assertEqual(room.contains((9,10)), False)
        self.assertEqual(room.contains((5,-8)), False)
        self.assertEqual(room.contains((-9,-3)), False)

    def test_get_size(self):
        room = Room((10,9), "R")

        # Test correct room size (rectangular room)
        self.assertEqual(room.get_size(), (10,9))

        # Test incorrect room size (rectangular room)
        self.assertNotEqual(room.get_size(), (9,10))
        self.assertNotEqual(room.get_size(), (-10,-9))

        # Change the room shape to circular
        room = Room((4), "C")

        # Test correct room size (circular room)
        self.assertEqual(room.get_size(), (4))

        # Test incorrect room size (circular room)
        self.assertNotEqual(room.get_size(), (9))
        self.assertNotEqual(room.get_size(), (-10))

    def test_set_size(self):
        room = Room((10,9), "R")

        # Tests for rectangular room
        self.assertEqual(room.get_size(), (10,9))
        room.set_size(8,8)
        self.assertEqual(room.get_size(), (8,8))

        # Test invalid sizes, size should not change
        room.set_size(0,8)
        self.assertEqual(room.get_size(), (8,8))
        room.set_size(1,-44)
        self.assertEqual(room.get_size(), (8,8))
        room.set_size(0.6,8)
        self.assertEqual(room.get_size(), (8,8))
        room.set_size(1,1.1)
        self.assertEqual(room.get_size(), (8,8))

        # Tests for circular room
        room.set_shape("C")
        room.set_size(10)
        self.assertEqual(room.get_size(), (20))
        room.set_size(8,8)
        self.assertEqual(room.get_size(), (16))

    def test_set_shape(self):
        room = Room((10,9), "R")

        # Test valid shape parameters
        room.set_shape("C")
        self.assertEqual(room.get_shape(), "C")

        room.set_shape("R")
        self.assertEqual(room.get_shape(), "R")

        # Test invalid shape parameters, should not change shape of room
        room.set_shape("r")
        self.assertEqual(room.get_shape(), "R")

        room.set_shape("P")
        self.assertEqual(room.get_shape(), "R")

        room.set_shape("RR")
        self.assertEqual(room.get_shape(), "R")

        room.set_shape("")
        self.assertEqual(room.get_shape(), "R")

        room.set_shape(1)
        self.assertEqual(room.get_shape(), "R")

        room.set_shape(None)
        self.assertEqual(room.get_shape(), "R")

    def test_get_shape(self):
        room = Room((10,9), "R")

        self.assertEqual(room.get_shape(), "R")
        room.set_shape("C")
        self.assertEqual(room.get_shape(), "C")

    def test_get_radius(self):
        room = Room((1), "C")
        self.assertAlmostEqual(room.get_radius(), 1.4142135623730950488)
        room = Room((10), "C")
        self.assertAlmostEqual(room.get_radius(), 10.0498756211208902702192)
        room = Room((0), "C")
        self.assertIsNone(room.get_radius())

    def set_robot(self):
        # Check that when setting the robot object to a room, it updates what robot the room should use correctly.

        room = Room((10,9), "R")
        robot = Robot((1,2))
        room.set_robot(robot)
        self.assertEqual(room.robot, robot)
        self.assertEqual(room.robot.get_position(), (1,2))

        robot2 = Robot((5,5))
        room.set_robot(robot2)
        self.assertEqual(room.robot, robot2)
        self.assertEqual(room.robot.get_position(), (5,5))    

        # Test invalid robot object, the room's robot object should not change.
        room.set_robot("robot")
        self.assertEqual(room.robot, robot2)
        room.set_robot(None)
        self.assertEqual(room.robot, robot2)        

    def test_get_robot(self):
        room = Room((10,9), "R")
        robot = Robot((1,2))
        robot2 = Robot((2,10))
        room.robot = robot

        self.assertEqual(room.get_robot(), robot) 
        room.set_robot(robot2)
        self.assertEqual(room.get_robot(), robot2)

        room.robot = None
        self.assertIsNone(room.get_robot())

    def test_control_robot(self):
        room = Room((10,9), "R")
        robot = Robot((1,2))

        # Test the control_robot function when the room has no robot.
        room.control_robot("HV")

        # Test the control_robot function when a square room has a robot.
        room.set_robot(robot)
        room.control_robot("HVH")
        self.assertEqual(robot.get_position(), (1,2))
        self.assertEqual(robot.get_direction(), 1)

        room.control_robot("VHVHGGGGGGGGGGGG")
        self.assertEqual(robot.get_position(), (9,2))
        self.assertEqual(robot.get_direction(), 1)

        room2 = Room((5,5), "R")
        robot2 = Robot((1,2))
        room2.set_robot(robot2)
        room2.control_robot("GGGVGVGGGGVGGGH")
        self.assertEqual(robot2.get_position(), (3,4))
        self.assertEqual(robot2.get_direction(), 2)

        room3 = Room((5,5), "R")
        robot3 = Robot((1,1))
        room3.set_robot(robot3)
        room3.control_robot("FFLRFFLF")
        self.assertEqual(robot3.get_position(), (0,0))
        self.assertEqual(robot3.get_direction(), 3)

        room4 = Room((5,5), "R")
        robot4 = Robot((4,4))
        room4.set_robot(robot4)
        room4.control_robot("LLLLRRFRLFRRRRF")
        self.assertEqual(robot4.get_position(), (4,4))
        self.assertEqual(robot4.get_direction(), 2)

        room5 = Room((5,5), "R")
        robot5 = Robot((1,2))
        room5.set_robot(robot5)
        self.assertEqual(room5.control_robot("HGHGGHGHG"), True)
        self.assertEqual(robot5.get_position(), (1,3))
        self.assertEqual(robot5.get_direction(), 0)

        self.assertEqual(room5.control_robot(5), False)


        # Test the control_robot function when a circular room has a robot.
        
        room6 = Room(10, "C")
        robot6 = Robot((0,0))
        room6.set_robot(robot6)
        room6.control_robot("RRFLFFLRF")
        self.assertEqual(robot6.get_position(), (3,1))
        self.assertEqual(robot6.get_direction(), 1)

        room6.control_robot("FFFFFF")
        self.assertEqual(robot6.get_position(), (8,1))
        self.assertEqual(robot6.get_direction(), 1)

        room6.control_robot("VGHG")
        self.assertEqual(robot6.get_position(), (9,0))
        self.assertEqual(robot6.get_direction(), 1)


    
if __name__ == '__main__':
    unittest.main()