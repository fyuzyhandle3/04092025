from logtail import LogtailHandler
import logging

SOURCE_TOKEN = 'hL9dgYKMSaKnnHxKH3uxQW1t'
HOST = 's1524250.eu-nbg-2.betterstackdata.com'


def get_logger():
    handler = LogtailHandler(
        source_token=SOURCE_TOKEN,
        host=f'https://{HOST}',
    )
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.handlers = []
    logger.addHandler(handler)
    return logger


logger = get_logger()

logger.info('some info log', exc_info={"user_id": 25653})
logger.error('some error log')
