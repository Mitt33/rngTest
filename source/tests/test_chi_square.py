import numpy
import math

# Import required src
import numpy as np
from nistrng import Test, Result, unpack_sequence
from scipy.stats import chisquare


class ChiSquareTest(Test):
    """
    The significance value of the test is 0.01.
    """

    def __init__(self):
        # Generate base Test class
        super(ChiSquareTest, self).__init__("Chi Square Test", 0.01)

    def _execute(self,
                 bits: numpy.ndarray):
        """
        Overridden method of Test class: check its docstring for further information.
        """
        observed_frequencies = [np.count_nonzero(bits == 0), np.count_nonzero(bits == 1)]

        # Calculate the expected frequencies assuming a 50/50 distribution of 0 and 1
        expected_frequencies = [bits.size / 2, bits.size / 2]

        # Perform the chi-square test
        chi2_statistic, p_value = chisquare(observed_frequencies, expected_frequencies)

        # Perform the chi-square test
        chi2_statistic, p_value = chisquare(observed_frequencies, expected_frequencies)

        # Output the results
        print("Chi-square statistic:", chi2_statistic)
        print("p-value:", p_value)
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
