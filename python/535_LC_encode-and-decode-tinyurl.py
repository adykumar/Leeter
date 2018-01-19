import random, string
class Codec:

    enc= {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        rand_arr= []
        for i in range(6):
            rand_arr.append(random.choice(string.ascii_letters+string.digits))
        short= ''.join(rand_arr)
        short= "http://tinyurl.com/"+short
        if short in self.enc:
            self.encode(longUrl)
        self.enc[short]= longUrl
        return short

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.enc[shortUrl]

if __name__=="__main__":
    lis=["google.com","facebook.com"]
    for each in lis:
        obj= Codec()
        print obj.encode(each)
        print obj.decode(obj.encode(each))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
