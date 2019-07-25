import tweepy

def api_setup():
    """
    Setup and authentication of twitter API dev account with user specific
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET.

    Inputs: None
    Returns(str): list
    """

    #login details from Twitter dev API
    CONSUMER_KEY=
    CONSUMER_SECRET=
    ACCESS_KEY=
    ACCESS_SECRET=

    # details needed to login to Twitter dev account
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    #setting up api object to read/write from twitter
    api = tweepy.API(auth)

    return api

def t_posts():
    """ Access the homepage of tweets based on the api setup

    Input: None

    Returns(list): nested list

    """

    api = api_setup()

    #tweepy function to invoke the posts on bot's timeline (includes accounts being followed)
    tposts = api.home_timeline()

    return tposts
