import urllib.request, urllib.error, urllib.parse, sys, time
from bs4 import BeautifulSoup

# arguments are the entry or inclusive range of entries to download
first = int( sys.argv[1] )
if( len(sys.argv) <= 2 ):
	last = first + 1
else:
	last = int( sys.argv[2] ) + 1

def getEntries( urlpart, outdir, htmlid ):
	# count any failures so we can see what they contain
	failed = []

	# loop over required letters
	for x in range( first, last ):

		try:
			headers = {}
			headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
			headers['accept-language'] = "en-GB,en;q=0.9,gd-GB;q=0.8,gd;q=0.7,en-US;q=0.6"

			url = 'https://learngaelic.scot/' + urlpart + str(x)
			print( 'Reading ' + url) 

			# download letter and parse
			request    = req = urllib.request.Request(url, headers = headers)
			response   = urllib.request.urlopen( request )
			webContent = response.read()
			soup       = BeautifulSoup(webContent, 'html.parser')

			# find the html div we are after from the html document
			paragraphs = soup.find(id=htmlid).find_all('p')

			if len( paragraphs ) == 0:
				raise Exception("Empty file")

			# write out the letter in a text file
			print( 'Writing corpus/' + outdir + str(x) + '.txt')
			f = open('corpus/'  + outdir + str(x) + '.txt', 'w', encoding="utf-8")
			for p in paragraphs:
				f.write(p.get_text())
			f.close

			time.sleep(.5)

		except:
			print( 'FAILED corpus/' + outdir + str(x) + '.txt')
			failed.append( x )

	print( "Failed entries:" + f'{failed}' )

getEntries( 'litir/index.jsp?l=', 'litir/litir', 'gaelictrans' )
getEntries( 'watch/documentaries.jsp?v=', 'watch/watch', 'gdTranscript' )


