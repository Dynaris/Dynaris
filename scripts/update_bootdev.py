import re
import requests

html = requests.get(
    "https://www.boot.dev/u/dynaris",
    timeout=30
).text

print(html[:1000])
