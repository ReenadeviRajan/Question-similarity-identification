# Question Similarity Identification
  The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing (NLP) for English written in the Python programming language.NLTK is intended to support research and teaching in NLP or closely related areas, including empirical linguistics, cognitive science, artificial intelligence, information retrieval, and machine learning. NLTK has been used successfully as a teaching tool, as an individual study tool, and as a platform for prototyping and building research systems.NLTK supports classification, tokenization, stemming, tagging, parsing, and semantic reasoning functionalities.To find the duplication of questions in a given series of data. To find the duplication NLTK Toolkit is used to classify the text. NLTK is a leading platform for building Python programs to work with language data.
# Getting Started
   1. Create a new project in the pycharm. 
   2. Install the pandas,numpy,tkinter,nltk,tessecret libraries. 
   3. For input data crawl websites to scrape html strings. The scraped html string stored as train.csv.
*Read the training dataset. The training dataset contains questions.
*In train() it is used to remove the null values in the training dataset. 
*In the Lemmatization process it groups together the different inflected forms of a word so they can be analysed as a single item. Lemmatization is similar to stimming but it brings context to the words. So it links words with similar meaning to one word.
*In my_tokenizer() it removes the stopwords,finds out the part of speech using pos-tag and returns the list of words. 
*In ask_question() the TfidfVectorizer will tokenize documents, learn the vocabulary and inverse document frequency weightings, and allow you to encode new documents. Fit.transform() is used to learn vocabulary and inverse document frequency, return document-term matrix. Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. After that similar questions are appended into the document with similarity.
*The input text ask_question function will execute.
*The input is an image. It extracts the text from the image and executes the ask_question function.
*When the Latex input is given to convert into the sympy form. Then find out the similarity.
*The output file is stored as text named Duplicate. It contains the Input Question, Similar Question with similarity percentage.
### Prerequestics
  * Python IDE-Pycharm
  * NLTK Data library
  * Tesseract Library
### Installing
Installing the pycharm IDE for running the program.
  ```
  https://www.jetbrains.com/pycharm/download/ 
  ```
Installing the numpy library in pycharm IDE.
  ```
  pip install numpy
  ```
Installing the pandas library.Pandas library is used for cleaning and preprocessing the data. It is used to remove the null value.
```
pip install pandas
```
Installing the nltk library. NLTK library is used for text classification.
```
pip install nltk
```
Next download the nltk library using nltk.download() command.
These commands are running into the terminal.
Installing the tesseract software. This software is used to extract the text from the image. After the installation of tesseract software tessecret library is used to extract the data.
Installing the tkinter.Tkinter is used for developing the api in python.
```
pip install tkinter 
```
This command is used to install the tkinter. 
+Scikit-learn is a free machine learning library for Python. It features various algorithms like support vector machines, random forests, and k-neighbours, and it also supports Python numerical and scientific libraries like NumPy and SciPy .
```
pip install scikit-learn
```





