# Scottish Gaelic Word Frequency Lists

Frequency lists of words and collocations created from learning resources covering a range of subjects on [LearnGaelic](https://learngaelic.scot/).

## What is this?
Sets of lists of Gaelic words, sorted by their frequency in 

## Where are they from?
They were generated from the following sources:
* 
*
*

## Why would I want it?
Being able to follow the [Litir Bheag](https://learngaelic.scot/litirbheag/index.jsp), [Litir do Luchd-ionnsachaidh](https://learngaelic.scot/litir/index.jsp) or [Watch Gaelic](https://learngaelic.scot/watch/news.jsp) makes a  major milestone in Gaelic learning, because it opens up a huge amount of comprehensible input to immerse or study from, with clear audio and translations. Frequency lists can help accompany these - either by helping identify the most common vocabulary needed for them to be comprehensible, or in making decisions about which of the new vocab encountered will be most useful to learn first.

Also, some people like to work through frequency lists as a means of learning in general. There is an existing frequency list kindly provided by [iGàidhlig](http://www.igaidhlig.net/en/gaelic-word-frequencies/) which you might also want to check out. Because of the corpus it was created from though, it highly favours terms like "pàrlamaid" and "comataidh" which wont necessarily be the most encountered words for a learner. The frequency lists here are just as biased by the sources they draw from, but that's not a terrible thing if you're planning to study those sources. Additionally the [frequency lists created from Watch Gaelic](https://github.com/innesmck/GaelicFrequencyLists/tree/main/output/watch) includes spoken content on a fairly broad range of topics, so might (in my incredibly non-expert, gaelic learning opinion) make a reasonable general purpose list.

## What are the different types of list?
* [Frequency.csv](https://github.com/innesmck/GaelicFrequencyLists/blob/main/output/litir/frequency.csv) - A list of individual words and a count of how many times they were encountered in the corpus. This can be useful for finding the vocabulary you need to learn to understand enough of the resource to benefit from it, or to make decisions about which new words you encounter to prioritise.
* [Bigrams1.csv](https://github.com/innesmck/GaelicFrequencyLists/blob/main/output/litir/bigrams1.csv) - Pairs of words ordered by how often they appear together in the source text. This can be useful for finding common phrases like "gu bheil" or "'s docha", or which prepositions frequently appear with a verb like "coltach	ri" or "fuireach anns". Excludes definite articles and some single character words, to avoid the list largely being "an cat", "an cù" etc.
* [Bigrams2.csv](https://github.com/innesmck/GaelicFrequencyLists/blob/main/output/litir/bigrams2.csv) - Pairs of words of four characters or longer, to help find common phrases, or pairs of adjectives and nouns commonly used together.
* [Trigrams.csv](https://github.com/innesmck/GaelicFrequencyLists/blob/main/output/litir/trigrams.csv) - Sets of three words, to help find phrases including articules which needed to be excluded from the bigrams.
