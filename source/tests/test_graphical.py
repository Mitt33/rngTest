import numpy as np
import math

from matplotlib import pyplot as plt
from matplotlib.patches import Arc
from nistrng import Test, Result, unpack_sequence
from scipy.stats import stats


class GraphicalTest(Test):
    """
    The significance value of the test is 0.01.
    """

    def __init__(self):
        # Generate base Test class
        super(GraphicalTest, self).__init__("Graphical test", 0.01)

    def _execute(self,
                 bits: np.ndarray):
        """
        Overridden method of Test class: check its docstring for further information.
        """
        if len(bits) > 1000000:  ####test_decref_doesnt_leak() work!!!!!!!!
            integers = np.packbits(bits)
            print(integers)
            normalized_numbers = (integers + 1) / (2 ** len(bits))
            print(normalized_numbers)
        else:
            unpacked = unpack_sequence(bits)
            # converting to int8 loss some precision - more cases (int 32..)
            normalized_ints = (unpacked + 128) / 255.0
            normalized_numbers = normalized_ints[:len(normalized_ints) // 2 * 2]
            # print(normalized_numbers)
        # TODO: fix converting to values on interval (0,1)

        fig, ax = plt.subplots()
        # arc function wit center in 0,0; diameter 2
        arc = Arc((0, 0), 2, 2, angle=0, theta1=0, theta2=90, edgecolor='r', linewidth=2)
        ax.add_patch(arc)
        # Set the x and y limits of the plot
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])

        if len(normalized_numbers) > 10000:
            point = ","
            thick = (72. / fig.dpi) ** 2
        else:
            point = "."
            thick = 100

        x_coordinates = normalized_numbers[::2]
        y_coordinates = normalized_numbers[1::2]
        count = 0
        count_in = 0
        count_out = 0
        within_circle = []
        outside_circle = []
        for x, y in zip(x_coordinates, y_coordinates):
            count += 1
            distance = math.sqrt(x ** 2 + y ** 2)
            if distance <= 1:
                count_in += 1
                within_circle.append((x, y))
            else:
                count_out += 1
                outside_circle.append((x, y))
        plt.scatter([x[0] for x in within_circle], [y[1] for y in within_circle], color='green', marker=point,
                    s=thick)
        plt.scatter([x[0] for x in outside_circle], [y[1] for y in outside_circle], color='red', marker=point,
                    s=thick)

        plt.ylim(0.0, 1.0)
        plt.xlim(0.0, 1.0)
        plt.xlabel(r'$x_i$')
        plt.ylabel(r'$x_{i+1}$')

        pi_approx = (4 * count_in) / count
        text = f"Points in: {count_in}, points out: {count_out} from: {count} points"
        plt.text(0.5, 1.1, text, ha='center')
        plt.text(0.5, 1.05, f"approximate value of pi: {pi_approx}", ha='center')
        plt.show()

        true_value = math.pi
        score = abs(true_value - pi_approx)
        if score <= self.significance_value:
            return Result(self.name, True, np.array(score))
        return Result(self.name, False, np.array(score))

    def is_eligible(self,
                    bits: np.ndarray) -> bool:
        # This test is always eligible for any sequence
        return True
