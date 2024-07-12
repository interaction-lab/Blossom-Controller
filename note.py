from .blossom_interface import BlossomInterface
import logging

__version__ = '1.0.0'
__description__ = 'A interface to control blossom via network or local usb.'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

__all__ = [BlossomInterface]
