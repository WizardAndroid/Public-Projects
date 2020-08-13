# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:45:49 2020

@author: Anurag Joshi
"""
import GetOldTweets3 as got

def get_tweets(startDate,endDate,query,tweetCount):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query)\
                   .setSince(startDate)\
                   .setUntil(endDate)\
                   .setMaxTweets(tweetCount)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    tweets_text = [[tweet.text] for tweet in tweets]
    return tweets_text