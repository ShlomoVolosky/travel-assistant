import logging
import os


LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
level=getattr(logging, LEVEL, logging.INFO),
format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("travel-assistant")