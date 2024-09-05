pip install langchain requests
%pip install --upgrade --quiet  langchain-google-genai pillow
pip install langchain_community
from langchain_google_genai import ChatGoogleGenerativeAI
import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI


# Make sure you replace 'YOUR_ACTUAL_API_KEY' with your real API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyB0G7lWzLbVILOLj4FFAKUrYLBk2mRiwn4"

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")
for i in range(100):
 input_1=input()
 result = llm.invoke(input_1)
 print(result.content)
 i=i+1
 if input_1=='quit':
  break