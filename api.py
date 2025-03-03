from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
