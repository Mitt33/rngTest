from source.tests import PokerTest, \
    TwoBitTest, LempelZivCompressionTest, HammingWeightTest, AutocorrelationTest, GapTest, TurningPointTest, \
    SerialTestMod
from nistrng.sp800_22r1a import *


def create_all_battery():
    all_test_battery: dict = {
        "Poker Test": PokerTest(),
        "Two Bit Test": TwoBitTest(),
        "Gap Test": GapTest(),
        "Turning Point Test": TurningPointTest(),
        "Autocorrelation Test": AutocorrelationTest(),
        "Hamming Weight Test": HammingWeightTest(),
        "Lempel-Ziv Compression Test": LempelZivCompressionTest(),
    }

    SP800_22R1A_BATTERY_changed: dict = {
        "Monobit": MonobitTest(),
        "Frequency Within Block": FrequencyWithinBlockTest(),
        "Runs": RunsTest(),
        "Longest Run Ones In A Block": LongestRunOnesInABlockTest(),
        "Discrete Fourier Transform": DiscreteFourierTransformTest(),
        "Non Overlapping Template Matching": NonOverlappingTemplateMatchingTest(),
        "Overlapping Template Matching": OverlappingTemplateMatchingTest(),
        "Maurers Universal": MaurersUniversalTest(),
        "Linear Complexity": LinearComplexityTest(),
        "Serial Test": SerialTestMod(),
        "Approximate Entropy": ApproximateEntropyTest(),
        "Cumulative Sums": CumulativeSumsTest(),
        "Random Excursion": RandomExcursionTest(),
        "Random Excursion Variant": RandomExcursionVariantTest(),
        "Binary Matrix Rank": BinaryMatrixRankTest(),
    }
    # nistrng.SP800_22R1A_BATTERY.pop("Serial")  # this is how to delete test from battery, so it can be replaced
    # all_test_battery.update(nistrng.SP800_22R1A_BATTERY)
    all_test_battery.update(SP800_22R1A_BATTERY_changed)

    return all_test_battery


