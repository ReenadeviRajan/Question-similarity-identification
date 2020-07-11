# Question Similarity Identification
  NLTK is a powerful Python package that provides a set of diverse natural language algorithms. It is free, opensource, easy to use, large community, and well documented. Tokenizing and part of speech tagging algorithms are used to find the duplication of questions in a given series of data. The process of breaking down a text paragraph into smaller chunks such as words or sentences is called Tokenization. Token is a single entity that is building blocks for sentences or paragraphs. The process of classifying words into their parts of speech and labeling them accordingly is known as part-of-speech tagging.A part-of-speech tagger processes a sequence of words, and attaches a part of speech tag to each word.
# Getting Started
   1. Create a new project in the pycharm. 
   2. Install the pandas,numpy,tkinter,nltk,tessecret libraries. 
   3. For input data crawl websites to scrape html strings. The scraped html string stored as train.csv.The input is an image,it extracts the text from the image and stored to the input data.The Latex input is occured it converts the latex form to sympy and stored to the input data.
   4. Read the training dataset. The training dataset contains questions.
   5. In train() it is used to remove the null values in the training dataset. 
   6. In the Lemmatization process it groups together the different inflected forms of a word so they can be analysed as a single item. 
   7. In my_tokenizer() it removes the stopwords,finds out the part of speech using pos-tag and returns the list of words. 
   8. In ask_question() the TfidfVectorizer will tokenize documents, learn the vocabulary and inverse document frequency weightings, and allow you to encode new documents. Fit.transform() is used to learn vocabulary and inverse document frequency, return document-term matrix. Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. After that similar questions are appended into the document with similarity.
   9. The output text file is stored as Duplicate.txt. It contains the Input Question, Similar Question with similarity percentage.

  
