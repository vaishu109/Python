from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)