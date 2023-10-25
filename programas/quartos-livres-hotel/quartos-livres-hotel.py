import random

rooms = [[[False for r in range(20)] for f in range(15)] for b in range(3)]

for i in range(70):
    building_random = random.randint(0,2)
    room_random = random.randint(0,19)
    floor_random = random.randint(0, 14)
    rooms[building_random][floor_random][room_random] = True


vacancy = 0

for building_number in range(3):
    for floor_number in range(15):
        for room_number in range(20):
            if not rooms[building_number][floor_number][room_number]:
                vacancy += 1

print(f'In all three building, the number of rooms vacant are {vacancy}')

rooms_taken = 0
not_taken = False

for building_number in range(3):
    print('--------------------------------')
    print(f'Building {building_number}')

    for floor_number in range(15):
        print(f'\nFloor {floor_number}:')

        for room_number in range(20):
            if rooms[building_number][floor_number][room_number]:
                print(f'room {room_number} taken')
                rooms_taken += 1
        
        if rooms_taken > 0:
            rooms_taken = 0
            continue
        else:
            print('All rooms are vacant')
            rooms_taken = 0