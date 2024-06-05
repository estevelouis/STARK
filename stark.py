import argparse
import configparser
import os
import resource
import sys
import time
from pathlib import Path

import stark
import logging
import psutil
from stark.stark import read_settings, parse_args
logger = logging.getLogger('stark')


def main():
    args = parse_args(sys.argv[1:])

    settings = read_settings(args.config_file, args)

    stark.run(settings)


if __name__ == "__main__":
    start_time = time.time()
    main()
    logger.info("Total:")
    logger.info("--- %s seconds ---" % (time.time() - start_time))
