# VictoriaCinemaBot
Little Bot that scrapes my local Cinema Website: https://www.victoriacinema.it/victoria_cinema/index.php and displays information about movies:
* When they are in the theater
* Duration
* Cast
* Direction
* Genere

## How to make it works?
After installing the requirements (I auto generated it with _pipreqs_), you can execute the following line:
```bash
bash container.sh
```
Note that in all the bash scripts I used _python3_ as python command. Make sure that your system has this command available, otherwise the script may not works at all.

### Screenshots
![screenshot_1](https://user-images.githubusercontent.com/59342085/165149574-523d1478-945d-4156-9f17-e4c8f50d6c48.png)
![screenshot_2](https://user-images.githubusercontent.com/59342085/165149579-d7c0a80a-714f-4a25-ba7c-e32b699b8a2d.png)

The only available command at the moment is _start_, that display all the movies that are in the theater. For every movie there's a link trailer and a reservation link. Both the links are taken from the website, but sometimes the trailer one not works properly. That's because can happens that the admin of the website, post a new film without the trailer link (or with a dummy one).

### How it works?
The bot has two parts:
* bot itself
* movie updater

The first aim to display information to the user every time he presses the button on the telegram chat. The movie updater is responsible for retrieves the movies information (once every hour) and saving them into files. I handle all this things with a _containter_ writte in _bash_. It makes run the updater once per hour and keep up the bot.

### About the website
The website is done by https://www.creaweb.it/creaweb/index.php, a company that seems to create website (_php_ based) for movie theaters. The website has got a curious html configurations, in which movies are divided in Even and Odd, so I had two to write similar funcion to catch the _even movies_ and the _odd_ ones. Then I put everything in two differnts list (_even, odd_) and saves everything to file. The bot open the file, read the content and print it to the user. Thanks to this task division, the bot doesn't have to calculate every time for every user all the available movies. This cames quite handy also because I do a lot of operations with string, that may requires sime time (depending on the hardware on whic the bot is working)

##### About messy commits
I did a wrong commit of something like 4 file at once, but I'm lazy so I don't think I'm gonna fix it for now :(
