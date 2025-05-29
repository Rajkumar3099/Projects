import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import heapq

# Download required NLTK datasets (run this once)
# nltk.download('punkt')
# nltk.download('stopwords')

text_str = '''
Those Who Are Resilient Stay In The Game Longer
“On the mountains of truth you can never climb in vain: either you will reach a point higher up today, or you will be training your powers so that you will be able to climb higher tomorrow.” — Friedrich Nietzsche
Challenges and setbacks are not meant to defeat you, but promote you. However, I realise after many years of defeats, it can crush your spirit and it is easier to give up than risk further setbacks and disappointments. Have you experienced this before? To be honest, I don’t have the answers. I can’t tell you what the right course of action is; only you will know. However, it’s important not to be discouraged by failure when pursuing a goal or a dream, since failure itself means different things to different people. To a person with a Fixed Mindset failure is a blow to their self-esteem, yet to a person with a Growth Mindset, it’s an opportunity to improve and find new ways to overcome their obstacles. Same failure, yet different responses. Who is right and who is wrong? Neither. Each person has a different mindset that decides their outcome. Those who are resilient stay in the game longer and draw on their inner means to succeed.
'''

def _create_frequency_table(text_string) -> dict:
    """
    Create a frequency table (word count) for the text string.
    """
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    ps = PorterStemmer()

    freqTable = dict()

    for word in words:
        word = ps.stem(word.lower())
        if word in stopWords or not word.isalnum():
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    return freqTable


def _score_sentences(sentences, freqTable) -> dict:
    """
    Score sentences based on the frequency of words in the sentence.
    """
    sentenceValue = dict()

    for sentence in sentences:
        sentence_words = word_tokenize(sentence.lower())
        sentence_value = 0
        for word in sentence_words:
            if word in freqTable:
                sentence_value += freqTable[word]
        sentenceValue[sentence] = sentence_value

    return sentenceValue


def _generate_summary(sentences, sentenceValue, threshold) -> str:
    """
    Generate summary by selecting sentences that have a score above a threshold.
    """
    summary = ''
    for sentence in sentences:
        if sentenceValue.get(sentence, 0) >= threshold:
            summary += sentence + " "
    return summary


def run_summarization(text):
    """
    Run the text summarization process.
    """
    # 1. Create the frequency table
    freq_table = _create_frequency_table(text)

    # 2. Tokenize the sentences
    sentences = sent_tokenize(text)

    # 3. Score the sentences based on the frequency of words
    sentence_scores = _score_sentences(sentences, freq_table)

    # 4. Calculate the threshold for important sentences
    threshold = sum(sentence_scores.values()) / len(sentence_scores)

    # 5. Generate the summary based on sentence scores
    summary = _generate_summary(sentences, sentence_scores, threshold)
    return summary


if __name__ == '__main__':
    # Run summarization on the provided text
    result = run_summarization(text_str)
    print("Summary:")
    print(result)
