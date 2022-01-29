import http.client, json

def main(stock):

    conn = http.client.HTTPSConnection("stock-data-yahoo-finance-alternative.p.rapidapi.com")

    with open("AuthRapidAPI.json", 'r') as f: #Host and key stored locally
        headers = json.load(f)

    conn.request("GET", "/v6/finance/quote?symbols="+stock, headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

if __name__ == '__main__': main("^FTSE")