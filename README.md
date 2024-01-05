# Magnet.cl - Python test

This technical test requires you to complete a python application that consumes and works with data from our Dogs API.

## Description

### Project structure

The project is a basic Python application with an entry point in `main.py`.

In the `models.py` file you can find three classes:
* Dog: A class that stores data from one dog.
* Breed: A class that stores data from one breed, also saves a list of dogs.
* DogHouse: A class that records Dogs and Breeds, for this test you must complete unimplemented methods.

In the `utils.py` file We provide some request functions to help you make the connection with the API.

### Environment

Your project will be tested using Python 3.7.

### General goals

Your goal is to implement the incomplete methods needed to compute and send the results to our server.

There are 6 methods you have to implement in the `DogHouse` class to pass
this test:

* `DogHouse.get_data(token: str) -> None`: You have to get the data from the given API and store in the DogHouse class.
* `DogHouse.get_total_dogs() -> int`: You have to return a `number` with the total number of dogs.
* `DogHouse.get_total_breeds() -> int`: You have to return a `number` with the total number of breeds.
* `DogHouse.get_common_breed() -> Breed` : You have to return the most common `Breed`.
* `DogHouse.get_common_dog_name() -> str`: You have to return the most common dog name.
* `DogHouse.send_data(data: dict, token: str) -> None`: You have to send your answers to a given API endpoint.

The expected output are just the 4 lines that `main.py` prints to the
console. These are the same results that the app sends to our server. No additional lines should be printed.

You can create additional methods, classes or files if you need it, but beware
that some files should not be edited. Those files are clearly marked with a
comment at the beginning of the file. For instance: `main.py` and `utils.py`.


### API

All the necessary documentation to perform this test is in: https://dogs.magnet.cl/

Also, our API implements the Rate Limiting policy, this means that it limits the number of requests that can be made in a period of time and in case of exceeding this limit, pending requests are rejected.

Our API accepts up to `200 requests per minute`, this implies that any
solution that exceeds this number will be rejected immediately. If your code
is done correctly you shouldn't need to worry about this limit.

Note: The data in the API does not change.

#### Delivery method

You will have full write access to your own fork of this project at
http://interviews.magnet.cl/{your-user-name}/python-api-test.

Send us a message on GetOnBoard when you push your
last commit to the `master` branch and your answer is ready for review.

Pull/Merge requests are not allowed on this project to prevent your answers
from being visible by other candidates.

## Aspects to be evaluated

* Appropriate use of the given model.
* Appropriate use of the language.
* Programming style.
* Solution design.
* Repository use.
* Compliance of these instructions.

## Aspects to be ignored

* Time you take to complete this test.
* Deployment to any server.

## Additional considerations

This is **not** an open source project.
You are not allowed to publish copies of this repository to other sites.
Check the LICENSE file if you need more information.
