Title: Dataclysm: The very best of
Date: 2015-02-25
Category: Data Science
Tags: data science, review
Summary: I recently read Dataclysm by Christian Rudder. These are some of my favorite stories from this book.

I recently read [Dataclysm](http://dataclysm.org) by [Christian Rudder](https://twitter.com/christianrudder). If you don't know him, Christian Rudder is one of the founders of [OkCupid](https://www.okcupid.com), a very popular online dating website.

In OKCupid, as in other dating websites, users create a profile, put up some pictures, and write some stuff about themselves. They can then rate other users and send them private messages with the purpose of getting a date and, if they are lucky, find that special someone. When you're creating your profile and from time to time, the website also asks you several questions, some of their answers will be kept private, others will be put up on their profile pages.

OKCupid website has a companion blog, [OkTrends](http://blog.okcupid.com), where its creators (the DataCupids!) discuss and analyze trends and stereotypes, debunk myths, give advice, and much more, all using data from OKCupid. Dataclysm takes some of the most popular stories from this blog, expands them, and adds in a few more external datasets (Twitter, Facebook, Reddit, just to name a few) for extra punch.

Dataclysm is essentially about making sense of Big Data. It's about how, faced with a deluge (cataclysm) of data, we can use good data analysis to draw great insights. More generally the book presents an uplifting message that many insights that would otherwise have required years of work, expensive setups, and many test subjects, are now possible with careful analysis of existing datasets. Instead of doing an intensive review of the book, which is but a simple google search away, I will instead highlight some of my favorite stories from the book.


### Men of all ages prefer 20 year old women.

While this may seem shocking at first it actually make some sense from a biological perspective. Males are hardwired to "spread their seed" so it makes sense that they would look for the most fertile females. In contrast, women exhibit much more socially acceptable preferences: women under 30 prefer men slightly older than themselves; women over 30 prefer men slightly younger than themselves, although never going above 40. Does this mean the human race is doomed? Are all men perverts? Probably not. When looking at the actual messaging rates for men, the datacupids found that men actually message women who are at most 9 years younger than them. This is possibly due to social stigma.


### Is Twitter degrading our language?

As you may know, Twitter messages are limited to 140 characters. Because of this apparent restriction it did not take long before people started predicting that language skills would begin to degrade with increasing Twitter use. That, in fact, did not happen. The datacupids compared the most common words on Twitter with those from the [Oxford English Corpus](https://en.wikipedia.org/wiki/Most_common_words_in_English) (OEC) (the *de facto* repository of modern english words) and found that:

1. The average Twitter word is 4.3 characters long compared to 3.4 in the OEC;
1. Twitter's top 100 word list which do not show up in the OEC are heavily related to feelings and declarative nouns such as home, life, best, today, etc.

So, in fact, Twitter's limit of 140 characters is not a restriction but a catalyst for innovation.  "Twitterites" increase the information density of their communications. They jump straight to the point, be it breakfast or landing on comets.
**Myth busted!**


### Love is blind.

A couple of years ago, to conclusively prove that love is blind, OKCupid removed all profiles photos from the website for a few hours. Well, not really. It was actually to promote a mobile app called [Crazy Blind Date](http://en.wikipedia.org/wiki/Crazy_Blind_Date). During that day, the number of messages exchanged on the website abruptly dropped to almost zero! While the app itself lasted only a few months, it still managed to serve blind dates to about 10,000 people. How did they feel about those blind dates? [_They loved them_!](http://blog.okcupid.com/index.php/we-experiment-on-human-beings/) Users, both male and female, reported having a great time, regardless of the other person's attractiveness. Maybe there is some truth to this myth after all.


### There are no borders anymore.

This one isn't really a story but a whole chapter providing evidence to something that is becoming more and more evident and that yet many world leaders still refuse to accept for whatever reason: Physical borders not cultural borders. The internet has totally redefined how we can chart cultural similarity. A few years ago [Pete Warden](http://petewarden.com/about/) scrapped Facebook data and calculated the clusters from the USA user connections. He [found](http://petewarden.com/2010/02/06/how-to-split-up-the-us/) that people belonged to one of 7 "states" instead of the physical 50. In a maybe-not-so-different context, the datacupids found a totally different set of borders. Reddit, the front page of the internet, is organized into thousand of themed "subreddits". Looking at the most popular ones, and the frequency of posts across the different subreddits, the datacupids [found](http://www.slate.com/articles/technology/technology/2014/10/mapmaking_using_reddit_okcupid_twitter_and_other_social_media_websites.html) a thriving "country" whose "state" borders are defined by common interests and location defined by similarity of interests.
