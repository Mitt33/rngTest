import numpy

import numpy as np
from nistrng import Test, Result
from scipy.stats import chi2, kstest


class BirthdaySpacingsTest(Test):
    """
    Doesnt work = maybe with R package?
    nci moc 64 and 32 bits numbeers" https://www.pcg-random.org/posts/birthday-test.html
    interval 0-1 file:///C:/Users/martin/Downloads/On_the_performance_of_birthday_spacings_tests_with.pdf

    https://www.researchgate.net/publication/5142801_Some_Difficult-to-Pass_Tests_of_Randomness
    """

    def __init__(self):
        # Generate base Test class
        super(BirthdaySpacingsTest, self).__init__("BirthdaySpacingsTest", 0.01)

    def _execute(self,
                 bits: numpy.ndarray):
        """
        Overridden method of Test class: check its docstring for further information.
        """


        score = 0

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

