Overview: The core problem addressed is the automated generation of concise summaries from lengthy texts, a process that preserves the essential information and overall meaning of the original content. This involves distilling the most important and relevant information into a shorter, coherent representation.

Steps Involved in the Project:

● Tokenizing sentences

● Creating a frequency matrix of words in each sentence

● Calculating Term Frequency (TF) and generating a matrix

● Creating a table of documents per words

● Calculating Inverse Document Frequency (IDF) and generating a matrix

● Calculating TF-IDF and generating a matrix

● Scoring the sentences

Solution Approach:
The text summarization system follows an extractive summarization approach. In extractive summarization, we select portions (sentences or paragraphs) from the original text that are most relevant and combine them into a summary. The approach can be broken down into several key
steps:
1. Text Preprocessing:
a. Tokenization: The text is split into individual sentences and words.
b. Stopword Removal: Common words that do not add significant meaning (e.g.,
“the”, “is”, “in”) are removed.
c. Stemming: Words are reduced to their root form (e.g., “running” becomes “run”).
2. Frequency Calculation:
a. A frequency table is built to count the number of times each significant word
(non-stopword) appears in the text.
3. Sentence Scoring:
a. Sentences are scored based on the frequency of words they contain. Sentences
with higher scores are considered more important.
4. Threshold Calculation:
a. The average sentence score is calculated. Sentences with scores higher than the
threshold are considered relevant for the summary.
5. Summary Generation:
a. Based on the scores, the sentences that contribute most to the overall meaning
of the text are selected and combined to form the summary

3. Algorithm Overview:
The algorithm can be broken down into the following steps:
Step 1: Tokenize the input text into sentences:
● Tokenization is the process of breaking down the text into smaller chunks (i.e.,
sentences or words).
● You first split the text into sentences using sent_tokenize() and into words using
word_tokenize().
● This is important because we need to analyze each sentence individually and
understand the frequency of each word.
Step 2: Remove stopwords (common, unimportant words):
● Stop words are common words like “is,” “the,” “a,” etc., which don’t carry much meaning
and can be removed from the text to focus on more important words.
● Using stopwords.words(‘english’), you create a list of stop words to filter them out of the
word tokens.
Step 3: Stem each word to its base form:
● Stemming is the process of reducing a word to its base or root form. For example:
○ “running” becomes “run”
○ “better” becomes “bet”
● This ensures that words with the same base form are treated as the same, improving the
accuracy of the summary.
Step 4: Build a frequency table of words:
● The frequency table calculates how often each word appears in the text.
● You then store the frequency of non-stop words in a dictionary called freqTable
● This helps in understanding which words are more important based on their frequency.
Step 5: Score each sentence based on the frequencies of the words in it:
● Sentences are assigned a score based on the frequency of important words (non-stop
words) they contain.
● Each sentence is evaluated by calculating the sum of the frequency of the important
words divided by the total number of words in that sentence.
● Sentences with more frequent important words will score higher, meaning they are more
likely to be included in the summary.
Step 6: Calculate an average sentence score to use as a threshold:
● To identify which sentences are significant enough to be included in the summary, the
average score of all sentences is calculated.
● The sentences with scores higher than the threshold (which is the average score
multiplied by a constant factor) are considered for the summary.
Step 7: Select sentences with scores above the threshold to form the summary:
● The final step involves extracting the top sentences from the original text.
● Sentences with scores greater than or equal to the threshold are included in the
summary.
● The result is a shortened version of the original text with the most relevant information.



