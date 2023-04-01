import os
import sys

import numpy as np
from nistrng import *
import secrets
import time


def generators_setup():
    generators = {'1': 'python numpy default PRNG - Mersenne Twister',
                  '2': 'Secrets - secure',
                  '3': 'Linear Congruential',
                  '4': 'Xorshift',
                  '5': "Linear Feedback Shift Register - bad on purpose",
                  '6': "OS generator",
                  '7': "test",
                  }
    print('Generators available: ')
    for key, value in generators.items():
        print(f'{key}. {value}')

    choice = input("Choose a generator: ")
    n_bits = int(input("Enter number of bits to generate: "))
    if choice == '1':
        generator = MersenneTwister(n_bits)
    elif choice == '2':
        generator = GenerateSecrets(n_bits)
    elif choice == '3':
        generator = LinearCongruentialGenerator(n_bits)
    elif choice == '4':
        generator = Xorshift(n_bits)
    elif choice == '5':
        generator = LinearFeedbackShiftRegister(n_bits)
    elif choice == '6':
        generator = SystemGen(n_bits)
    elif choice == '7':
        generator = TestGen(n_bits)
    else:
        print('Choice of generator not valid')
        exit()
    random_sequence = generator.generate_bits()
    print("random_sequence generated", random_sequence)
    filename = generator.save_to_file()
    return filename


class BitGenerator:
    def __init__(self, bit_length):
        self.bits = np.ndarray
        self.bit_length = bit_length

    def generate_bits(self):
        pass

    def save_to_file(self):
        filename_bin = f"generated_data/{type(self).__name__}_{self.bit_length}_bits.bin"
        with open(filename_bin, "wb") as f:
            f.write(self.bits)

        # filename = f"generated_data/{type(self).__name__}_{self.bit_length}_bits.txt"
        # with open(filename, "w") as f:
        #     for bit in self.bits:
        #         f.write(str(bit) + "\n")
        return filename_bin


class MersenneTwister(BitGenerator):
    """Classic random generator in Python - based on mersenne twister

    https://numpy.org/doc/stable/reference/random/index.html
    https://github.com/bashtage/randomgen
    """

    def generate_bits(self):
        sequence = np.random.randint(2, size=(self.bit_length,), dtype=np.int8)
        self.bits: np.ndarray = sequence
        # bytes_sequence: np.ndarray = np.random.randint(-128, 127, byte_length, dtype=np.int8)
        # self.bits: np.ndarray = pack_sequence(bytes_sequence)[:self.bit_length]
        return self.bits


class GenerateSecrets(BitGenerator):

    def generate_bits(self):
        """
        function to generate random amount of bits with *secrets* module.
        (function generates bytes, convert them to  int8 and then to bits and stores them
        in binary file)
        secrets module is based on os.urandom(), which is in win based on CryptGenRanom (sha-1?)

        https://docs.python.org/3/library/secrets.html
        """
        random_bytes = secrets.token_bytes((self.bit_length + 7) // 8)
        random_int8 = np.frombuffer(random_bytes, dtype=np.int8)
        self.bits: np.ndarray = pack_sequence(random_int8)[:self.bit_length]
        return self.bits


class LinearCongruentialGenerator(BitGenerator):

    def generate_bits(self):
        """
        linear congruential generator with parameters:
        -multiplier a, incement c, modulus m
            BSD formula: 1103515245, 12345, 2 ** 31
            Microsoft: 214013, 2531011, m**31
        """
        a = 1103515245
        c = 12345
        m = 2 ** 31
        # initial seed (current time in seconds)
        seed = round(time.time())
        num_bytes = (self.bit_length + 7) // 8
        random_int8 = np.zeros(num_bytes, dtype=np.int8)
        for i in range(num_bytes):
            seed = (a * seed + c) % m
            random_int8[i] = (seed >> 23) - 128
        self.bits: np.ndarray = pack_sequence(random_int8)[:self.bit_length]
        return self.bits


class Xorshift(BitGenerator):
    """

    """

    def generate_bits(self):
        a = 13
        b = 17
        c = 5
        seed = round(time.time())
        bits = []
        for i in range(self.bit_length):
            # generate the next pseudo-random number
            seed ^= (seed << a)
            seed ^= (seed >> b)
            seed ^= (seed << c)
            # extract the least significant bit
            bit = seed & 1
            # append the bit to the list
            bits.append(bit)
        self.bits = np.array(bits, dtype=np.uint8).astype(np.int8)
        return self.bits


class LinearFeedbackShiftRegister(BitGenerator):

    def generate_bits(self):
        """
        bad on purpose lfsr generator with period 2^4-1 = 15 bits
        """
        bits = []
        state = 0b0101
        # Initialize the LFSR with the seed value
        for _ in range(self.bit_length):
            newbit = (state ^ (state >> 1)) & 1
            state = (state >> 1) | (newbit << 3)
            bits.append(state & 0b1)

        # start_state = 1 << 15 | 1
        # lfsr = start_state
        # period = 0
        # while True:
        #     # taps: 16 15 13 4; feedback polynomial: x^16 + x^15 + x^13 + x^4 + 1
        #     bit = (lfsr ^ (lfsr >> 1) ^ (lfsr >> 3) ^ (lfsr >> 12)) & 1
        #     lfsr = (lfsr >> 1) | (bit << 15)
        #     period += 1
        #     if (lfsr == start_state):
        #         print(period)
        #         break

        self.bits: np.ndarray = np.array(bits, dtype=np.uint8).astype(np.int8)
        return self.bits

class SystemGen(BitGenerator):
    """
    https://download.microsoft.com/download/1/c/9/1c9813b8-089c-4fef-b2ad-ad80e79403ba/Whitepaper%20-%20The%20Windows%2010%20random%20number%20generation%20infrastructure.pdf
    https://docs.python.org/3/library/os.html#os.urandom

    """

    def generate_bits(self):
        random_bytes = os.urandom((self.bit_length + 7) // 8)
        random_int8 = np.frombuffer(random_bytes, dtype=np.int8)
        self.bits: np.ndarray = pack_sequence(random_int8)[:self.bit_length]
        print(random_bytes)
        print(self.bits)
        return self.bits

class TestGen(BitGenerator):

    def generate_bits(self):
        int_list = np.random.randint(low=0, high=2 ** 31, size=100, dtype=np.uint32)

        # Save the list to a file
        with open('generated_data/integers32.txt', 'w') as f:
            for i in int_list:
                f.write(str(i) + '\n')
        sys.exit()


"""
randu: bad generator

additive congruential method

compare:
https://realpython.com/python-random/



"""
