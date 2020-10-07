# Luma NLP Engineering Interview

## Interview Task

Using Yelp reviews [data set](https://www.yelp.com/dataset), build an interface that takes a string and returns a sentiment (positive, neutral, negative). Solution must be able to support user input from multiple languages. Provide tests, counter examples, and explanation of technique.

## Solution 

The resolution can be encountered in the .ipynb file attached, as well as a htlm file (Yelp Dataset - Lumahealth NLP Test.html).

I provided a dockerized solution to run the flask Api, which attend multiple languages, and does input validation.


## How to execute

### Build
$ docker build  --tag sentiment-classifier    --file Dockerfile     --pull . 

### Run
$ docker run -it  --publish 5000:5000  sentiment-classifier <br>

- open http://0.0.0.0:5000/

## Assumptions

Given that yelp dataset has a scoring system of 5 stars, to classify the review sentiment as negative, neutral or positive, I divided as follows:

- 1 star - Negative <br>
- 2 star - Negative <br>
- 3 star - Neutral <br>
- 4 star - Positive <br>
- 5 star - Positive <br>

Also, the dataset has ~6 million reviews, but it was unbalanced, having more 5 stars than the rest, so I applied a step to balance this dataset, reducing it to ~3 million reviews

## Features

The solution provided is a Flask Api, and I created a front-end with an input field also, to run preditions


## TODO

If given more time, I would try to improve the classification score, but using other approaches to transform the reviews text, and also would try deep learning approaches such as BERT. Would also try Hugging face and try to do it using javascript with Node-nlp.

