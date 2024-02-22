import streamlit as st
from openai import OpenAI


Gpt = OpenAI(
    api_key='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',
    organization='org-xdHJoxr3uz579dGBP0gqMMYG',
    base_url='https://api.openai.com/v1'
    )

def ask_ai(user_input, config):
    # 在这里，你将根据用户的配置来调整 AI 的行为
    # 例如，你可以修改 prompt，或者调用不同的 AI 模型
    # 这里只是一个示例输出，你需要根据你的 AI 模型来实现具体逻辑
    model_types = ['gpt-4-1106-preivew', 'gpt-3.5-turbo-1106']
    model_type = model_types[0]
    sys_msg = f"根据您的学习风格 {config['learning_style']}，AI 提供了以下回答：\n{user_input}"
    messages = [
        {'role': 'system', 'content': sys_msg},
        {'role': 'user', 'content': user_input}
    ]
    response = Gpt.chat.completions.create(
        model=model_type,
        messages=messages,
        temperature=0.9,
        max_tokens=200)
    return response.choices[0].message.content

# 更新 AI 配置的函数
def update_ai_config(key, value):
    # 在这里，你可以根据用户的选择更新配置
    st.session_state['config'][key] = value

# 设置 Streamlit 页面
st.title('智能导师')

# 初始化会话状态变量
if 'config' not in st.session_state:
    st.session_state['config'] = {
        'edu_level': '在读本科',
        'learning_style': '视觉',
        'communication_type': '文字',
        'tone': '友好',
        'reasoning_framework': '逻辑'
    }





