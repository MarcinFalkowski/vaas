import logging
import loremipsum

from django.dispatch import receiver
from django.db.models.signals import post_save

logger = logging.getLogger('vaas')


@receiver(post_save)
def lorem(**kwargs):
    logger.info("######## PLUGIN {} START ########".format(__name__))
    for sentence in loremipsum.get_sentences(5):
        logger.info(sentence)
    logger.info("######## PLUGIN {} STOP  ########".format(__name__))
