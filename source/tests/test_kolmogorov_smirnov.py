import numpy
import math

# Import required src
import numpy as np
from nistrng import Test, Result, unpack_sequence
from scipy.stats import kstest


class KolmogorovSmirnovTest(Test):
    """
    Monobit test as described in NIST paper: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf
    The focus of the test is the proportion of zeroes and ones for the entire sequence. The purpose of this test is to determine
    whether the number of ones and zeros in a sequence are approximately the same as would be expected for a truly random sequence.
    The test assesses the closeness of the fraction of ones to 1/2, that is, the number of ones and zeroes in a sequence
    should be about the same.

    The significance value of the test is 0.01.
    """
    def __init__(self):
        # Generate base Test class
        super(KolmogorovSmirnovTest, self).__init__("KolmogorovSmirnovTest", 0.01)

    def _execute(self,
                 bits: numpy.ndarray):
        """
        Overridden method of Test class: check its docstring for further information.
        """
        cumulative_sum = np.cumsum(bits)

        # Normalize the cumulative sum to obtain the empirical distribution function
        empirical_cdf = cumulative_sum / np.max(cumulative_sum)

        # Generate a uniform distribution as the null hypothesis
        null_hypothesis = np.random.uniform(size=900)

        # Apply the KS test to compare the empirical distribution function with the null hypothesis
        ks_statistic, p_value = kstest(empirical_cdf, 'uniform')

        # Print the results
        print(f"KS statistic: {ks_statistic}")
        print(f"P-value: {p_value}")

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
