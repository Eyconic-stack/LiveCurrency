import requests

URL = "https://open.er-api.com/v6/latest/USD"

def get_rates():
    try:
        response = requests.get(URL, timeout=10)
        if response.status_code != 200:
            print("Server problem, code:", response.status_code)
            return None
        data = response.json()
        return data["rates"]
    except requests.exceptions.RequestException:
        print("Could not connect. Check your internet.")
        return None

def convert(amount, from_cur, to_cur, rates):
    in_usd = amount / rates[from_cur]
    return in_usd * rates[to_cur]

rates = get_rates()

if rates is not None:
    print("Live rates loaded!")
    while True:
        text = input("\nAmount (or q to quit): ")
        if text == "q":
            break

        amount = float(text)
        from_cur = input("From (e.g. NGN): ").upper()
        to_cur = input("To (e.g. USD): ").upper()

        if from_cur not in rates or to_cur not in rates:
            print("Unknown currency, try again")
        else:
            result = convert(amount, from_cur, to_cur, rates)
            print(amount, from_cur, "=", round(result, 2), to_cur)