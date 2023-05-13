import nistrng.functions
import numpy as np
from nistrng import Test, Result
from scipy.stats import chisquare, norm


class TurningPointTest(Test):

    def __init__(self):
        # Generate base Test class
        super(TurningPointTest, self).__init__("Turning Point Test", 0.01)

    def _execute(self,
                 bits: np.ndarray):
        """
        Overridden method of Test class: check its docstring for further information.
        """

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
