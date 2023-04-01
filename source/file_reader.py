import re

import numpy as np
from nistrng import pack_sequence


def file_read_prep(file_path):
    reader = FileReader(file_path)
    reader.read_file()
    binary_sequence: np.ndarray = reader.get_data()
    print("Data inserted: ", binary_sequence)
    print("File type: ", reader.get_file_type())

    return binary_sequence


class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.file_type = None
        self.bit_length = None

    def read_file(self):

        # Determine data type from file extension
        ext = self.file_path.split('.')[-1].lower()

        if ext == 'txt':
            self.file_type = "txt"
            with open(self.file_path, 'r') as f:
                data = f.read()
            numbers_only = []
            for item in re.findall(r'-?\d+(?:\.\d+)?', data):
                numbers_only.append(item)
            # list_splitted = re.split(",|\s|\n", data)
            float_lst = [float(item) for item in numbers_only]
            is_floats_zero_to_one = True
            for num in float_lst:
                if not 0 <= num <= 1:
                    is_floats_zero_to_one = False
                    break

            if is_floats_zero_to_one:
                # convert data to a float ndarray
                bits = []
                for num in float_lst:
                    bit = round(num)
                    bits.append(bit)
                data = np.array(list(bits), dtype=np.int8)
                self.data: np.ndarray = data

            # Check if data consists of only 0's and 1's
            elif set(data) <= {'0', '1'}:
                # Data is already in bit format
                bits = np.array(list(data), dtype=np.int8)
                self.data: np.ndarray = bits

            else:
                data = np.array(numbers_only, dtype=np.uint8)   # takhle se čísla oříznou na unit8 - konverze je pak ok
                # data = np.array(numbers_only)
                bits = np.unpackbits(data.astype(np.uint8))
                self.data: np.ndarray = bits

        elif ext == 'bin':
            self.file_type = "bin"
            # Convert binary data to bit sequence
            with open(self.file_path, 'rb') as f:
                data: np.ndarray = np.fromfile(f, dtype=np.int8)
                self.data: np.ndarray = data

        else:
            raise ValueError('Unsupported file type')

    def get_data(self):
        return self.data

    def get_file_type(self):
        return self.file_type


