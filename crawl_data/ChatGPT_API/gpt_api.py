import os
import openai
import time

# openai.api_key = "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"  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
# openai.api_key = "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" 
openai.api_key ="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"

data = open("./crawler_facebook_comment/input_test.csv",encoding="utf-8").read().splitlines()  # read input file

prompt = """Phân loại cảm xúc cho câu sau, theo 4 nhãn: [happiness],[sadness],[anger] và [fear]:"""

for item in data:
    prompt += f"\n- {item}"

print(f"Final promt is: \n" + prompt)


def openai_create(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["Human:", " AI:"]
    )

    return response.choices[0].text


a = time.time()
ans = openai_create(prompt)
b = time.time()
print(f"Request time: {b - a}")  # print request time
print()
print(prompt + ans)