tooltip_dict = {
    "Poker Test": "<h2>Poker Test</h2><p>"
                  "<strong>Approach:</strong> Tests the sequence divided into groups and compares"
                  " the number of occurrences with a truly random sequence.</p>"
                  "<p><strong>Eligibility:</strong> Unrestricted</p>"
                  "<p><strong>Result:</strong> p-value &lt; 0,01 indicates a "
                  "non-random distribution of groups with different combinations of bits  </p>",
    "Two Bit Test": "<h2>Two Bit Test</h2><p>"
                    "<strong>Approach:</strong> Tests the sequence for the occurrence of "
                    "two consecutive bits and compares the number of occurrences with a truly random sequence.</p>"
                    "<p><strong>Eligibility:</strong> Unrestricted</p>"
                    "<p><strong>Result:</strong> p-value &lt; 0,01 indicates a "
                    "non-random distribution of two consecutive bits in the sequence</p>",
    "Gap Test": "<h2>Gap Test</h2><p>"
                "<strong>Approach:</strong> Measures the number of occurrences of consecutive zeros between two ones "
                "in a "
                "sequence and compares it with a truly random sequence.</p> "
                "<p><strong>Eligibility:</strong> Unrestricted</p>"
                "<p><strong>Result:</strong> p-value &lt; 0,01 indicates a non-random distribution of gaps "
                "between ones.</p>",
    "Turning Point Test": "<h2>Turning Point Test</h2><p>"
                          "<strong>Approach:</strong> Tests for the number of times the sequence switches from"
                          " increasing to decreasing or vice versa, compared to a truly random sequence.</p>"
                          "<p><strong>Eligibility:</strong> Unrestricted</p>"
                          "<p><strong>Result:</strong> p-value &lt; 0,01 indicates a non-random sequence with "
                          "too few or too many turning points.</p> ",
    "Autocorrelation Test": "<h2>Autocorrelation Test</h2><p>"
                            "<strong>Approach:</strong> Tests the sequence for correlation between each"
                            " element and its neighboring elements at various lag times.</p>"
                            "<p><strong>Eligibility:</strong> Unrestricted</p>"
                            "<p><strong>Result:</strong> p-value &lt; 0,01 indicates a "
                            "non-random sequence with a high degree of correlation between neighboring elements.</p>",
    "Hamming Weight Test": "<h2>Hamming Weight Test</h2><p>"
                           "<strong>Approach:</strong> Counts the number of ones in each block (with length of 8 bits) "
                           "of the sequence."
                           " Compares this with the expected frequency of ones in a truly random sequence.</p>"
                           "<p><strong>Eligibility:</strong> Unrestricted</p>"
                           "<p><strong>Result:</strong> p-value &lt; 0,01 indicates a "
                           "non-random distribution of 1's and 0's in the sequence.</p>",
    "Lempel-Ziv Compression Test": "<h2>Lempel-Ziv Compression Test</h2><p>"
                                   "<strong>Approach:</strong> Tests the compressibility of the sequence using "
                                   "the Lempel-Ziv algorithm, which is based on finding repeated substrings in "
                                   "the sequence.</p>"
                                   "<p><strong>Eligibility:</strong> n &gt; 10^6 bits</p>"
                                   "<p><strong>Result:</strong> p-value &lt; 0,01 indicates a non-random "
                                   "sequence that can be compressed too much.</p> ",
    "Monobit": "<h2>Monobit Test</h2>"
               "<p><strong>Approach:</strong> Tests the sequence to determine if the number of "
               "ones and zeros is approximately equal.</p>"
               "<p><strong>Eligibility:</strong> n &gt; 100 bits </p>"
               "<p><strong>Result:</strong> p-value &lt; 0,01 indicates a non-random distribution of ones and "
               "zeros in the sequence.</p>",
    "Frequency Within Block": "<h2>Frequency Within Block Test</h2>"
                              "<p><strong>Approach:</strong> Divides the sequence into blocks of equal size and counts the "
                              "number of ones in each block. Compares the distribution of the block frequencies with a "
                              "chi-square distribution.</p>"
                              "<p><strong>Eligibility:</strong> n &gt; 100 bits </p>"
                              "<p><strong>Result:</strong> p-value &lt; 0,01 indicates a non-random distribution of ones"
                              " and "
                            "zeros in blocks.</p>",
    "Runs": "<h2>Runs Test</h2>"
            "<p><strong>Approach:</strong> Tests the sequence to determine if the number of "
            "runs of consecutive ones and zeros is as expected in a random sequence. A run is a sequence "
            "of consecutive bits of one kind.</p>"
            "<p><strong>Eligibility:</strong> n &gt; 100 bits</p>"
            "<p><strong>Result:</strong> p-value &lt; 0,01 suggests that the "
            "sequence may not be truly random since the number of runs is "
            "significantly different from the expected number in a random sequence.</p>",
    "Longest Run Ones In A Block": "<h2>Longest Run Ones In A Block Test</h2>"
                                   "<p><strong>Approach:</strong> Divides the sequence into blocks of equal size and counts "
                                   "the longest run of consecutive ones in each block. Compares the distribution of the "
                                   "longest run lengths with the expected distribution in a random sequence.</p>"
                                   "<p><strong>Eligibility:</strong> n &gt; 128</p>"
                                   "<p><strong>Result:</strong> p-value &lt; 0,01 suggests that the "
                                   "distribution of the longest runs of "
                                   "consecutive ones in the blocks is significantly different from the expected "
                                   "distribution in a random sequence.</p>",
    "Discrete Fourier Transform": "<h2>Discrete Fourier Transform Test</h2>"
                                  "<p><strong>Approach:</strong> Computes the Discrete Fourier Transform of the "
                                  "sequence and checks for periodic patterns in the frequency spectrum.</p>"
                                  "<p><strong>Eligibility:</strong> n &gt; 1000</p>"
                                  "<p><strong>Result:</strong> p-value &lt; 0,01 suggests that the "
                                  "sequence may not be truly random since there are unusual patterns in the frequency "
                                  "spectrum that are not expected in a random sequence.</p>",

    "Non Overlapping Template Matching": "<h2>Non-Overlapping Template Matching Test</h2>"
                                         "<p><strong>Approach:</strong> Searches for occurrences of a predefined set of"
                                         " m-bit templates in non-overlapping windows of the sequence. Counts the number "
                                         "of occurrences and compares it with the expected number of occurrences in a "
                                         "truly random sequence.</p>"
                                         "<p><strong>Eligibility:</strong> Unrestricted</p>"
                                         "<p><strong>Result:</strong> p-value &lt; 0,01 suggests that "
                                         "the sequence may not be truly random since the number of occurrences of the "
                                         "predefined templates in the sequence is significantly different from the expected"
                                         " number in a random sequence.</p>",
    "Overlapping Template Matching": "<h2>Overlapping Template Matching Test</h2>"
                                     "<p><strong>Approach:</strong> Test Searches for occurrences of a predefined "
                                     "set of m-bit "
                                     "templates in overlapping windows of the sequence. Counts the number of"
                                     " occurrences and compares it with the expected number of occurrences in a "
                                     "truly random sequence.</p>"
                                     "<p><strong>Eligibility:</strong> n &gt; 1 028 016 bits</p>"
                                     "<p><strong>Result:</strong> p-value &lt; 0,01 suggests that "
                                     "the sequence may not be truly random since the number of occurrences of the "
                                     "predefined overlapping templates in the sequence is significantly different "
                                     "from the "
                                     "expected number in a random sequence.</p>",
    "Maurers Universal": "<h2>Maurer's Universal Test</h2>"
                         "<p><strong>Approach:</strong> Measures the number of bits between the same patterns."
                         " If the sequence can be compressed (between repetitions of the same pattern, few different "
                         "bits are found), is considered non-random.</p>"
                         "<p><strong>Eligibility:</strong> n &gt; 387840 bits</p>"
                         "<p><strong>Result:</strong> p-value  &lt; 0,01 suggests that the "
                         "sequence may not be truly random since number of bits between teh same pattern is different "
                         "from the expected value in a random sequence.</p>",
    "Linear Complexity": "<h2>Linear Complexity Test</h2>"
                         "<p><strong>Approach:</strong> Measures the complexity of the sequence by computing "
                         "the linear complexity of a set of linearly generated sub-sequences. Compares the result "
                         "with the expected value in a random sequence.</p>"
                         "<p><strong>Eligibility:</strong> n &gt; 10^6 bits</p>"
                         "<p><strong>Result:</strong> p-value &lt; 0,01 suggests that the "
                         "sequence may not be truly random since the linear complexity of the sub-sequences is "
                         "significantly different from the expected value in a random sequence (short linear complexity"
                         "indicates non-random sequence).</p>",
    "Serial Test": "<h2>Serial Test</h2>"
              "<p><strong>Approach:</strong> Divides the sequence into overlapping sub-sequences of a fixed length "
              "k and counts the number of occurrences of each possible sub-sequence. Compares the distribution of "
              "the sub-sequence counts with the expected distribution in a random sequence.</p>"
              "<p><strong>Eligibility:</strong> m &lt; &#x230A;log<sub>2</sub> n&#x230B; "
                   "(m is length of block and n length of sequence)</p>"
              "<p><strong>Result:</strong> p-value &lt; 0,01 suggests that the sequence"
              " may not be truly random since the distribution of sub-sequence counts is significantly different "
              "from the expected distribution in a random sequence. Test calculates 18 p-values, all must be less "
                                "than 0,01 for success, their average is shown in the table of results.</p>",
    "Approximate Entropy": "<h2>Approximate Entropy Test</h2>"
                           "<p><strong>Approach:</strong> Measures the similarity of pairs of adjacent blocks "
                           "and compares it to a truly random sequence. </p>"
                           "<p><strong>Eligibility:</strong> m &lt; &#x230A;log<sub>2</sub> n&#x230B; - 5 "
                           "(m is length of block and n length of sequence)</p>"
                           "<p><strong>Result:</strong> p-value  &lt; 0,01 suggests that "
                           "the sequence may not be truly random since the number of similar sub-sequences is "
                           "significantly different from the expected value in a random sequence.</p>",
    "Cumulative Sums": "<h2>Cumulative Sums Test</h2>"
                       "<p><strong>Approach:</strong> Computes the cumulative sums of the sequence (transformed to -1 and +1) "
                       "and measures the"
                       " maximum absolute deviation of the sums from their expected values. Compares the result with"
                       " the expected maximum deviation in a random sequence.</p>"
                       "<p><strong>Eligibility:</strong> n &gt; 100 bits</p>"
                       "<p><strong>Result:</strong> p-value &lt; 0,01 suggests that "
                       "the sequence may not be truly random since the maximum deviation of the cumulative "
                       "sums is significantly different from the expected value in a random sequence. Test calculates"
                       " 2 p-values, all must be less "
                                "than 0,01 for success, their average is shown in the table of results.</p>",

    "Random Excursion": "<h2>Random Excursions Test</h2>"
                         "<p><strong>Approach:</strong> Tests the number of times a particular state is visited "
                         "during a cumulative sum excursion of the sequence. Test compares the distribution of the"
                         " visited states with the expected distribution in truly random sequence.</p>"
                         "<p><strong>Eligibility:</strong> n &gt; 10^6 bits</p>"
                         "<p><strong>Result:</strong> p-value &lt 0,01 suggests "
                         "that cumulative sums of random excursion are significantly different from expected value"
                        " in a random sequence. Test calculates 9 p-values, all must be less "
                                "than 0,01 for success, their average is shown in the table of results.</p>",
    "Random Excursion Variant": "<h2>Random Excursions Variant Test</h2>"
                                 "<p><strong>Approach:</strong> Tests the number of times a particular state "
                                 "is visited during a cumulative sum excursion of the sequence. "
                                "Compares the distribution of the visited states with the"
                                 " expected distribution in a random sequence. The difference from Random Excursion"
                                "Test is that the test is series of eighteen tests for states from -9 to 9 "
                                "except state 0.</p>"
                                 "<p><strong>Eligibility:</strong> n &gt; 10^6</p>"
                                 "<p><strong>Result:</strong> p-value &lt; 0.01 suggests"
                                 " that the sequence may not be truly random since the distribution of visited"
                                 " states during the excursions is significantly different from the expected "
                                 "distribution in a random sequence. Test calculates 18 p-values, all must be less "
                                "than 0,01 for success, their average is shown in the table of results.</p>",

    "Binary Matrix Rank": "<h2>Binary Matrix Rank Test</h2>"
                          "<p><strong>Approach:</strong> Constructs a binary matrix from the sequence and computes"
                          " its rank. Compares the rank with the expected rank in a random"
                          " binary matrix of the same size.</p>"
                          "<p><strong>Eligibility:</strong> n > 38912 </p>"
                          "<p><strong>Result:</strong> p-value &lt; 0,01 suggests that "
                          "the sequence may not be truly random since the rank of the binary matrix is significantly"
                          " different from the expected rank in a random binary matrix of the same size.</p>",
}

