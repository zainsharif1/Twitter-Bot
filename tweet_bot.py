import tweepy
import random
import time
from user_prompt import word_prompt, geo_area
from tweepy_api_setup import api_setup, t_posts

def random_retweet_function(prompt_list, twitter_posts, api, geo_area):
    """
    The function accesses the user provided twitter API's homepage to identify
    tweets containing the supplied agriculture finance keywords. Once the tweet
    is identified by keyword AND location/country of origin, the tweet is
    retweeted randomly as determined by the randomizer boolean functions.
    The tweet is also unretweeted at random as well.

    Finally, some statistics are printed from the function:
    - Number of tweets with key words found
    - Number of key words found
    - Number of retweets
    - Number of undo tweets
    - The list of countries for each tweet origination

    Inputs:
    - prompt_list(list) : list of prompt/keywords to be tracked for retweets
    - twitter_posts(list): nested list of tweet specific information

    Returns(str): print statements for statistics mentioned above

    """

    #create a list of location from the tweet
    location_lst = list()
    #create a list of tweet ids to track
    tweet_id_lst = list()

    #count of words, retweet and undo initializer
    count_wrd=0
    count_retweet=0
    count_undo=0

#iterate through the posts to check if word in prompt list
    for post in twitter_posts:
    #generate random element to be used for retweet
        randomizer = random.choice([True,False])

    #create dictionary of tweet specific data returned from current tweet
    #tweet_id : retrieve tweet id
    #is_retweeted: retrieve boolean state for retweeted
    #wrds: make all the words lowercase to eliminate capitalization errors
    #json: retrieve _json list
        post_dict = {'tweet_id': post.id, 'is_retweeted': post.retweeted,
                    'wrds': post.text.lower().split(), 'json': post._json}

    #index user list to return the 'location' and store in a list
        location=post_dict['json']['user']['location']
        location_lst += location.split()
        country_tweets= list()

    #iterate to check if word is in prompt list and if the tweet originated from specified geo location
        for wrd in post_dict['wrds']:
            for country in location_lst:
                if wrd in prompt_list and country in geo_area:
                    print(wrd, "word found!")
                    count_wrd +=1
                    country_tweets.append(country)
    #iterate to check if the tweet has already been seen
                    if post_dict['tweet_id'] not in tweet_id_lst:
                        tweet_id_lst.append(post_dict['tweet_id'])
    #check to see if the tweet has already been retweeted, then randomly retweet
                        if post_dict['is_retweeted'] is False and randomizer == True:
                            api.retweet(post_dict['tweet_id'])
                            count_retweet= count_retweet +1
    #check to see if the tweet has not been retweeted before, and randomly undo the retweet
                        elif post_dict['is_retweeted'] is True and randomizer == False:
                            api.unretweet(post_dict['tweet_id'])
                            count_undo = count_undo +1

    print("\nNumber of tweets with key words found:", len(tweet_id_lst))
    print("Number of key words found:", count_wrd)
    print("Number of retweets:", count_retweet)
    print("Number of undo tweets:", count_undo)
    print("The list of countries for each tweet origination:", str(country_tweets)+"\n")

# count initializer for count of loop
count_loop=0
while True:
    #set n to be a random number b/w 0 and 99
    n = random.randrange(100)
    random_retweet_function(word_prompt(), t_posts(), api_setup(), geo_area())
    count_loop = count_loop +1
    print("Loop has now run "+str(count_loop)+" time(s)\n")
    user_input = input("""Press 'q' to quit, any key to continue the loop\n""")
    if user_input.lower() == str('q'):
        #quit the program
        print("Quitting twitter bot...")
        break
    else:
        print("\nContinuing...")
        #wait random amount of seconds to recall the function
        time.sleep(n)
        continue
