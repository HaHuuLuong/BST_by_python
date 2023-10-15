

prompt = """Phân loại cảm xúc cho câu sau, theo 3 nhãn: [NEGATIVE],[POSITIVE] và [NEUTRAL]:"""

for item in data:
    prompt += f"\n- {item}"

print(f"Final promt is: \n" + prompt)


def openai_create(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=3500,