import source
from source import generators, test_data, file_reader

if __name__ == '__main__':
    print("_________Program for testing and evaluation of random numbers________")
    choice = input("1: Generate random data to test\n2: Choose file to test \n")

    if choice == "1":
        file_path = generators.generators_setup()
    elif choice == "2":
        file_path = input("Please enter the file path: ") or "generated_data/test_data/random_numbers.txt"
    else:
        print("Choice not valid")
        exit()

    binary_sequence = file_reader.file_read_prep(file_path)
    test_data.test_prep(binary_sequence)
