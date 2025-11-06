import logging
logger = logging.getLogger("travel-assistant.telemetry")


def record_event(name: str, **kwargs):
logger.info("event=%s %s", name, kwargs)