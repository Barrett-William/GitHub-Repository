#Twitter limit: 900 requests/15-minutes, 300/3 hours post update
def Tweet(x):

    import tweepy, json

    # Authenticate to Twitter
    MySecrets = json.loads("AuthTwitter.json")
    auth = tweepy.OAuthHandler(MySecrets["OAuthHandler"])
    print(auth)
    auth.set_access_token(MySecrets["AccesToken"])

    # Create API object
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
    except:
        print("Error during authentication")

    # Create a tweet
    api.update_status(x)
    
    return "Tweet posted. "
