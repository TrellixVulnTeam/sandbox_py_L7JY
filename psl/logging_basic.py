# demonstrate the logging api in Python

# use the built-in logging module
import logging


def basic():
    # Use basicConfig to configure logging
    # this is only executed once, subsequent calls to
    # basicConfig will have no effect
    logging.basicConfig(level=logging.INFO,  # default: WARNING
                        filemode="w",  # default: 'a'
                        filename="../tmp/logging_basic.log")

    # Try out each of the log levels
    logging.debug("This is a debug-level log message")
    logging.info("This is an info-level log message")
    logging.warning("This is a warning-level message")
    logging.error("This is an error-level message")
    logging.critical("This is a critical-level message")


if __name__ == "__main__":
    basic()
