import http.client

def main(stock):

    conn = http.client.HTTPSConnection("stock-data-yahoo-finance-alternative.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "stock-data-yahoo-finance-alternative.p.rapidapi.com",
        'x-rapidapi-key': "8aed70d298msh6c2b2452a54a93ep1853b7jsnb8d6c4ad5b7d"
        }

    conn.request("GET", "/v6/finance/quote?symbols="+stock, headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

#if __name__ == '__main__': main("^FTSE")