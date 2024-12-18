text = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

def lowercase(text):
    return text.lower()

def removePunctuation(text):
    punctuations = ['.', '-', ',', '*']
    for punctuation in punctuations:
        text = text.replace(punctuation, '')
    return text

def removeNewlines(text):
    text = text.replace('\n', ' ')
    return text

def removeShortWords(text):
    return ' '.join([word for word in text.split() if len(word) > 3])

def removeLongWords(text):
    return ' '.join([word for word in text.split() if len(word) < 6])

processingFunctions = [lowercase, removePunctuation, removeNewlines]
for func in processingFunctions:
	text = func(text)
print(text)
