# 💱 Live Currency Converter

> Convert between world currencies using **live exchange rates**, straight from your terminal. If the internet fails, it tells you politely instead of crashing.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![API](https://img.shields.io/badge/Data-Live%20REST%20API-0A66C2)
![Library](https://img.shields.io/badge/Library-requests-2EA44F)

---

## ✨ What it does

Type an amount, pick two currencies, and get the answer using today's rates. It works for any currency pair the API supports, such as Naira to US dollars or pounds to Naira.

- 🌍 **Live rates** downloaded from a public exchange-rate API
- 🔁 **Any pair**: for example `NGN → USD`, `GBP → NGN`, `EUR → JPY`
- 🛡️ **Crash-proof**: handles no internet, slow servers and unknown currency codes
- ⌨️ **Forgiving input**: `ngn` and `NGN` both work

---

## 🎬 See it in action

```text
Live rates loaded!

Amount (or q to quit): 15000
From (e.g. NGN): ngn
To (e.g. USD): usd
15000.0 NGN = 10.0 USD

Amount (or q to quit): q
```

> The numbers above are a sample. Real results depend on today's rates.

---

## 🚀 Run it

```bash
git clone https://github.com/YOUR-USERNAME/currency-converter.git
cd currency-converter
python -m pip install requests
python converter.py
```

> 💡 On Windows, if `pip` is not recognised, `python -m pip` works every time.

---

## 🧠 How it works

1. **Ask the API.** `requests.get(url, timeout=10)` sends a request to the exchange-rate service. The `timeout` stops the program from waiting forever.
2. **Check the answer.** Status code `200` means success. Anything else prints a clear message.
3. **Read the data.** `response.json()` turns the reply into a Python dictionary of rates.
4. **Convert using USD as a bridge.** All rates are "per 1 US dollar", so the app divides by the starting currency's rate to get dollars, then multiplies by the target currency's rate.

```python
def convert(amount, from_cur, to_cur, rates):
    in_usd = amount / rates[from_cur]
    return in_usd * rates[to_cur]
```

Example: 15,000 NGN ÷ 1,500 = 10 USD, then 10 × 0.79 = 7.9 GBP (sample rates).

---

## 🗂️ Project structure

```text
currency-converter/
├── converter.py
└── README.md
```

---

## 📚 What I learned building this

- What an **API** is and how a program talks to someone else's server
- Sending a **GET request** and reading **JSON**
- HTTP **status codes** (200 = success, 404 = not found, 500 = server error)
- Writing safe network code with **timeouts** and `try / except`
- Checking data (`not in`, `is not None`) before using it

---

## 🔭 Ideas for next time

- [ ] Save a conversion history to a file
- [ ] Cache the rates so the app does not call the API every run
- [ ] Add a web page for it with JavaScript

---

👤 **Godwin** · Lagos, Nigeria
🔗 [GitHub](https://github.com/YOUR-USERNAME) · [LinkedIn](https://linkedin.com/in/YOUR-LINK)
