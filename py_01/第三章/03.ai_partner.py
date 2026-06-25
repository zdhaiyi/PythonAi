import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="👽",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)
st.logo("./resource/logo.png")
st.title("AI控制面板")

#保存会话方法
def save_session():
    #判断当前会话是否有内容
    # if not st.session_state.messages:
    #     return
    if st.session_state.identification:
        # 构建会话对象
        session_data = {
            "identification": st.session_state.identification,  # 创建时间
            "messages": st.session_state.messages,  # 会话内容
            "ai_name": st.session_state.ai_name,  # 伴侣名字
            "ai_character": st.session_state.ai_character  # 伴侣性格
        }
        # 判断是否有创建保存会话目录sessions
        if not os.path.exists("sessions"):
            os.makedirs("sessions")

        with open(f"sessions/{st.session_state.identification}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)


#创建与AI大模型交互的客户端对象
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")
#初始化会话状态
if "messages" not in st.session_state:
    st.session_state.messages = []

#存储用户修改的ai名字和性格
if "ai_name" not in st.session_state:
    st.session_state.ai_name = "小甜甜"
if "ai_character" not in st.session_state:
    st.session_state.ai_character = "活泼开朗的东北姑娘"

#会话标识
if "identification" not in st.session_state:
    st.session_state.identification = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


system_propot =  f"""
        你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。：
        规则：
            1. 每次只回1条消息
            2. 禁止任何场景或状态描述性文字
            3. 匹配用户的语言
            4. 回复简短，像微信聊天一样
            5. 有需要的话可以用❤️🌸等emoji表情
            6. 用符合伴侣性格的方式对话
            7. 回复的内容, 要充分体现伴侣的性格特征
        伴侣性格：
            - %s
        你必须严格遵守上述规则来回复用户。
    """

#展示ai与用户会话状态存储
for message in st.session_state.messages:
    print(message,"-------会话状态")
    st.chat_message(message["role"]).write(message["content"])


#左侧侧边栏
with st.sidebar:
    #会话数据存储
    st.subheader("AI控制面板")
    if st.button("创建会话",width="stretch",icon="🚀"):
        # 1.保存当前会话数据
        save_session()
        # 2.创建会话



    #伴侣信息
    st.subheader("伴侣信息")
    st.text_input("名字",placeholder = "请输入伴侣名字",key="ai_name")
    st.text_area("性格",placeholder = "请输入伴侣性格",key="ai_character")






prompt = st.chat_input('请输入您要问得问题')

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    # print(prompt,"-------用户输入")
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_propot % (st.session_state.ai_name, st.session_state.ai_character)},
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




