def count_bits(lst, num):
    count = 0
    for e in lst:
        if e[num] == '1':
            count += 1
        else:
            count -= 1
    return count


def main():
    with open('input.txt', 'r') as data_file:
        data = data_file.read().splitlines()
        current_oxygen_data = data.copy()
        current_co2_data = data.copy()
        for bit_num in range(len(current_oxygen_data[0])):
            if len(current_oxygen_data) > 1:
                oxy_count = count_bits(current_oxygen_data, bit_num)
                oxy_bit = '1' if oxy_count >= 0 else '0'
                current_oxygen_data = [x for x in current_oxygen_data if x[bit_num] == oxy_bit]
            if len(current_co2_data) > 1:
                co2_count = count_bits(current_co2_data, bit_num)
                co2_bit = '0' if co2_count >= 0 else '1'
                current_co2_data = [x for x in current_co2_data if x[bit_num] == co2_bit]

            print(data)
            print(f'Oxy: {current_oxygen_data} {int("".join(current_oxygen_data), 2)} {oxy_bit}')
            print(f'Co2: {current_co2_data} {int("".join(current_co2_data), 2)} {co2_bit}')
            print()
            print(int("".join(current_oxygen_data), 2)*int("".join(current_co2_data), 2))


if __name__ == '__main__':
    main()

