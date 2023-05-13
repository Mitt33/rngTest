from nistrng import Test, Result
from scipy.special import comb
import numpy as np
from collections import defaultdict
from scipy.stats import chisquare


class HammingWeightTest(Test):
    """
    The significance value of the test is 0.01.
    """

    def __init__(self):
        # Generate base Test class
        super(HammingWeightTest, self).__init__("Hamming Weight Test", 0.01)

    def _execute(self,
                 bits: np.ndarray):
        """
        Overridden method of Test class: check its docstring for further information.
        """

        subseqs = np.array_split(bits, len(bits) // 8)

        # Compute hamming weight for each byte
        hamming_weights = np.array([np.count_nonzero(byte) for byte in subseqs])

        # Create dictionary for each possible occurrence of hamming weight
        hw_counts = defaultdict(int)
        for hw in hamming_weights:
            hw_counts[hw] += 1

        # Compute expected values of occurrences for each category
        n = len(subseqs)
        expected = np.zeros(8)
        for i in range(1, 9):
            expected[i - 1] = n * (1 / 2) ** 8 * comb(8, i)

        observed = np.array([hw_counts[i] for i in range(1, 9)])
        scaled_observed_values = observed * np.sum(expected) / np.sum(observed)

        _, p = chisquare(scaled_observed_values, expected)
        score = p
        if score >= self.significance_value:
            return Result(self.name, True, np.array(score))
        return Result(self.name, False, np.array(score))

    def is_eligible(self,
                    bits: np.ndarray) -> bool:
        return True
