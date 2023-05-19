import random
import numpy as np
from nistrng import *
import secrets
import time

generators_list = ["Python random",
                   "Python secrets",
                   "LCG",
                   "Xorshift",
                   "LFSR - bad RNG!",
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
    elif selected_generator == "LFSR - bad!":
        generator = LinearFeedbackShiftRegister(n_bits)
    else:
        print('Choice of generator not valid')
        exit()
    generator.generate_bits()
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
        return filename_bin


class PythonRandom(BitGenerator):
    """
    Classic random generator in Python - based on mersenne twister
    """

    def generate_bits(self):
        sequence = [random.randint(0, 1) for _ in range(self.bit_length)]
        self.bits: np.ndarray = np.array(sequence, dtype=np.int8)
        return self.bits


class PythonSecrets(BitGenerator):
    """
    Function to generate random amount of bits with *secrets* module.
    """

    def generate_bits(self):
        random_bytes = secrets.token_bytes((self.bit_length + 7) // 8)
        random_int8 = np.frombuffer(random_bytes, dtype=np.int8)
        self.bits: np.ndarray = pack_sequence(random_int8)[:self.bit_length]
        return self.bits


class LinearCongruentialGenerator(BitGenerator):
    """
    - linear congruential generator with parameters:
    - multiplier a, increment c, modulus m
    - glibc formula
    """

    def generate_bits(self):
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
    Implementation of Xorshift RNG
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
        for _ in range(self.bit_length):
            newbit = (state ^ (state >> 3) ^ (state >> 4)) & 1
            state = (state >> 1) | (newbit << 3)
            bits.append(state & 0b1)

        self.bits: np.ndarray = np.array(bits, dtype=np.uint8).astype(np.int8)
        return self.bits

