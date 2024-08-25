from memory_repository import MemoryRepository
from memory_repository import populate

repo_instance = MemoryRepository()
populate(repo_instance)

print(repo_instance.get_number_of_podcasts())
p1 = (repo_instance.get_podcast()[1000])
print(p1.id)
print(p1.author)
print(p1.title)
print(p1.description)
print(p1.episodes)