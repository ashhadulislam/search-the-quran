# Flask Application To Search For Any English Word In Quran

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)
[![HitCount](http://hits.dwyl.io/ashhadulislam/https://githubcom/ashhadulislam/search-the-quran.svg)](http://hits.dwyl.io/ashhadulislam/https://githubcom/ashhadulislam/search-the-quran)
### Introduction

Given any word, this application returns all the verses in the Quran in which the word is present.

Not only that, it also looks for synonyms of said word and finds the verses which contain the same.



### How to use

You can use this app as a service.
Simple make a get request:
https://iqrah.herokuapp.com/search/word
Where word is the word that you are looking for

### Result
Example query:

https://iqrah.herokuapp.com/search/pray

You will get a json file having following structure
```json
{
    "rich": [{
      "Surah": "2",
      "Ayah": "69",
      "Text": "They said: \"Beseech on our behalf Thy Lord to make plain to us Her colour.\" He said: \"He says: A fawn-coloured heifer, pure and rich in tone, the admiration of beholders!\"",
      "Proximity": 100
   }, {
      "Surah": "3",
      "Ayah": "181",
      "Text": "Allah hath heard the taunt of those who say: \"Truly, Allah is indigent and we are rich!\"- We shall certainly record their word and (their act) of slaying the prophets in defiance of right, and We shall say: \"Taste ye the penalty of the Scorching Fire!",
      "Proximity": 100
   },
   {
      "Surah": "9",
      "Ayah": "28",
      "Text": "O ye who believe! Truly the Pagans are unclean; so let them not, after this year of theirs, approach the Sacred Mosque. And if ye fear poverty, soon will Allah enrich you, if He wills, out of His bounty, for Allah is All-knowing, All-wise.",
      "Proximity": 80
   },
   
   ],
   "fertile": [{
      "Surah": "2",
      "Ayah": "265",
      "Text": "And the likeness of those who spend their substance, seeking to please Allah and to strengthen their souls, is as a garden, high and fertile: heavy rain falls on it but makes it yield a double increase of harvest, and if it receives not Heavy rain, light moisture sufficeth it. Allah seeth well whatever ye do.",
      "Proximity": 100
   }, {
      "Surah": "6",
      "Ayah": "6",
      "Text": "See they not how many of those before them We did destroy?- generations We had established on the earth, in strength such as We have not given to you - for whom We poured out rain from the skies in abundance, and gave (fertile) streams flowing beneath their (feet): yet for their sins We destroyed them, and raised in their wake fresh generations (to succeed them).",
      "Proximity": 100
   }],
   "ample": [{
      "Surah": "17",
      "Ayah": "63",
      "Text": "(Allah) said: \"Go thy way; if any of them follow thee, verily Hell will be the recompense of you (all)- an ample recompense.",
      "Proximity": 100
   }, {
      "Surah": "53",
      "Ayah": "32",
      "Text": "Those who avoid great sins and shameful deeds, only (falling into) small faults,- verily thy Lord is ample in forgiveness. He knows you well when He brings you out of the earth, And when ye are hidden in your mothers' wombs. Therefore justify not yourselves: He knows best who it is that guards against evil.",
      "Proximity": 100
   }]
}
    
```

As you can see above, we get the verses where rich is mentioned in the Quran.
We also get verses where the synonyms of rich are mentioned.

Note the Proximity value tells us, how close to the original word, the word in the verse is.

For example if the word in the verse is enriched then the proximity value will be a little low (80 in this case), whereas if the word is rich, same as the word queried, the value of Proximity will be 100.

The results are sorted on Proximity values for each word.

Please paste the output in any json validator to get a good view of the returned data

### Development

If you want to source this project
Download this repo and cd into the folder

Install the dependencies
```sh
$ pip install -r requirements.txt
```
The application runs as a flask app.
Simply execute
```sh
$ python app.py
```
The app will be running in localhost at port 5000
You can run query locally as follows

localhost:5000/search/word_to_search



### Todos

 - Make it more visual(Preferably in a different app)
 - Add robustness ( example, support multiple word search)

 If you can help out in any of these tasks or you want to add more features, please feel free to fork and contribute.
 For any details, get in touch with me at ashhadulislam@gmai.com.


License
----

MIT


**Free Software, Alhamdulillah Yeah!**

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
