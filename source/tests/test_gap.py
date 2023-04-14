import numpy
import math

# Import required src
import numpy as np
from nistrng import Test, Result, unpack_sequence
from scipy.stats import chisquare, chi2


class GapTest(Test):
    """
    The significance value of the test is 0.01.
    """

    def __init__(self):
        # Generate base Test class
        super(GapTest, self).__init__("Gap Test", 0.01)

    def _execute(self,
                 bits: numpy.ndarray):
        """
        Overridden method of Test class: check its docstring for further information.
        """
        # Compute the lengths of the gaps between consecutive ones in the sequence
        gaps = []
        count = 0
        for bit in bits:
            if bit == 0:
                count += 1
            else:
                if count > 0:
                    gaps.append(count)
                    count = 0
        if count > 0:
            gaps.append(count)

        # Count the number of occurrences of each gap length
        gap_counts = {}
        for gap_length in set(gaps):
            gap_counts[gap_length] = gaps.count(gap_length)

        # Compute the expected number of occurrences of each gap length under a uniform distribution
        n = len(bits)
        p = 0.5  # 1 - np.sum(bits) / n
        expected_counts = {}
        for gap_length, gap_count in gap_counts.items():
            # expected_counts[gap_length] = (n - len(gaps) * p) * ((1 - p) ** gap_length) * p
            expected_counts[gap_length] = len(gaps) * (p ** gap_length)

        observed_counts = np.array([gap_counts[gap_length] for gap_length in gap_counts.keys()])
        expected_counts = np.array([expected_counts[gap_length] for gap_length in gap_counts.keys()])
        # Scale the observed values to have the same total as the expected values
        scaled_observed_values = observed_counts * np.sum(expected_counts) / np.sum(observed_counts)

        # Compute the test statistic and p-value
        chi_squared, p_value = chisquare(scaled_observed_values, f_exp=expected_counts)

        score = p_value
        if score >= self.significance_value:
            return Result(self.name, True, numpy.array(score))
        return Result(self.name, False, numpy.array(score))

    def is_eligible(self,
                    bits: numpy.ndarray) -> bool:
        """
        Overridden method of Test class: check its docstring for further information.
        """
        # for continous generated_data: transformation?
        return True
