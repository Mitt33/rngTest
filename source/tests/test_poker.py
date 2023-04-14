import numpy as np
from nistrng import Test, Result
from scipy.stats import chisquare


class PokerTest(Test):
    """
    The significance value of the test is 0.01.
    Poker test with hands of three: hands of 4 is another posiblle way, maybe add?
    degrees of freedom - 4 categories (types of block) = degrees is 3?
        degrees_of_freedom = 2**3 - 1 - spíš to za mě řeší samo
    https://www.iosrjournals.org/iosr-jm/papers/Vol12-issue1/Version-5/D012151723.pdf
    https://thescipub.com/pdf/jcssp.2012.1353.1357.pdf
    """

    def __init__(self):
        # Generate base Test class
        super(PokerTest, self).__init__("Poker Test", 0.01)

    def _execute(self,
                 bits: np.ndarray):
        """
        Overridden method of Test class: check its docstring for further information.
        """
        remainder = len(bits) % 3

        # if remainder is not zero, cut the ndarray
        if remainder != 0:
            bits = bits[:-remainder]

        subsequences = np.split(bits, len(bits) / 3)
        num_subsequences = len(subsequences)

        # initialize counters for each case
        zero_ones = 0
        one_ones = 0
        two_ones = 0
        all_ones = 0

        # iterate through subsequences and count cases
        for subseq in subsequences:
            ones_count = np.count_nonzero(subseq)
            if ones_count == 0:
                zero_ones += 1
            elif ones_count == 1:
                one_ones += 1
            elif ones_count == 2:
                two_ones += 1
            else:
                all_ones += 1

        exp_zero_ones = num_subsequences * (1 / 8)
        exp_one_ones = num_subsequences * (3 / 8)
        exp_two_ones = num_subsequences * (3 / 8)
        exp_all_ones = num_subsequences * (1 / 8)

        observed = np.array([zero_ones, one_ones, two_ones, all_ones])
        expected = np.array([exp_zero_ones, exp_one_ones, exp_two_ones, exp_all_ones])
        _, score = chisquare(observed, f_exp=expected)

        if score >= self.significance_value:
            return Result(self.name, True, np.array(score))
        return Result(self.name, False, np.array(score))

    def is_eligible(self,
                    bits: np.ndarray) -> bool:
        """
        Overridden method of Test class: check its docstring for further information.
        """
        # for continous generated_data: transformation?
        return True

