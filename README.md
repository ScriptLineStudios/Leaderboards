Leaderboard API v0.1
==============

Leaderboards is a simpole leaderboards api that allows you to make GET/POST requests to a leaderboard server which will manage the board.

Getting Started
==============

To get started head over to https://leaderboards.pythonanywhere.com/ and and create a new leaderboard. This will give you an api key which will allow you to access to the api. **Keep this key safe** as it will allow for new entries to be made to your board. To make a new entry make a POST request to the following endpoint: https://leaderboards.pythonanywhere.com/add/ an example of a request in Python:

```
import requests
requests.post("https://leaderboards.pythonanywhere.com/add?apiKey=YOUR_API_KEY&data=NAME_OF_ENTRY&scores=THEIR_SCORE")
```

The leaderboard can then be viewed at: https://leaderboards.pythonanywhere.com/leaderboard/YOUR_LEADERBOARD_NAME alternativly you might want to grab the leaderboards contents to display directly in your game. This can be done by making a GET request to the endpoint. An example of the request being made in Python:

```
import requests
data = requests.get("https://leaderboards.pythonanywhere.com/add?apiKey=YOUR_API_KEY")
print(data.content)
```
From there the data can be formatted to be displayed in any way you like. 


https://user-images.githubusercontent.com/85095943/151555501-98845d3f-f9ad-48c2-a9bd-2cf301a18553.mov
 
