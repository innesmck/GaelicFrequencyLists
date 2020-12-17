import nltk, sys, re
from nltk.corpus       import PlaintextCorpusReader
from nltk.tokenize     import TreebankWordTokenizer
from nltk.util         import bigrams, trigrams
from collections import Counter

stop_short   = [ 'an', 'am', 'na', 'a', 'e', 'i', 'a’', 'ag' ]
stop_numbers = [ 'trì', 'ceithir', 'còig', 'sia', 'seachd', 'ochd', 'naoi', 'deich', 'deug', 'fichead' ]
stop_common  = [ 'chan', 'eil', 'cha', 'robh', 'tha', 'bha', 'agus', 'th’', 'bh’' ]
punctuation  = '!"#$%&()*+,./:;<=>?@[\\]^_`{|}~'

def write_bigrams( words, name, minlength, count ):
	print("Finding " + name)
	stopfilter = lambda w: len(w) < minlength or w in stop_short + stop_numbers + stop_common

	collocs = Counter( bigrams(words) )
	collocs = Counter({ key : val for key, val in collocs.items() if not stopfilter(key[0]) and not stopfilter(key[1]) })
	collocs = collocs.most_common(count)

	f = open( name + '.csv', 'w', encoding="utf-8")
	for word, val in collocs:
	    f.write(u'{},{},{},\n'.format(word[ 0 ], word[ 1 ], val))
	f.close


def write_trigrams( words, name, minlength, count ):
	print("Finding " + name)
	stopfilter = lambda w: len(w) < minlength or w in stop_numbers + stop_common + [ 'e', 'i' ]

	collocs = Counter( trigrams(words) )
	collocs = Counter({ key : val for key, val in collocs.items() if not stopfilter(key[0]) and not stopfilter(key[1]) and not stopfilter(key[2]) })
	collocs = collocs.most_common(count)
	
	f = open( name + '.csv', 'w', encoding="utf-8")
	for word, val in collocs:
	    f.write(u'{},{},{},{}\n'.format(word[ 0 ], word[ 1 ], word[ 2 ], val))
	f.close


indir = sys.argv[1]
outdir = sys.argv[2]
if len( outdir ) > 0:
	outdir = outdir + '/'

# load corpus
corpus = PlaintextCorpusReader(indir, '.*', TreebankWordTokenizer(), encoding='utf-8')
words = corpus.words()
print('Loaded corpus containing ' + str(len(words)) +' tokens')

# filter and modify word list
# removing words here will create incorrect collocations so only remove invalid characters
words = [word.lower() for word in words]
words = [word.translate(str.maketrans('', '', punctuation)) for word in words ]
words = [word for word in words if len(word) > 0]
words = [word for word in words if bool(re.match("^.*?[A-zÀ-ú].*$", word )) ]
print('Processed corpus contains ' + str(len(words)) +' words')

# write out collections
write_bigrams(  words, outdir + "bigrams1", 0, 5000 );
write_bigrams(  words, outdir + "bigrams2", 4, 2000 );
write_trigrams( words, outdir + "trigrams", 0, 3000 );
