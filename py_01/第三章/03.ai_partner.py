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
st.title("AI智能伴侣")


# 创建会话标识
def create_identification():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#保存会话方法
def save_session():
    if st.session_state.identification and st.session_state.messages:
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


#加载会话文件
def load_session():
    conversation_list = []
    if os.path.exists("sessions"):
        files = os.listdir("sessions")
        for file in files:
            if file.endswith(".json"):
                conversation_list.append(file[:-5])
    conversation_list.sort(reverse=True)
    return conversation_list

#加载当前会话
def load_session_current(conversation):
    #判断是否有这个会话文件
    try:
        if os.path.exists(f"sessions/{conversation}.json"):
            with open(f"sessions/{conversation}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.identification = conversation
                st.session_state.messages = session_data["messages"]
                st.session_state.ai_name = session_data["ai_name"]
                st.session_state.ai_character = session_data["ai_character"]
    except Exception:
        st.error("会话文件不存在")

#删除当前会话
def dele_session_current(conversation):
    try:
        if os.path.exists(f"sessions/{conversation}.json"):
            os.remove(f"sessions/{conversation}.json")
            if conversation == st.session_state.identification:
                st.session_state.identification = create_identification()
                st.session_state.messages = []
    except Exception:
        st.error("会话文件删除失败")


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
    st.session_state.identification = create_identification()


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
#展示当前会话名称
st.text(st.session_state.identification)
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
        # 2.新建会话
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.identification = create_identification()
            save_session()
            #重新渲染页面
            st.rerun()

    st.text("历史会话")
    for conversation in load_session():
        col1, col2 = st.columns([4,1])
        with col1:
            #使用三元运算符使选中的按钮更显眼
           if st.button(conversation, width="stretch", icon="🗒️", key=f"load_{conversation}", type="primary" if conversation == st.session_state.identification else "secondary"):
                #加载会话
                load_session_current(conversation)
                # 重新渲染页面
                st.rerun()
        with col2:
           if st.button("", width="stretch", icon="❌", key=f"delete_{conversation}"):
               #删除会话
               dele_session_current(conversation)
               # 重新渲染页面
               st.rerun()

     #分割线
    st.markdown("___")
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
    # 保存会话数据
    save_session()
    st.rerun()



