import http.client, json, alpaca_trade_api as tradeapi

def main(stock):

    with open("AuthAlpaca.json", 'r') as f: #Host and key stored locally
        MyDict = json.load(f)
    api_key = MyDict["API Key ID"]
    api_secret = MyDict["API Secret Key"]
    base_url = MyDict["endpoint"]

    # instantiate REST API
    api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
    
    # obtain account information
    account = api.get_account()
    print(account)

    DayStock = api.get_barset(stock, 'day')
    print(DayStock.df)

    QtrHStock = api.get_barset(stock, '15Min', limit=1000)
    print(QtrHStock.df)

if __name__ == '__main__': main("AAPL")