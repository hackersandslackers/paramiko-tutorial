"""Custom logger."""
from sys import stdout
from loguru import logger as custom_logger


def create_logger():
	"""Create custom logger."""
	custom_logger.remove()
	custom_logger.add(
		stdout,
		format="{time} {message}",
		filter="client",
		level="INFO"
	)
	custom_logger.add(
		'logs/errors.log',
		colorize=True,
		level="ERROR",
		rotation="500 MB",
		format="<light-cyan>{time:MM-DD-YYYY HH:mm:ss}</light-cyan> | "
				+ "<light-red>{level}</light-red>: "
				+ "<light-white>{message}</light-white>"
	)
	return custom_logger

