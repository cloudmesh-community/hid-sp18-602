import connexion
import six

from swagger_server.models.list_images import ListImages  # noqa: E501
from swagger_server import util
from listimg import get_images_list

def list_images_get():  # noqa: E501
    """Get list of images stored in glance

      # noqa: E501


    :rtype: List[ListImages]
    """
    return get_images_list()
