import random
from hashids import Hashids
from .models import *

def shortenIt():
    num = random.randint(1000, 100000)
    hashes = Hashids(min_length=5)
    h = hashes.encode(num)
    if UrlShort.objects.filter(short=h).exists():
        shortenIt()
    return h
