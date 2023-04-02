import nistrng

from source.tests import GraphicalTest, PokerTest, ChiSquareTest, KolmogorovSmirnovTest, \
    TwoBitTest, LempelZivCompressionTest, HammingWeightTest, AutocorrelationTest, GapTest, TurningPointTest, DummyTest


def create_all_battery():
    all_test_battery: dict = {
        "Graphical Test": GraphicalTest(),
        "Poker test": PokerTest(),
        "Two bit test": TwoBitTest(),
        "Gap Test": GapTest(),
        "Turning point test": TurningPointTest(),
        "Autocorrelation Test": AutocorrelationTest(),
        "Hamming weight test": HammingWeightTest(),
        "Lempel ziv compression test": LempelZivCompressionTest(),


        # "Chi Square": ChiSquareTest(),                                                      # = monobit test
        # "Kolmogorov smirnov": KolmogorovSmirnovTest(),                                      # = spojité hodnoty
        # "dummy test": DummyTest(),

    }
    # nistrng.SP800_22R1A_BATTERY.pop("dft")  # this is how to delete test from battery, so it can be replaced
    all_test_battery.update(nistrng.SP800_22R1A_BATTERY)

    return all_test_battery


"""
k-s and chi kvadrat? = monobit

two-bit test: speciální případ serial/poker testu?
    https://www.economic-debates.ro/art.20165roxana_dragomir.pdf
    
poker test:
    degrees of freedom? - asi vyřešeno
    
---------------------------------------------------------------------

lempel-ziv complexity: hard (computing compression is doable, but evaluation?)
    podobný jako hamming weight / t complexity
    polamý, kde se bere mu a sigma?

birthday spacings:

test autokorelace
    knuth chapter 5: https://cacr.uwaterloo.ca/hac/about/chap5.pdf
    
hamming weight test/autocorelation:
    https://www.economic-debates.ro/art.20165roxana_dragomir.pdf

Bartels Test for Randomness:
    zdroje jsou, ale asi starý a složitý 
    
Cox Stuart Test? 
    https://github.com/zhukov-msu/TrendAlgorithms

new test
    file:///C:/Users/martin/Downloads/INFO898-2.pdf
    
gcd, gorilla, bday, parking lot, entropy, cochranův test

test bodů zvratu, zneménkových diferencí, cochranův, autokorelace
    https://is.muni.cz/el/sci/jaro2013/M6444/um/38997543/prednaska2.pdf
    
R package - více testů
    https://cran.r-project.org/web/packages/randtests/index.html
    
test diference znamének:
    mohl by jít, podovný jako zvratu
    https://is.muni.cz/el/sci/jaro2013/M6444/um/38997543/prednaska2.pdf
    https://aip.scitation.org/doi/pdf/10.1063/1.4938768
    https://en.wikipedia.org/wiki/Sign_test
    https://rdrr.io/cran/randtests/man/difference.sign.test.html
    
spearman koeficient
    popsán je jen tady
    https://is.muni.cz/el/sci/jaro2013/M6444/um/38997543/prednaska2.pdf
    

    
"""
