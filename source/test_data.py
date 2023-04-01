import os.path

import numpy as np
from nistrng import *
import csv

from source import create_battery_of_tests


def test_prep(binary_sequence):
    all_test_dict = create_battery_of_tests.create_all_battery()
    eligible_battery = create_eligible_battery(binary_sequence, all_test_dict)
    print_eligible_battery(eligible_battery, all_test_dict)

    results = test_data(binary_sequence, eligible_battery)
    print_results(results)
    save_results(results)


def create_eligible_battery(binary_sequence: np.ndarray, all_battery):
    # Check the eligibility of the test and generate an eligible battery from the default NIST-sp800-22r1a battery
    eligible_battery: dict = check_eligibility_all_battery(binary_sequence, all_battery)

    return eligible_battery


def print_eligible_battery(eligible_battery, all_battery):
    # Print the eligible tests
    print("number of eligible test out of ", len(all_battery), "are: ", len(eligible_battery))
    print("Eligible testyy from NIST-SP800-22r1a:")
    for name in eligible_battery.keys():
        print("-" + name)


def test_data(binary_sequence: np.ndarray, eligible_battery):
    # Test the sequence on the eligible testyy
    results = run_all_battery(binary_sequence, eligible_battery, False)
    return results


def print_results(results):
    # Print test_results one by one
    print("Test test_results:")
    for result, elapsed_time in results:
        if result.passed:
            print("- PASSED - score: " + str(
                np.round(result.score, 3)) + " - " + result.name + " - elapsed time: " + str(elapsed_time) + " ms")
        else:
            print("- FAILED - score: " + str(
                np.round(result.score, 3)) + " - " + result.name + " - elapsed time: " + str(elapsed_time) + " ms")


def save_results(results):
    # saves test_results of testing (nist test at this time) to csv file for further evaluation
    filename = "test_results/test_results.csv"
    file_exists = os.path.isfile(filename)
    with open(filename, "a", newline="") as csvfile:
        fieldnames = ["name", "score", "result", "time"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        for result, elapsed_time in results:
            writer.writerow({"name": result.name, "score": np.round(result.score, 3),
                             "result": "passed" if result.passed else "failed", "time": str(elapsed_time) + "ms"})
