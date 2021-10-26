# ChatBot Using Dialogflow and Flask


## Introduction

This Project is for ordering food through chatbot.I used Dialogflow and as Backend APi i used Flask.
Flask was used to give dyanmic response to the customer.Instead of Two or Three responses like in Dialogflow.


## Flask

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

## Dialogflow

Dialogflow is a natural language understanding platform used to design and integrate a conversational user interface into mobile apps, web applications, devices, bots, interactive voice response systems and related uses.

## MyBot

* I have deployed my bot with Telegram using telegrams Fatherbot.
![img1](https://github.com/hissh05/OnlineEatsBot_with_Flask-/blob/master/Botimage.png)

* Link To My Bot
		(t.me/Hissh05Bot)

## How i created?

* I started with Dialogflow which is easy to learn and work with.it gives you demo chatbot in side of screen
* In dialogflow Create a Intent and entities.
* And Mark which all are entites.Best is to import entites and store in entities block.(in my case it was food names).Check The foodentity.txt file.
* Then i created a flask api which will get the request from dialogflow.To connect api and dialogflow.In fullfilment option You paste the link of the api.
* Upload your api to Heroku and get the link from there and paste in fullfillment.

## reference

* Dialogflow Documentation(https://cloud.google.com/dialogflow/docs)