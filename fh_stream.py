import websocket

with open('.finnhub_apikey', 'r') as f:
    token = f.read()

print(token)
ws_url = "wss://ws.finnhub.io?token="+token
print(ws_url)
def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print('### closed ###')

def on_open(ws):
    ws.send('{"type":"subscribe", "symbol":"AAPL"}')

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(ws_url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
