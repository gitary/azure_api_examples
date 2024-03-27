#Note: The openai-python library support for Azure OpenAI is in preview.
  #Note: This code sample requires OpenAI Python library version 1.0.0 or higher.
import os
from openai import AzureOpenAI

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = AzureOpenAI(
 azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
 api_key=os.getenv("AZURE_OPENAI_KEY"),  
 api_version="2024-02-15-preview"
)
#print(os.getenv("AZURE_OPENAI_ENDPOINT"))
#print(os.getenv("AZURE_OPENAI_KEY"))
message_text = [{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":"Qual è il primo uomo ad essere andato sulla luna?"}]#,{"role":"assistant","content":"Il primo uomo ad essere andato sulla luna è stato Neil Armstrong, il 20 luglio 1969, durante la missione Apollo 11."}]
completion = client.chat.completions.create(
 model="gpt-35-turbo", # model = "deployment_name"
 messages = message_text,
 temperature=0.7,
 max_tokens=800,
 top_p=0.95,
 frequency_penalty=0,
 presence_penalty=0,
 stop=None
)

print(completion.choices[0].message.content)