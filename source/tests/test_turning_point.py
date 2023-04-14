import nistrng.functions
import numpy as np
from nistrng import Test, Result
from scipy.stats import chisquare, norm


class TurningPointTest(Test):
    """
    The significance value of the test is 0.01.
    test bodů zvratu
    https://katedry.pf.jcu.cz/kma/wp-content/uploads/2020/10/crek-prednaska_12.pdf
    https://is.muni.cz/el/1431/jaro2015/M6444/um/38997543/prednaska2.pdf
    """

    def __init__(self):
        # Generate base Test class
        super(TurningPointTest, self).__init__("Turning Point Test", 0.01)

    def _execute(self,
                 bits: np.ndarray):
        """
        Overridden method of Test class: check its docstring for further information.
        """

        # num_turning_points = np.sum(bits[1:] != bits[:-1])
        # # Step 3: Calculate the expected number of turning points
        # n = len(bits)
        # mean = 2 * (n - 1) / 3
        # variance = np.sqrt(16 * n / 90)
        # # Step 4: Calculate the test statistic and p-value
        # z = (num_turning_points - mean) / variance
        # p = 2 * (1 - norm.cdf(abs(z)))
        # score = p

        ints = nistrng.functions.unpack_sequence(bits)
        turn_points = 0
        for i in range(1, len(ints) - 1):
            if (ints[i - 1] < ints[i] and ints[i] > ints[i + 1]) or (ints[i - 1] > ints[i] and ints[i] < ints[i + 1]):
                turn_points += 1
        n = len(ints)
        mean = 2 * (n - 2) / 3
        variance = np.sqrt(16 * n / 90)
        z = (turn_points - mean) / variance
        p = 2 * (1 - norm.cdf(abs(z)))
        score = p

        if score >= self.significance_value:
            return Result(self.name, True, np.array(score))
        return Result(self.name, False, np.array(score))

    def is_eligible(self,
                    bits: np.ndarray) -> bool:
        return True
