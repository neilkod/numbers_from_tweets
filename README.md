numbers from tweets
===================

given input as raw twitter data in json format, this code will do the following:
- strip entities from the tweet (hashtags, url, @username mentions)
- print each number from the tweet on its own line

Entity mentions are stripped using data from twitter's supplied entities, including start/end position. Although I haven't measured the performance, it should be faster than performing multiple regex substitutions against each tweet.

usage:

    time zcat ~/one_point_five_million_tweets.Z |python output_numbers_from_tweets.py > numbers_from_1point5milliontweets.txt

todo:
-~~flag for determining whether or not to strip entities~~

why?
====

I think some useful things can be done with the numbers that are extracted from a large-ish number of tweets. The first thing I checked was to see if the extracted numbers from 12e6 tweets fit [benford's law][1]. Spoiler alert: They did!

    nkodner@hadoop4 numbers_from_tweets$ awk '{print substr($1,0,1)}' output/numbers_from_12milliontweets_cast_as_long.txt |sort -n|uniq -c|sort -nr
    541115 1
    399356 2
    373189 3
    213307 5
    135144 4
    85316 8
    83887 6
    74252 9
    73089 7
    73051 0

We can also find which numbers occur most frequently in this sample of tweets:

    nkodner@hadoop4 numbers_from_tweets$ cat output/numbers_from_12milliontweets_cast_as_long.txt |sort|uniq -c|sort -nr|head -25|awk '{printf "%d. %s\n",NR,$0}'
    1. 267416 3
    2. 163757 2
    3. 143249 1
    4. 117857 5
    5. 81915 4
    6. 73051 0
    7. 61276 10
    8. 55091 8
    9. 52567 6
    10. 52285 11
    11. 51008 2012
    12. 45012 12
    13. 44958 7
    14. 37254 9
    15. 32759 30
    16. 31647 20
    17. 27792 15
    18. 26327 100
    19. 20465 13
    20. 18965 18
    21. 18472 50
    22. 17956 14
    23. 17068 16
    24. 13841 24
    25. 13715 19

[1]: http://en.wikipedia.org/wiki/Benford%27s_law

