import logging
import logging.config
import json
from typing import Optional

LOGGER_CONFIG_PATH = 'conf/log_config.json'

# Custom log level definitions
AI_LEVEL = 35
FE_LEVEL = 25

logging.addLevelName(AI_LEVEL, "AI")
logging.addLevelName(FE_LEVEL, "FE")

# AI and FE :Custom logger methods 
def ai(self, message, *args, **kwargs):
    if self.isEnabledFor(AI_LEVEL):
        self._log(AI_LEVEL,
                  message,
                  args,
                  **kwargs,
                  stacklevel=2)

def fe(self, message, *args, **kwargs):
    if self.isEnabledFor(FE_LEVEL):
        self._log(FE_LEVEL,
                  message,
                  args,
                  **kwargs,
                  stacklevel=2)

class LevelFilter(logging.Filter):
    def __init__(self, level):
        super().__init__()
        self.level = level

    def filter(self, record):
        return record.levelno == self.level

# Attach custom methods to Logger class
logging.Logger.ai = ai
logging.Logger.fe = fe

def setup_logging(config_path: str = LOGGER_CONFIG_PATH) -> None:
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)

        logging.config.dictConfig(config)

        # Exact-level filtering
        app_logger = logging.getLogger("app_logger")
        app_logger.handlers[0].addFilter(LevelFilter(10))   # debug_file
        app_logger.handlers[1].addFilter(LevelFilter(20))   # info_file
        app_logger.handlers[2].addFilter(LevelFilter(40))   # error_file
        app_logger.handlers[3].addFilter(LevelFilter(30))   # console

        ai_logger = logging.getLogger("ai_logger")
        ai_logger.handlers[0].addFilter(LevelFilter(35))

        fe_logger = logging.getLogger("fe_logger")
        fe_logger.handlers[0].addFilter(LevelFilter(25))

        print(f"Logging configured using {config_path}")

    except FileNotFoundError:
        print(f"ERROR: Logging config file not found: {config_path}")
    except Exception as e:
        print(f"ERROR initializing logging: {e}")


# Logger getters
def get_app_logger() -> logging.Logger:
    return logging.getLogger("app_logger")

def get_ai_logger() -> logging.Logger:
    return logging.getLogger("ai_logger")

def get_fe_logger() -> logging.Logger:
    return logging.getLogger("fe_logger")


def log_message(level: str, message: str, logger: Optional[logging.Logger] = None) -> None:
    if logger is None:
        logger = get_app_logger()

    level = level.upper()

    match level:
        case "DEBUG": logger.debug(message)
        case "INFO": logger.info(message)
        case "WARNING": logger.warning(message)
        case "ERROR": logger.error(message)
        case "CRITICAL": logger.critical(message)
        case "AI": logger.ai(message)
        case "FE": logger.fe(message)
        case _:
            logger.warning(f"Invalid log level '{level}', using INFO instead.")
            logger.info(message)


# Initialize logging when module loads
setup_logging()
