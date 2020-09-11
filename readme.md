				## WIKIPEDIA SEARCH ENGINE ##
The mini project involves building a search engine on the Wikipedia Data Dump without using any external index. For this project, we use the data dump of size ~73 GB. The search results return in real time. Multi-word and multi-field search on Wikipedia Corpus is implemented.

You also need to rank the documents and display only the top 10 most relevant documents.

Key challenge
To implement multi level data indexing to provide on demand search results(i.e in less than a sec) in memory through disk reads.

How things are done:
SAX is used to parse the XML Corpus without loading the entire corpus in memory. This helps parse the corpus with minimum memory. After parsing the following morphological operations are performed to obtain clean vocabulary.

Stemming : It is done using Pystemmer  library of python.

Casefolding : Casefolding is easily done through lower().

Tokenisation : Tokenisation is done using regular expressions.

Stop Word Removal: Stop words are removed by referring a stop word list that is maintained in a seperate file.

Term filter : This removes some of the common terms that are found in abundance in all the pages. These include terms like redirect,URL,png, HTTP etc.

NOTE One major optimization is done in stemming to reduce time of indexing is that, till 50000 document any repeatative word is not again stemmed,i.e we have used dynamic programming based approach here because stemming is time consuming and this has reduced indexing time to half.

As a part of Primary Inverted Index we have multiple no of  files
. Index_n : Each file holding a posting list correspond to that word


In order for O(1) access of title we have maintained 1 pickle file that keep track of title corresponding to docId.

Secondary Index:

. SecondaryIndex : It holds the entry corresponds to each file of Primary Index.Make searching Faster.

	  `XYX:d456b45t23i76 d23b5t7
Ranking Factor While building index ranking of top 10 document corresponding to a word is done using td-idf and build a champion list and write into file.

Merging all temporary indexes using block based k way merge sort algorithm We have made

Term Field Abbreviations For Search:
. i abbreviated as infobox

. b abbreviated as body

. t abbreviated as title

. e abbreviated as ext

. r abbreviated as ref

. c abbreviated as category

Query Format
. Field Query : 't:abc b:xyz c:xxy i:dde e:ref r:ext'

. Normal Query : word1 wor2 word3

How Searching in Less than a sec
.For normal query we do a binary search on Secondary Index and get the fileNumber of primary file, after that we extract the posting list corresponds to each word in query, then we calculate TFIDF score for each docID where word(Query) occurs and return top K documents title
. For field query instead of calculating frequency of body we calculate frequency of that field and get documentID and rest all process goes same as normal query.
