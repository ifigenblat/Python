'''
Language Model
A probability distribution over a sequence of words - takes a context and predict the next word in the sequence 
Example:
sending query "Shaping tomorrow" would return the next word "with"
then will concatenate the predicted word and send again "Shaping tomorrow with" return "AI"
concatenate the predicted word and send again "Shaping tomorrow with AI" return "application"
concatenate the predicted word and send again "Shaping tomorrow with AI application" return "<endoftext>"
endoftext is a token that denotes the conclusion of text generation.

Tokenization - splitting and mapping text into numbers for a machine to understand.
OpenAI uses Byte-Pair encoding to tokenize texts into sub-word pieces. 

https://platform.openai.com/tokenizer - to see token in action
Tokenization Summary:
* OpenAI charges by tokens
* Rule of thumb: budget for roughly 30% more tokens than words.
* Use 'tiktocken' package to get accurate token count

Large language model
large language model is defined by:
* Parameter count: 1+ billion
* Data size: Billions of tokens
