import math
import numpy as np
from nistrng import Test, Result


class LempelZivCompressionTest(Test):
    def __init__(self):
        # Generate base Test class
        self._sequence_size_min: int = 1000000
        super(LempelZivCompressionTest, self).__init__("Lempel-Ziv Compression Test", 0.01)

    def _execute(self,
                 bits: np.ndarray):
        """
        Implementation of Lempel-Ziv Compression Test
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
        sigma = math.sqrt(70.448718)
        score = (1 / 2) * math.erfc((mu - dict_len)/(math.sqrt(2 * (sigma ** 2))))

        if score >= self.significance_value:
            return Result(self.name, True, np.array(score))
        return Result(self.name, False, np.array(score))

    def is_eligible(self,
                    bits: np.ndarray) -> bool:
        if bits.size < self._sequence_size_min:
            return False
        return True
