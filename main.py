import argparse

import TransParser
import constants

def main(args):
    print(args)

if __name__ = "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num-iterations", type=int, default=DEFAULT_NUM_ITERATIONS,
        help="Number of simulation iterations. Defualt: {0}".format(DEFAULT_NUM_ITERATIONS))
    parser.add_argument("--conf-json", type=str, default=DEAULE_CONFIGURATION_JSON,
        help="Json file with configuration for simulation. Default: {0}".format(DEAULE_CONFIGURATION_JSON))
    args = parser.parse_args()
    main(args)
