import logging

def setup_logger(name, level=logging.INFO):
    """Sets up a logger with the given name and level."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Check if the logger already has handlers to avoid duplicate logs
    if not logger.hasHandlers():
        # Create handlers
        console_handler = logging.StreamHandler()

        # Create formatter and add to the handler
        formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(formatter)

        # Add handler to the logger
        logger.addHandler(console_handler)

    return logger