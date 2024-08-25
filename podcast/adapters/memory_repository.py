from bisect import insort_left


from podcast.adapters.repository import AbstractRepository
from podcast.domainmodel.model import Podcast
from podcast.adapters.datareader.csvdatareader import CSVDataReader


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self.__podcast = list()

    def add_podcast(self, podcast: Podcast):
        if isinstance(podcast, Podcast):
            insort_left(self.__podcast, podcast)

    def get_podcast(self):
        return self.__podcast

    def get_number_of_podcasts(self):
        return len(self.__podcast)

def populate(repo: MemoryRepository):
    reader = CSVDataReader()
    reader.create_podcast()
    reader.load_episodes_into_podcasts()

    for podcast in CSVDataReader.podcast_list:
        repo.add_podcast(podcast)

def make_podcast_list_into_dict(list: list) -> dict:
    podcast_dictionary = dict()
    for podcast in list:
        if not isinstance(podcast, Podcast):
            pass
        else:
            podcast_dictionary[podcast.title] = podcast
    return podcast_dictionary