from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<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>"
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)