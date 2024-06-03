from openai import OpenAI

api_key = "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"
client = OpenAI(api_key=api_key)

user_input = input("chat ab anything to test SmartKit's capabilities")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a chatbot who specializes in vegan food."},        # six years vegan as of
    # 2024 LFG
    {"role": "user", "content": user_input}
  ]
)

print(completion.choices[0].message)