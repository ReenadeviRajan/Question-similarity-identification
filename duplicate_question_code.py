import pandas as pd
import numpy as np
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

stopwords_list = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

def train(file):
    all_data = pd.read_csv(file)
    data = pd.DataFrame(all_data['question1'])
    data = data.dropna()
    # data.head()

    data = data.drop_duplicates(subset='question1')
    data = data[0:100]
    # data.head()
    return data
def my_tokenizer(doc):
    words = word_tokenize(doc)

    pos_tags = pos_tag(words)

    non_stopwords = [w for w in pos_tags if not w[0].lower() in stopwords_list]

    non_punctuation = [w for w in non_stopwords if not w[0] in string.punctuation]

    lemmas = []
    for w in non_punctuation:
        if w[1].startswith('J'):
            pos = wordnet.ADJ
        elif w[1].startswith('V'):
            pos = wordnet.VERB
        elif w[1].startswith('N'):
            pos = wordnet.NOUN
        elif w[1].startswith('R'):
            pos = wordnet.ADV
        else:
            pos = wordnet.NOUN

        lemmas.append(lemmatizer.lemmatize(w[0], pos))

    return lemmas

# print(tfidf_matrix.shape)
def ask_question(k, question):
    query_vect = tfidf_vectorizer.transform([question])
    similarity = cosine_similarity(query_vect, tfidf_matrix)
    f = open("Duplicates.txt", "a",encoding="utf-8")
    flag = 0

    for i in similarity:
        for j in range(len(i)):
            if i[j] != 0 and j != k:
                if flag == 0:
                    f.write(str(k + 1) + ". Question : " + question + "\n\n")
                    f.write("\tSimilar Questions : \n ")

                flag = 1
                f.write("\t" + str(j + 1) + ". " + data.iloc[j]['question1'] + "\n")
                f.write("\t\tSimilarity : " + str("{:.2f}".format(i[j] * 100)) + "% \n")
    f.write("\n\n")


file = "E:\\Examly\\train.csv"
data = train(file)
tfidf_vectorizer = TfidfVectorizer(tokenizer=my_tokenizer)
tfidf_matrix = tfidf_vectorizer.fit_transform(tuple(data['question1']))

with open("E:\\Examly\\Duplicates.txt", "r+") as f:
    f.truncate()
    f.close()
for i in range(len(data['question1'])):
    ask_question(i, str(data.iloc[i]['question1']))
