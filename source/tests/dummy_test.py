import nistrng.functions
import numpy as np
from nistrng import Test, Result
from scipy.stats import chisquare, norm
import numpy as np



class DummyTest(Test):
    """
    The significance value of the test is 0.01.
    """

    def __init__(self):
        # Generate base Test class
        super(DummyTest, self).__init__("DummyTest", 0.01)

    def _execute(self,
                 bits: np.ndarray):
        """
        Overridden method of Test class: check its docstring for further information.
        """



    def is_eligible(self,
                    bits: np.ndarray) -> bool:
        return True
