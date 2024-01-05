# utils
from utils import get
from utils import post
from utils import BASE_URL

# typing
from typing import List

#counter
from collections import Counter

class Dog(object):
    """
    Dog object that is composed of the id, name and breed of the dog

    To initialize:
    :param id: dog id
    :param name: dog name
    :param breed: dog breed id

    USAGE:
        >>> dog = Dog(id=1, name='Bobby', breed=1)
    """
    def __init__(self, id: int, name: str, breed: int):
        self.id = id
        self.name = name
        self.breed = breed


class Breed(object):
    """
    Breed object that is composed of the id and the name of the breed.

    To initialize:
    :param id: breed id
    :param name: breed name

    Also, breed has a list of dogs for development purposes
    :field dogs: breed dog list

    USAGE:
        >>> breed = Breed(id=1, name='Kiltro')
        >>> dog = Dog(id=1, name='Cachupin', breed=breed.id)
        >>> breed.add_dog(dog)
        >>> breed.dogs_count()
        1
    """
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.dogs: List[Dog] = []

    def add_dog(self, dog: Dog):
        self.dogs.append(dog)

    def dogs_count(self) -> int:
        return len(self.dogs)


class DogHouse(object):
    """
    Doghouse object that manipulates information on breeds and dogs.
    We expect you implement all the methods that are not implemented
    so that the flow works correctly


    DogHouse has a list of breeds and a list of dogs.
    :field breeds: breed list
    :field dogs: dog list

    USAGE:
        >>> dog_house = DogHouse()
        >>> dog_house.get_data(token='some_token')
        >>> total_dogs = dog_house.get_total_dogs()
        >>> common_breed = dog_house.get_common_breed()
        >>> common_dog_name = dog_house.get_common_dog_name()
        >>> total_breeds = dog_house.get_total_breeds()
        >>> data = {  # add some data
        ...     'total_dogs': total_dogs,
        ...     'total_breeds': total_breeds,
        ...     'common_breed': common_breed.name,
        ...     'common_dog_name': common_dog_name,
        ... }
        >>> token = 'some token'
        >>> dog_house.send_data(data=data, token=token)
    """
    def __init__(self):
        self.breeds: List[Breed] = []
        self.dogs: List[Dog] = []

    def get_data(self, token: str):
        """Fetches data for breeds and dogs from the API."""
        self._get_breeds_data(token)
        self._get_dogs_data(token)

    def _get_breeds_data(self, token: str):
        """Fetches and stores breeds data."""
        # Get total number of breeds to determine pagination
        response = get(f"{BASE_URL}/api/v1/breeds/?limit=1", token)
        total_breeds = response.get('count', 0)
        limit_breeds = min(100, total_breeds)  # Fetch in batches of 100
        url_breeds = f"{BASE_URL}/api/v1/breeds/?limit={limit_breeds}"

        while url_breeds:
            response = get(url_breeds, token)
            for breed_data in response.get('results', []):
                breed = Breed(id=breed_data["id"], name=breed_data["name"])
                self.breeds.append(breed)
            url_breeds = response.get('next', None)  # Pagination

    def _get_dogs_data(self, token: str):
        """Fetches and stores dogs data."""
        url_dogs = f"{BASE_URL}/api/v1/dogs/"
        while url_dogs:
            response = get(url_dogs, token)
            for dog_data in response.get('results', []):
                breed_id = dog_data.get("breed")  # Get breed of dog
                breed = next((b for b in self.breeds if b.id == breed_id), None)
                if breed:
                    dog = Dog(id=dog_data["id"], name=dog_data["name"], breed=breed.id)
                    self.dogs.append(dog)
                    breed.add_dog(dog)
            url_dogs = response.get('next', None)  # Pagination

    def get_total_breeds(self) -> int:
        """Returns the total number of breeds."""
        return len(self.breeds)

    def get_total_dogs(self) -> int:
        """Returns the total number of dogs."""
        return len(self.dogs)

    def get_common_breed(self) -> Breed:
        """Returns the most common breed."""
        if not self.breeds:
            return None
        return max(self.breeds, key=lambda breed: breed.dogs_count())

    def get_common_dog_name(self) -> str:
        """Returns the most common dog name."""
        if not self.dogs:
            return ""
        name_count = Counter(dog.name for dog in self.dogs)
        return name_count.most_common(1)[0][0]

    def send_data(self, data: dict, token: str):
        """Sends computed data to the API."""
        # Prepare data for sending
        data = {
            "totalBreeds": self.get_total_breeds(),
            "totalDogs": self.get_total_dogs(),
            "commonBreed": self.get_common_breed().name,  
            "commonDogName": self.get_common_dog_name()
        }

        # API endpoint
        url = f"{BASE_URL}/api/v1/answer/"

        # Make the POST request
        response = post(url, data, token)
        print(response)