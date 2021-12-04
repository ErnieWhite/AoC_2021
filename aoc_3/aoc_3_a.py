def main():
    with open('input.txt', 'r') as data_file:
        bits = None
        while line := data_file.readline():
            clean_line = line.strip()
            if bits is None:
                bits = [0 for _ in list(clean_line)]
            for bit_num, bit in enumerate(list(clean_line)):
                print(f'{bit}', end='\t')
                bits[bit_num] += 1 if bit == '1' else -1
        print()
        gamma_rate = int(''.join(['1' if x > 0 else '0' for x in bits]), 2)
        epsilon_rate = int(''.join(['0' if x > 0 else '1' for x in bits]), 2)
        print(gamma_rate, epsilon_rate)
        print(f'Power consumption: {gamma_rate * epsilon_rate}')


if __name__ == '__main__':
    main()

