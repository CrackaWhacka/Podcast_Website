import abc

from podcast.domainmodel.model import Podcast, Author, Episode, Category

repo_instance = None


class RepositoryException(Exception):
    def __init__(self, message=None):
        print(f'RepositoryException: {message}')


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_podcast(self, podcast: Podcast):
        """ Adds a podcast to the repository list of podcasts"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_podcast(self):
        """ Returns the list of podcasts"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_number_of_podcasts(self):
        """ Returns the number of podcasts that exist in the repository"""
        raise NotImplementedError