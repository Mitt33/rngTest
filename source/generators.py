import os
import random
import sys

import numpy as np
from nistrng import *
import secrets
import time

generators_list = ["Python random",
                   "Python secrets",
                   "LCG",
                   "Xorshift",
                   "LFSR - bad",
                   "test",
                   ]


def generators_setup(selected_generator, n_bits):
    if selected_generator == "Python random":
        generator = PythonRandom(n_bits)
    elif selected_generator == "Python secrets":
        generator = PythonSecrets(n_bits)
    elif selected_generator == "LCG":
        generator = LinearCongruentialGenerator(n_bits)
    elif selected_generator == "Xorshift":
        generator = Xorshift(n_bits)
    elif selected_generator == "LFSR - bad":
        generator = LinearFeedbackShiftRegister(n_bits)
    elif selected_generator == "test":
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


class PythonRandom(BitGenerator):
    """Classic random generator in Python - based on mersenne twister

    https://numpy.org/doc/stable/reference/random/index.html
    https://github.com/bashtage/randomgen
    """

    def generate_bits(self):
        # sequence = np.random.randint(2, size=(self.bit_length,), dtype=np.int8)
        sequence = [random.randint(0, 1) for _ in range(self.bit_length)]
        self.bits: np.ndarray = np.array(sequence, dtype=np.int8)
        return self.bits


class PythonSecrets(BitGenerator):

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
        - glibc formula
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
        period = 2^n-1 = 15,
        polynomial = x^4 + x^3 + 1
        seed value : 8 bits from current time
        """
        current_time = int(time.time())
        state = current_time & 0b1111
        bits = []
        # state = 0b01010101
        for _ in range(self.bit_length):
            newbit = (state ^ (state >> 3) ^ (state >> 4)) & 1
            state = (state >> 1) | (newbit << 3)
            bits.append(state & 0b1)

        self.bits: np.ndarray = np.array(bits, dtype=np.uint8).astype(np.int8)
        return self.bits


# class SystemGen(BitGenerator):
#     """
#     https://download.microsoft.com/download/1/c/9/1c9813b8-089c-4fef-b2ad-ad80e79403ba/Whitepaper%20-%20The%20Windows%2010%20random%20number%20generation%20infrastructure.pdf
#     https://docs.python.org/3/library/os.html#os.urandom
#
#     """
#
#     def generate_bits(self):
#         random_bytes = os.urandom((self.bit_length + 7) // 8)
#         random_int8 = np.frombuffer(random_bytes, dtype=np.int8)
#         self.bits: np.ndarray = pack_sequence(random_int8)[:self.bit_length]
#         print(random_bytes)
#         print(self.bits)
#         return self.bits


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
