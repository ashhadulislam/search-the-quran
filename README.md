# Flask Application To Search For Any English Word In Quran

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)
### Introduction

Given any word, this application returns all the verses in the Quran in which the word is present.

Not only that, it also looks for synonyms of said word and finds the verses which contain the same.

Some examples are as follows:
```
User: Hi
Bot: Hi there! How may I help you?
User: Can you suggest some good restaurants in kolkata Bot: What kind of cuisine would you like to have?
1. Chinese 2. Mexican 3. Italian
4. American 5. Thai
6. North Indian
User: american
Bot: What's the average budget for two people?
1. Lesser than Rs. 300 2. Rs. 300 to 700
3. More than 700
User: <300
Bot: Showing you top rated restaurants:
1. Restaurant 1 in Area 1. And the average price for two people here is: XXX Rs
2. Restaurant 1 in Area 1. And the average price for two people here is: XXX Rs
3. .
4. .
5. .
Bot: Should I send you details of all the restaurants on email? User: yes. Please
Bot: To what email id should I send it to?
User: jddk.2jmd@kdl.co.in
Bot: Sent. Bon Appetit!
```


### Installation

Download this repo and cd into the folder

Install the dependencies
```sh
$ pip install -r requirements.txt
```
Install the spacy en library
```sh
$ python -m spacy download en
```

### Training the RASA 

In order to train the interpreter, run the following command

```sh
$ python -m rasa_nlu.train -c nlu_config.yml --data data/data.json -o models --fixed_model_name nlu --project current --verbose
```

In order to train RASA CORE, run the following command

```sh
$ python -m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue -c policies.yml
```

### Running the RASA on commandline

In order to run rasa action server, execute
```sh
$ python -m rasa_core_sdk.endpoint --actions actions
```


In order to run rasa at commandline, execute
```sh
$ python -m rasa_core.run -d models/current/dialogue -u models/current/nlu --endpoints endpoints.yml
```

### Running the RASA on GUI
First, run a small flask server to get the GUI
```sh
$ cd chat_interface
$ python deploy.py
```
This will run flask server with a chat window that can be accessed by visiting
http://localhost:5090

Next get the rasa action server up and running
```sh
$ python -m rasa_core_sdk.endpoint --actions actions
```

Next run rasa as a simple server
```sh
$ python -m rasa_core.run --enable_api -d models/current/dialogue -u models/current/nlu -o out.log --endpoints endpoints.yml
```

Now if you go to your browser and open http://localhost:5090, a chat window will pop up and you can converse with the bot.


### Running the RASA on Slack

Set up slack as mentioned here
https://www.youtube.com/watch?v=xu6D_vLP5vY
Also check out this blog for more clarity https://towardsdatascience.com/building-a-conversational-chatbot-for-slack-using-rasa-and-python-part-2-ce7233f2e9e7

First get the rasa action server up and running
```sh
$ python -m rasa_core_sdk.endpoint --actions actions
```

Next run the app which will handle slack messages
```sh
$ python run_app.py
```

Create the ngrok tunneling as mentioned in the video/blog post mentioned above.
Open slack and you're good to go.




| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| Github | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |


### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantanously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma test
```
#### Building for source
For production release:
```sh
$ gulp build --prod
```
Generating pre-built zip archives for distribution:
```sh
$ gulp build dist --prod
```
### Docker
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd dillinger
docker build -t joemccann/dillinger:${package.json.version} .
```
This will create the dillinger image and pull in the necessary dependencies. Be sure to swap out `${package.json.version}` with the actual version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

#### Kubernetes + Google Cloud

See [KUBERNETES.md](https://github.com/joemccann/dillinger/blob/master/KUBERNETES.md)


### Todos

 - Write MORE Tests
 - Add Night Mode

License
----

MIT


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