# 使用侧边栏添加配置选项
with st.sidebar:
    st.header('配置选项')
    # 学历水平配置
    edu_level = st.selectbox(
        '选择你的【学历】:',
        ('小学', '初中', '高中', '在读本科', '学士', '硕士', '在读博士', '博士后', '哲学博士'),
        key='edu_level'
    )
     # 学习风格描述
    edu_level_desc = { 
        '小学': '指代小学阶段教育。', 
        '初中': '指代初中阶段教育。', 
        '高中': '指代高中阶段教育。', 
        '在读本科': '指代本科阶段教育。', 
        '学士': '学位名称，通常授予完成本科学习的学生。', 
        '硕士': '学位名称，通常授予完成研究生学习的学生。', 
        '在读博士': '指代正在攻读博士学位的学生。', 
        '博士后': '指代获得博士学位后，进行博士后研究的学生。', 
        '哲学博士': '学位名称，通常授予完成博士研究的学生。' }
    st.caption(edu_level_desc[edu_level])

    # 学习风格配置
    learning_style = st.selectbox(
        '选择你的【学习风格】:',
        ('视觉', '文字', '主动', '直觉', '反思', '全局'),
        key='learning_style'
    )
     # 学习风格描述
    learning_style_desc = { 
        '视觉': '喜欢视觉材料如图表和图像。', 
        '文字': '喜欢文字材料如书籍和文章。', 
        '主动': '喜欢通过实践和动手操作学习。', 
        '直觉': '喜欢直觉思考，善于发现规律和模式。', 
        '反思': '喜欢通过反思和总结来加深理解。', 
        '全局': '喜欢从整体和全局的角度去分析和解决问题。'
    }
    st.caption(learning_style_desc[learning_style])

    # 通信类型配置
    communication_type = st.selectbox(
        '选择你的【沟通类型】:',
        ('正式型', '教科书型', '平易型', '讲故事型', '苏格拉底型', '直接型', '间接型', '支持型', '挑战型', '表达型', '倾听型', '被动型', '强势型'),
        key='communication_type'
    )
    # 通信类型描述
    communication_type_desc = 
{ '正式型': '这种沟通风格的人在沟通时注重礼节和正式性， 通常使用规范、严谨的语言， 遵循一定的沟通流程。', '教科书型': '教科书型沟通者喜欢按照事实和逻辑进行沟通， 他们的表达通常有条理、系统， 但可能较为刻板。', '平易型': '平易型沟通者倾向于使用简单、易懂的语言进行沟通， 他们善于将复杂的信息用简单的语言表达出来， 让听众容易理解。', '讲故事型': '讲故事型沟通者擅长通过生动、有趣的故事来传达信息， 他们善于抓住听众的注意力， 使信息更加引人入胜。', '苏格拉底型': '苏格拉底型沟通者喜欢通过提问和引导对话的方式来探讨问题， 他们善于激发他人的思考和反思。', '直接型': '这种沟通风格的人喜欢直截了当地表达自己的想法和需求， 通常以明确、简洁的语言进行沟通。', '间接型': '与直接型相对， 间接型的人倾向于通过暗示、比喻或讲故事的方式表达自己的观点， 以避免直接冲突。', '支持型': '这类沟通者注重在交流中建立和谐的氛围， 他们倾向于使用鼓励性语言， 关注他人的感受和需求。', '挑战型': '挑战型沟通者喜欢辩论， 他们通过提问和讨论来检验想法， 可能会显得较为强势和好辩。', '表达型': '这类人情感丰富， 喜欢用语言和肢体语言来表达自己的情感和想法， 沟通时可能会显得较为生动和具有感染力。', '倾听型': '倾听型沟通者擅长聆听， 他们给予说话者充分的关注， 通过倾听来理解他人的观点和感受。', '被动型': '被动型的人在进行沟通时， 可能不够积极主动， 他们可能更倾向于遵循而非主导沟通的方向。', '强势型': '强势型沟通者通常在交流中占据主导地位， 他们喜欢控制对话的节奏和内容。' }
    st.caption(communication_type_desc[communication_type])


    # 语气配置
    tone = st.selectbox(
        '选择你喜欢的【语气】:',
        ('友好', '正式', '幽默'),
        key='tone'
    )
    # 语气描述
    tone_desc = {
        '友好': '轻松友好的交流方式。',
        '正式': '严肃正式的交流方式。',
        '幽默': '幽默风趣的交流方式。'
    }
    st.caption(tone_desc[tone])


    # 推理框架配置
    reasoning_framework = st.selectbox(
        '选择你的【推理框架】:',
        ('逻辑', '情感', '直觉'),
        key='reasoning_framework'
    )
    # 推理框架描述
    reasoning_framework_desc = {
        '逻辑': '基于逻辑和证据的推理。',
        '情感': '基于情感和共鸣的推理。',
        '直觉': '基于直觉和直观感受的推理。'
    }
    st.caption(reasoning_framework_desc[reasoning_framework])

    # 当配置发生变化时，更新会话状态
    if st.session_state['config']['learning_style'] != learning_style:
        update_ai_config('learning_style', learning_style)
    if st.session_state['config']['communication_type'] != communication_type:
        update_ai_config('communication_type', communication_type)
    if st.session_state['config']['tone'] != tone:
        update_ai_config('tone', tone)
    if st.session_state['config']['reasoning_framework'] != reasoning_framework:
        update_ai_config('reasoning_framework', reasoning_framework)


# 创建一个文本区域，用户可以在其中输入他们的问题或命令
user_input = st.text_area("请输入你的问题或命令:", height=150)

# 创建一个发送按钮
if st.button('发送'):
    # 调用 AI 函数，传入用户输入和当前配置
    ai_response = ask_ai(user_input, st.session_state['config'])
    
    # 显示 AI 的响应
    st.text(ai_response)

# 显示可用指令的提示
st.markdown("""
    **为了提供更好的学习体验，只需使用以下指令即可实现:**
    - **`/test`**: 测试你的知识和理解。
    - **`/config`**: 更新你的 AI 导师配置/偏好。
    - **`/plan`**: 根据你的偏好创建一个课程计划。
    - **`/start`**: 开始课程计划。
    - **`/continue`**: 如果输出被截断，继续输出。
    - **`/language`**: 更改 AI 导师的语言。
    """, unsafe_allow_html=True)
# 当用户输入并提交后，调用 AI 函数并显示响应
if user_input:
    # 调用 AI 函数，传入用户输入和当前配置
    ai_response = ask_ai(user_input, st.session_state['config'])
    
    # 显示 AI 的响应
    st.text(ai_response)