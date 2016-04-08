
import json
from urllib.request import urlopen

TOKEN="9ec2dd65920b14f33200cc3b57db7b8f2cd0811c"
ROOT_URL = "https://api-ssl.bitly.com"
SHORTEN = "/v3/shorten?access_token={}&longUrl={}"

class BitlyHelper:
	def shorten_url(self,longurl):
		try:
			url = ROOT_URL + SHORTEN.format(TOKEN,longurl)
			response = urlopen(url).read()
			jr = json.loads(response)
			return jr['data']['url']
		except Exception as e:
			print (e)


