import math

import numpy as np
from nistrng import Test, Result
from scipy.stats import chisquare


class LempelZivCompressionTest(Test):
    """
    The significance value of the test is 0.01.
    another test as a poker or serial test

    corrections: https://www.researchgate.net/publication/294756057_Revisions_to_the_Spectral_Test_and_the_Lempel-Ziv_Compression_Test_in_the_NIST_Statistical_Test_Suite
    question:  https://crypto.stackexchange.com/questions/129/why-did-nist-remove-the-lempel-ziv-compression-test-from-the-statistical-test-su
    nist 2002: https://csrc.nist.gov/publications/detail/sp/800-22/archive/2001-05-15
    hard paper: file:///C:/Users/martin/Downloads/A_Randomness_Test_Based_on_T-Complexity.pdf
    """

    def __init__(self):
        # Generate base Test class
        self._sequence_size_min: int = 1000000
        super(LempelZivCompressionTest, self).__init__("LempelZivCompressionTest", 0.01)

    def _execute(self,
                 bits: np.ndarray):
        """
        Overridden method of Test class: check its docstring for further information.
        """

        bits = bits[:1000000]

        unique_subseqs = []
        # Initialize an empty string to store the current subsequence
        current_subseq = ""
        # Iterate through the binary sequence
        for bit in bits:
            # Add the current bit to the current subsequence
            current_subseq += str(bit)
            # If the current subsequence is not in the dictionary, add it
            if current_subseq not in unique_subseqs:
                unique_subseqs.append(current_subseq)
                current_subseq = ""
            # Compare the current subsequence with the dictionary
            # and update the count if it is already present

        dict_len = len(unique_subseqs)
        mu = 69586.25
        sigma = math.sqrt(70.48718)
        score = (1 / 2) * math.erfc((mu - dict_len)/(math.sqrt(2 * (sigma ** 2))))

        if score >= self.significance_value:
            return Result(self.name, True, np.array(score))
        return Result(self.name, False, np.array(score))

    def is_eligible(self,
                    bits: np.ndarray) -> bool:
        """
        Overridden method of Test class: check its docstring for further information.
        """
        # for continous generated_data: transformation?
        if bits.size < self._sequence_size_min:
            return False
        return True
