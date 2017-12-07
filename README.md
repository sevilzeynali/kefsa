# kefsa : KeyWords Extraction For Scientific Articles

kefsa is a program in Python for extract keywords from scientific articles in txt format. It uses Python [textacy](https://pypi.python.org/pypi/textacy) library.

## Installing and requirements

You need Python >= 2.6 or >= 3.3

You must install textacy and spacy for using tefsa :

```

$ pip install textacy
$ sudo pip install -U spacy

```

## How to use

The input folder should contanins scientific articles in txt format.

In output folder you can see the keywords and their tfidf for each article in a separated txt file.