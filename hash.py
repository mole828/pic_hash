from collections import Counter
from io import BytesIO
from PIL import Image
from imagehash import phash
import requests


def hash_image(image: Image.Image):
    return phash(image)

def hash_image_file(path):
    image = Image.open(path)
    return hash_image(image)

def hash_url (url: str) -> str:
    resp = requests.get(url)
    tempIm = BytesIO(resp.content)
    image = Image.open(tempIm)
    return hash_image(image)


if __name__ == '__main__':
    pics = [
        './test_file/big.png',
        './test_file/small.png',
        './test_file/split.png',
    ]

    hashs = [(p,hash_image_file(p)) for p in pics]

    print([(h[0],str(h[1])) for h in hashs])