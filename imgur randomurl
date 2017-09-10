import requests
import time
def randimgurLink():
  from random import sample
  a=["0123456789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"]
  b="http://imgur.com/gallery/"
  c=sample(a[0],5)
  return b+"".join(c)

for x in range(100):
    url = randimgurLink()
    r= requests.get(url)
    if str(r)!="<Response [404]>":
        print(url)
        time.sleep(2)
