import math
import nistrng.functions
import numpy as np
from nistrng import Test, Result
from scipy.stats import norm


class AutocorrelationTest(Test):

    def __init__(self):
        # Generate base Test class
        super(AutocorrelationTest, self).__init__("Autocorrelation Test", 0.01)

    def _execute(self,
                 bits: np.ndarray):
        """
        Implementation of Autocorrelation Test
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
        return True
