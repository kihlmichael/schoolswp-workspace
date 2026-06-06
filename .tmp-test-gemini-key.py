import urllib.request
import json
import os

key = "AIzaSyDu2pox3mKj9ZuEuB-W1xnYjKsxjeuyW1E"

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={key}"
payload = {
    "contents": [{"parts": [{"text": "Hello, is this key working?"}]}]
}
payload_bytes = json.dumps(payload).encode("utf-8")

req = urllib.request.Request(
    url,
    data=payload_bytes,
    headers={"Content-Type": "application/json"},
    method="POST"
)

try:
    with urllib.request.urlopen(req) as resp:
        print("Success! Response:")
        print(resp.read().decode("utf-8"))
except Exception as e:
    print("Error:", e)
