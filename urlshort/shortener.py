import random
import string
from .models import *

# def shortenIt():
#     num = random.randint(1000, 100000)
#     hashes = Hashids(min_length=5)
#     h = hashes.encode(num)
#     if UrlShort.objects.filter(short=h).exists():
#         shortenIt()
#     return h

def shortenIt(size=7, chars=string.ascii_lowercase + string.digits):
    temp = ''.join(random.choice(chars) for _ in range(size))
    if UrlShort.objects.filter(short=temp).exists():
        shortenIt()
    return temp
