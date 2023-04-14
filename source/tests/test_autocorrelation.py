import math

import nistrng.functions
import numpy as np
import scipy
from nistrng import Test, Result
from scipy.stats import chisquare, norm


class AutocorrelationTest(Test):
    """
    The significance value of the test is 0.01.
    jen jeden lag - více - velká false pozitivita, početní náročnost
    """

    def __init__(self):
        # Generate base Test class
        super(AutocorrelationTest, self).__init__("Autocorrelation Test", 0.01)

    def _execute(self,
                 bits: np.ndarray):
        """
        Overridden method of Test class: check its docstring for further information.
        """
        data = nistrng.functions.unpack_sequence(bits)
        data_length = len(data)
        scores = []
        mean = np.mean(data)
        variance = np.var(data)
        for lag in range(1, 11):
            autocorr = 0
            for i in range(data_length - lag):
                autocorr += (data[i] - mean) * (data[i + lag] - mean)
            autocorr /= (data_length - lag) * variance

            se = 1 / math.sqrt(data_length - lag)

            z_score = autocorr / se
            p_value = 2 * norm.cdf(-abs(z_score))
            scores.append(p_value)

        for score in scores:
            if score < self.significance_value:
                return Result(self.name, False, np.array(score))
        else:
            return Result(self.name, True, np.array(scores))

    def is_eligible(self,
                    bits: np.ndarray) -> bool:
        """
        Overridden method of Test class: check its docstring for further information.
        """
        return True
