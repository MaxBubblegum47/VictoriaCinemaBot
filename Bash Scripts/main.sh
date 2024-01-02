#!/bin/sh

if [[ -f 'saveEven.txt' ]] & [[ -f 'saveOdd.txt' ]]
then
	echo "Save files are present. I'm starting the bot."
	bash helper_main.sh &
else
	echo "There are not save files available. I'm starting Movie.py."
	bash helper_movie.sh	
fi



while true
do
	echo "Updating Movies"
	bash helper_movie.sh	
	sleep 3600
done
