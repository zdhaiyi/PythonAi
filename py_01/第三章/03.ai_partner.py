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

role = "你的名字叫飞姐，请用高冷御姐类型回答问题"
prompt = st.chat_input('请输入您要问得问题')

if prompt:
    st.chat_message("user").write(prompt)
    client = OpenAI(
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    st.chat_message("ai").write(response.choices[0].message.content)


