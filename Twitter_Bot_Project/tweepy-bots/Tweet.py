#Twitter limit: 900 requests/15-minutes, 300/3 hours post update
def Tweet(x):

    import tweepy

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("NufbneysTjDX8CWvPW4A3NG6C", "qtGlouy8CuKOOJLBKOzkKjXXAIlVa4SDVrMRJes5i9zJfh2pvX")
    auth.set_access_token("1449445159813406728-yg14Jx9jGBQUpZZJR3KLCDX66tZlB5", "Z6r13Zyd9iakYdHHJWvrzZoDPsEJUtYlABGFoirCyMy3d")

    # Create API object
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
    except:
        print("Error during authentication")

    # Create a tweet
    api.update_status(x)
    print("Tweet posted")
