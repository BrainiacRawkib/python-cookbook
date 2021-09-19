from ch_08.ex_24 import Room, House


if __name__ == '__main__':
    h1 = House('h1', 'Cape')
    h1.add_room(Room('Master Bedroom', 14, 21))
    h1.add_room(Room('Living Room', 18, 20))
    h1.add_room(Room('Kitchen', 12, 16))
    h1.add_room(Room('Office', 12, 12))

    h2 = House('h2', 'Ranch')
    h2.add_room(Room('Master Bedroom', 14, 21))
    h2.add_room(Room('Living Room', 18, 20))
    h2.add_room(Room('Kitchen', 12, 16))

    h3 = House('h3', 'Split')
    h3.add_room(Room('Master Bedroom', 14, 21))
    h3.add_room(Room('Living Room', 18, 20))
    h3.add_room(Room('Kitchen', 15, 17))
    h3.add_room(Room('Office', 12, 16))

    houses = [h1, h2, h3]

    print('Is h1 bigger than h2?', h1 > h2)  # prints True
    print('Is h2 smaller than h3?', h2 < h3)  # prints True
    print('Is h2 greater than or equal to h1?', h2 >= h1)  # Prints False
    print('Which one is biggest?', max(houses))  # Prints 'h3: 1101-square-foot Split'
    print('Which is smallest?', min(houses))  # Prints 'h2: 846-square-foot Ranch