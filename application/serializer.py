"""
    Class responsible serializing and recording of objects
    Utilizes pickle module
"""

import logging
import pickle

class Serializer():

    def __init__(self):
        # logger should be initialized on the main function
        logger = logging.getLogger()
        logger.info("Serializer initialized")

    """
        obj: object to be stored in file
        file_prefix: name of the file the object will be stored on, without
                     extension
    """
    def serialize(self, obj, file_prefix: str):
        with open(file_prefix+'.pkl', 'wb') as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
            logger.info(f'{obj} stored at {file_prefix+".pkl"}') 

    """
        file_prefix: file containing the object to be unserialized

        return: the unpickled object
    """
    def deserialize(self, file_prefix):
        # TODO throw exception if the given filename does not currently exist

        with open(file_prefix+'.pkl', 'rb') as in_:
            obj = pickle.load(in_)
            logger.info(f'{obj} loaded from {file_prefix+".pkl"}')
            return obj
