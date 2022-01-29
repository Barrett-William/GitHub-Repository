#Twitter limit: 900 requests/15-minutes, 300/3 hours post update
def Tweet(x):

    import tweepy, json

    # Retrieve Auths from Json
    path = path = r"C:\Users\Will\Desktop\GitHub-Repository\Twitter_Bot_Project\tweepy-bots" + '\\'
    with open(path+"AuthTwitter.json", 'r') as f:
        MyAuths = json.load(f)
    
    consumer_key = MyAuths["API Key"]
    consumer_secret = MyAuths["API Key Secret"]
    access_token = MyAuths["Access Token"]
    access_token_secret = MyAuths["Access Token Secret"]

    #Authenticatw to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
    except:
        print("Error during authentication")

    # Create a tweet
    api.update_status(x)
    
    return "Tweet posted. "