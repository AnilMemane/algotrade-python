import logging
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect(api_key="tdpsoq22bb0p58qs")

# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
# Once you have the request_token, obtain the access_token
# as follows.

data = kite.generate_session("9rR5Nad73FPKHKg4lqbB52WcQuz7cXSh", api_secret="10qzhgg81vsvwy8cijhl6q305lcgu0gt")
kite.set_access_token(data["access_token"])

# Place an order
# # Fetch the LTP (Last Traded Price) for a specific instrument
instrument_token = "260105"  # Replace with the instrument token of the stock you want to fetch

# Fetch LTP
ltp = kite.ltp("NSE:INFY")
print(ltp)


option_data = kite.option_chain('NSE') # You can specify the exchange here, like NSE or BSE
# Access option data as per your requirement
print(option_data)


# Extract the price from the response
# price = ltp[f"NSE:{instrument_token}"]["last_price"]
# print(f"The current price of the instrument is: {price}")

# try:
#     order_id = kite.place_order(tradingsymbol="INFY",
#                                 exchange=kite.EXCHANGE_NSE,
#                                 transaction_type=kite.TRANSACTION_TYPE_BUY,
#                                 quantity=1,
#                                 variety=kite.VARIETY_AMO,
#                                 order_type=kite.ORDER_TYPE_MARKET,
#                                 product=kite.PRODUCT_CNC,
#                                 validity=kite.VALIDITY_DAY)

#     logging.info("Order placed. ID is: {}".format(order_id))
# except Exception as e:
#     logging.info("Order placement failed: {}".format(e.message))

# # Fetch all orders
# kite.orders()

# # Get instruments
# kite.instruments()

# # Place an mutual fund order
# kite.place_mf_order(
#     tradingsymbol="INF090I01239",
#     transaction_type=kite.TRANSACTION_TYPE_BUY,
#     amount=5000,
#     tag="mytag"
# )

# # Cancel a mutual fund order
# kite.cancel_mf_order(order_id="order_id")

# # Get mutual fund instruments
# kite.mf_instruments()