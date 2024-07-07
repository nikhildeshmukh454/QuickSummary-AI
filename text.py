import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import pickle

class TextSummarizer:
    def __init__(self, model="en_core_web_sm"):
        self.nlp = spacy.load(model)
        self.stopwords = list(STOP_WORDS)
        self.punctuation = punctuation

    def summarize_text(self, text, summary_percentage):
        doc = self.nlp(text)
        
        word_frequencies = {}
        for word in doc:
            if word.text.lower() not in self.stopwords and word.text.lower() not in self.punctuation:
                if word.text not in word_frequencies:
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

        max_frequency = max(word_frequencies.values())

        for word in word_frequencies.keys():
            word_frequencies[word] = word_frequencies[word] / max_frequency

        sentence_tokens = [sent for sent in doc.sents]

        sentence_scores = {}
        for sent in sentence_tokens:
            for word in sent:
                if word.text in word_frequencies.keys():
                    if sent not in sentence_scores:
                        sentence_scores[sent] = word_frequencies[word.text]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text]

        new_length = int(len(sentence_tokens) * summary_percentage)
        summary_sentences = nlargest(new_length, sentence_scores, key=sentence_scores.get)

        final_summary = [sent.text for sent in summary_sentences]
        summary = ' '.join(final_summary)

        original_length = len(text.split(' '))
        summary_length = len(summary.split(' '))
        

        return summary, original_length, summary_length

# Create an instance of the TextSummarizer
textsum = TextSummarizer()

# Save the instance to a pickle file
with open('textsummarizer.pkl', 'wb') as f:
    pickle.dump(textsum, f)

print("TextSummarizer object has been saved to textsummarizer.pkl")
