# demonstrate the logging api in Python

# use the built-in logging module
import logging

extra_data = {'user': 'hoge@example.com'}


def custom_fmt():
    # set the output file and debug level, and
    # use a custom formatting specification
    log_fmt = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
    date_fmt = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(filename="../tmp/logging_custom.log",
                        filemode="w",
                        level=logging.DEBUG,
                        format=log_fmt,
                        datefmt=date_fmt)

    logging.debug("This is a debug-level log message", extra=extra_data)
    logging.info("This is an info-level log message", extra=extra_data)
    logging.warning("This is a warning-level message", extra=extra_data)
    logging.error("This is an error-level message", extra=extra_data)
    logging.critical("This is a critical-level log message", extra=extra_data)


if __name__ == "__main__":
    custom_fmt()
