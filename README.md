# Simpsons Markov Bot

A Markov chain model to generate text and tweet it.
In this particular example we used ~600 chapters of the Simpsons to generate the a Homer Simpson text model.  

## Getting Started

In the the notebook [explore_dataset_and_create_bot.ipynb](explore_dataset_and_create_bot.ipynb) 
you will find the code snippets to generate a Markcov chain generator model trained using a dataset.
For this particular model we choosed to train a model based on Homer Simpson.



### Prerequisites

See [requirements.txt](requirements.txt) 


## Running the bot

1. Follow the steps on [explore_dataset_and_create_bot.ipynb](explore_dataset_and_create_bot.ipynb)

2. [Setup a twitter application](https://www.mattcrampton.com/blog/step_by_step_tutorial_to_post_to_twitter_using_python/)

3. setup [keys.py](#setup-keys)

4. run `python bot.py model_name` 


### Setup keys

Generate a the file `keys.py` that contains

```python
API_KEY = 'FILL_API_KEY'
API_SECRET = 'FILL_API_SECRET'

ACCES_TOKEN = 'FILL_ACCES_TOKEN'
ACCES_TOKEN_SECRET = 'FILL_ACCES_TOKEN_SECRET'
``` 

and save it in `./`

You will get this keys following the [tutorial]https://www.mattcrampton.com/blog/step_by_step_tutorial_to_post_to_twitter_using_python/
 

## Authors

* **Ivan Lengyel** http://ivanlen.github.io/


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
