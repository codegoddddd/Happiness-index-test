from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re
print("What are you feeling now just express your thoughts : ")
a=input()
tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

tokens = tokenizer.encode(a, return_tensors='pt')

result = model(tokens)

result.logits

c=int(torch.argmax(result.logits))+1

if(c<=2):
    print("According to data entered you are FEELING LOW and you are quite sad")
elif(c>=4):
    print("You are having a good day and your mood is AWESOME !!")
else:
    print("You are absolutely NORMAL !!")