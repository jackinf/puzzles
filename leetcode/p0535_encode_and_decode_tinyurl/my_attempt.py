import hashlib


class Codec:
    def __init__(self):
        self.cache = {}
        self.prefix = "https://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = hashlib.md5(longUrl.encode('utf-8')).hexdigest()
        self.cache[key] = longUrl
        return self.prefix + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl[len(self.prefix):]
        return self.cache[key]