import logging


def get_logger(name, level=logging.DEBUG):
	logger = logging.getLogger(name)
	logger.setLevel(level)

	if not logger.handlers:
		# ch = logging.StreamHandler()
		ch = logging.FileHandler("logs.log", 'w')
		ch.setLevel(level)

		formatter = logging.Formatter(
			"[%(name)s.%(module)s]: %(message)s",
			datefmt="%H:%M:%S"
		)
		ch.setFormatter(formatter)

		logger.addHandler(ch)

	return logger

log = get_logger("fireplace", level=logging.CRITICAL)
# log = get_logger("wins", level=logging.CRITICAL)
