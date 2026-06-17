# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system","content": "你的名字叫小飞飞，请用高冷御姐类型语气回答问题"},
        {"role": "user", "content": "你是谁，请做一个全面的自我介绍"},
    ],
    stream=True,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

# 方式1: 流式输出 (stream=True)
for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()  # 换行

# 方式2: 非流式输出 (stream=False)
# response = client.chat.completions.create(
#     model="deepseek-v4-pro",
#     messages=[
#         {"role": "system","content": "你的名字叫小飞飞，请用高冷御姐类型语气回答问题"},
#         {"role": "user", "content": "你是谁，请做一个全面的自我介绍"},
#     ],
#     stream=False,
#     reasoning_effort="high",
#     extra_body={"thinking": {"type": "enabled"}}
# )
# print(response.choices[0].message.content)