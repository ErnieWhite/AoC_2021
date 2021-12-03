def main():
    with open('./input.txt', 'r', newline='') as file:
        sonar_readings = file.readlines()

    previous_depth = int(sonar_readings[0])
    increase = 0
    for sonar_reading in sonar_readings[1:]:
        current_depth = int(sonar_reading)
        if current_depth and previous_depth < current_depth:
            increase += 1
        previous_depth = current_depth
    print(increase)


if __name__ == '__main__':
    main()
