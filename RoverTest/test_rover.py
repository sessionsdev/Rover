
from rover import Rover



def test_create_rover():
    rover = Rover()
    assert rover.x == 0
    assert rover.y == 0
    assert rover.orientation == 'n'

def test_rover_move_forward():
    rover = Rover(1, 5)
    assert rover.y == 5
    rover.move_forward()
    assert rover.y ==6
    rover.rotate('r')
    rover.move_forward()
    assert rover.y == 6
    assert rover.x == 2
    rover.rotate('r')
    rover.move_forward()
    assert rover.y == 5

def test_rover_move_back():
    rover = Rover(1, 5)
    assert rover.y == 5
    rover.move_back()
    assert rover.y == 4
    rover.rotate('r')
    rover.move_back()
    assert rover.x == 0


def test_rover_rotate():
    rover = Rover()
    assert rover.x == 0
    assert rover.orientation == 'n'
    rover.rotate('l')
    assert rover.orientation == 'w'
    rover.rotate('r')
    assert rover.orientation == 'n'
    rover.rotate('r')
    assert rover.orientation == 'e'

def test_accepts_commands():
    """ example commands: mf, mb, rr, rl """
    rover = Rover(0, 0)
    rover.commands('mf')
    assert rover.y == 1
    rover.commands('mf', 'mb')
    assert rover.y == 1
    rover.commands('rr')
    assert rover.orientation == 'e'
    rover.commands('rr')
    assert rover.orientation == 's'
    rover.commands('rl')
    assert rover.orientation == 'e'

def test_rover_str():
    rover = Rover()
    print(rover)

def test_rover_multiple_commands_ending_position():
    rover = Rover()
    rover.commands('mf', 'mf', 'rr', 'mb', 'rr', 'mf', 'rl')
    assert rover.x == -1
    assert rover.y == 1
    assert rover.orientation == 'e'
    print(rover)


# test_create_rover()
# test_rover_move_forward ()
# test_rover_rotate_right()
# test_rover_rotate()
# test_accepts_commands()
# test_rover_move_back()
# test_rover_str()
test_rover_multiple_commands_ending_position()











# convert to pytest



