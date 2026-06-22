import streamlit as st
import os
from openai import OpenAI
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="👽",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)
st.logo("./resource/logo.png")
st.title("AI智能伴侣")
# print("-------重新开始对话")
role = "你的名字叫飞姐，请用高冷御姐类型回答问题"
#创建与AI大模型交互的客户端对象
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")
#初始化会话状态
if "messages" not in st.session_state:
    st.session_state.messages = []
#展示ai与用户会话状态存储
for message in st.session_state.messages:
    print(message,"-------会话状态")
    st.chat_message(message["role"]).write(message["content"])


prompt = st.chat_input('请输入您要问得问题')

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    # print(prompt,"-------用户输入")
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": role},
            #解决会话记忆问题
            *st.session_state.messages,
        ],
        #切换成流式输出
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    # print(response.choices[0].message.content)
    # 用生成器提取每个chunk的文本内容
    response_gen = (chunk.choices[0].delta.content for chunk in response if chunk.choices[0].delta.content is not None)
    # 在同一个聊天气泡中流式写入，write_stream会返回完整拼接后的文本
    with st.chat_message("ai"):
        full_response = st.write_stream(response_gen)
    # 循环结束后一次性存入会话状态
    st.session_state.messages.append({"role": "assistant", "content": full_response})




