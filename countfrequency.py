import nltk, sys, re, string
from nltk.corpus   import PlaintextCorpusReader
from nltk.tokenize import TreebankWordTokenizer
from nltk          import FreqDist

# string.punctuation with '’- removed
punctuation = '!"#$%&()*+,./:;<=>?@[\\]^_`{|}~'

# arguments are the number of words to output, the corpus director and an output directory
count  = int( sys.argv[1] )
indir  = sys.argv[2]
outdir = sys.argv[3]
if len( outdir ) > 0:
	outdir = outdir + '/'

# load corpus
corpus = PlaintextCorpusReader(indir, '.*', TreebankWordTokenizer(), encoding='utf-8')
words = corpus.words()
print('Loaded corpus containing ' + str(len(words)) +' tokens')

# process loaded words to strip punctuation, remove t- and h-
words = [word.lower() for word in words]											 # lower case
words = [re.sub(r'^[th]-', '', word) for word in words]								 # strip h- and t-
words = [word.translate(str.maketrans('', '', punctuation)) for word in words ]		 # strip punctuation
words = [word for word in words if bool(re.match("^[A-zÀ-ú][A-zÀ-ú'’-]*$", word )) ] # remove empty and non-words
words = [word for word in words if not bool(re.match("^.*’$", word )) ]				 # remove word parts like bh’ th’
print('Processed corpus contains ' + str(len(words)) +' words')

# create a frequency dictionary from processed words
freqDist = FreqDist(words)
common = freqDist.most_common(count)

# write frequency list to file
print('Writing most frequent ' + str( count ) + ' words to frequency.csv')
f = open(outdir + 'frequency.csv', 'w', encoding="utf-8")

for word, frequency in common:
    f.write(u'{},{},\n'.format(word, frequency))

f.close