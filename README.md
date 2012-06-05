numbers_from_tweets
===================

given input as raw twitter data in json format, this code will do the following:
- strip entities from the tweet (hashtags, url, @username mentions)
- print each number from the tweet on its own line

Entity mentions are stripped using data from twitter's supplied entities, including start/end position. Although I haven't measured the performance, it should be faster than performing multiple regex substitutions against each tweet.

usage:

    time zcat ~/one_point_five_million_tweets.Z |python output_numbers_from_tweets.py > numbers_from_1point5milliontweets.txt

todo: flag for determining whether or not to strip entities

why?
====

I think some useful things can be done with the numbers that are extracted from a large number of tweets. The first thing I checked was to see if the extracted numbers fit [benford's law][1]. Spoiler alert: They did!

[1]: http://en.wikipedia.org/wiki/Benford%27s_law