tooltip_gen_dict = {
    "Python random": "<h2>Python Generator: random</h2>"
                     "<p><strong>Description:</strong> Basic Python generator - <tt>random</tt>. "
                     "It uses a Mersenne Twister generator with a period 2**19937-1. "
                     "Generates the specified number of bits in the application</p>",
    "Python secrets": "<h2>Python Generator: secrets</h2>"
                      "<p><strong>Description:</strong> The <tt>secrets</tt> module is a module in Python that is "
                      "used to "
                      "generate cryptographically secure random numbers (for passwords, authentication, security "
                      "tokens). "
                      "Randomness is sourced from the operating system's secure random number generator, which is "
                      "accessed "
                      "through the os.urandom() function (in Unix systems uses syscall getrandom() and "
                      "the BCryptGenRandom function in Windows systems)."
                      " </p>",
    "LCG": "<h2>Linear Congruential Generator (LCG)</h2>"
           "<p><strong>Description:</strong> The LCG is a basic pseudorandom number generator that uses a formula: </p>"
           " <div class=\"formula\"><p>X<sub>n+1</sub> = (aX<sub>n</sub> + c) mod m</p></div>"
           "<p> Implemented parameters are: m=2**31, a = 1103515245, c = 12345 and time as a seed</p>",
    "Xorshift": "<h2>Xorshift</h2>"
                "<p><strong>Description:</strong> The xorshift generator uses the system time as an input seed "
                "and applies bit-shift operations to it. It creates a sequence of bits of the specified length </p>",
    "LFSR - bad RNG!": "<h2>Linear Feedback Shift Register (LFSR)</h2>"
                       "<p><strong>Description:</strong>  Linear feedback shift register RNG is implemented wrong on "
                       "purpose "
                       "(with register length 4), so it produces bits with period 15.  </p>",
}

