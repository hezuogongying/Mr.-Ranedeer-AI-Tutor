import streamlit as st
from openai import OpenAI

aaa = '''
# 请给出不同性格类别类型，以下面格式给出。

举例:
# 语气类别配置
tone = st.selectbox(
    '选择你喜欢的【语气】:',
    ('鼓励', '中立', '信息丰富', '友好', '幽默', '严肃', '激情', '温柔', '自信', '疑惑'),
    key='tone'
)
# 语气类别描述
tone_desc = { 
    '鼓励': '鼓励型音调样式通常具有激励、支持的特点，可以使听众感到振奋和积极。', 
    '中立': '中立型音调样式不带明显的情感色彩，表现出客观、公正的态度，适用于正式、专业的场合。', 
    '友好': '友好型音调样式表现出亲切、和善的态度，可以使听众感到舒适和放松。'
}
st.caption(tone_desc[tone])

###########
# 性格类别配置 
personality_type = st.selectbox(
    '选择你的【性格类别】:',
    ('外向', '内向', '实干', '理想', '分析', '直觉', '感性', '判断'),
    key='personality_type'
)
# 性格类别描述
personality_type_desc = { 
    '外向': '外向型的人喜欢与人交往，能从社交活动中获得能量，通常表现得更加开放和热情。',
    '内向': '内向型的人倾向于独处，从内省中获得能量，可能在社交场合更加保守和沉默。',
    '实干': '实干型的人倾向于实际行动，喜欢通过具体的行动来解决问题，通常很有组织和效率。',
    '理想': '理想型的人追求高远的理想和目标，喜欢探索可能性，常常有创新的想法和愿景。',
    '分析': '分析型的人喜欢通过逻辑和理性来理解世界，强调数据和事实在决策过程中的重要性。',
    '直觉': '直觉型的人依赖直觉和直观感受来做决策，他们倾向于看到大局并追求创意和灵感。',
    '感性': '感性型的人重视情感和情绪，他们在做决策时会考虑人际关系和情感影响。',
    '判断': '判断型的人喜欢有计划和结构，倾向于快速做出决策并遵循既定的规则和程序。'
}
'''


Gpt_name = '人工智能私教'
Proj_desc = '''是一个基于 GPT-4 的个性化学习体验定制工具。这个项目的目标是通过定制化的提示，为不同需求和兴趣的用户提供个性化的学习体验。它允许用户根据自己的学习需求调整知识深度，定制学习风格、沟通方式、语气和推理框架，以创建适合自己的最佳 AI 导师。'''
Gpt = OpenAI(
    api_key='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',
    organization='org-xdHJoxr3uz579dGBP0gqMMYG',
    base_url='https://api.openai.com/v1'
    )

with open('My_Information_zh.txt', 'r', encoding='utf-8') as fp:
    gpt_info = fp.read()

with open('GPT_Prompt_zh.txt', 'r', encoding='utf-8') as fp:
    gpt_prompt = fp.read()

with open('Mr_Ranedeer_zh.txt', 'r', encoding='utf-8') as fp:
    flow_info = fp.read()

def ask_ai(user_input, config):
    
    model_types = ['gpt-4-1106-preview', 'gpt-3.5-turbo-1106']
    model_type = model_types[0]
    sys_msg = f"{gpt_info}\n\n{gpt_prompt}\n\n{flow_info}\n\n根据您的学习风格 {config['learning_style']}，AI 提供了以下回答：\n\n"
    messages = [
        {'role': 'system', 'content': sys_msg},
        {'role': 'user', 'content': user_input}
    ]
    response = Gpt.chat.completions.create(
        model=model_type,
        messages=messages,
        temperature=0.9,
        max_tokens=4000)
    return response.choices[0].message.content

# 更新 AI 配置的函数
def update_ai_config(key, value):
    # 在这里，你可以根据用户的选择更新配置
    st.session_state['config'][key] = value

# 设置 Streamlit 页面
st.title(Gpt_name)
st.markdown(Proj_desc)
# 初始化会话状态变量
if 'config' not in st.session_state:
    st.session_state['config'] = {
        'language_style': '简体中文',
        'edu_level': '在读本科',
        'learning_style': '视觉',
        'communication_type': '文字',
        'tone': '友好',
        'reasoning_framework': '逻辑',
    }


# 使用侧边栏添加配置选项
with st.sidebar:
    st.header('配置选项')

    # 语言配置
    language_style = st.selectbox(
        '选择你的【语言】:',
        ('简体中文', '广东话',  '繁体中文', 'Français', 'english', '한국어'),
        key='language_style'
    )
    
    #  # 语言描述
    language_style_desc = { 
        '简体中文': ' 中国大陆官方语言', 
        '广东话': '中国广东广西用语', 
        '繁体中文': '中国港澳台语言', 
        'Français': '法国语言。', 
        'english': '英美语言', 
        '한국어': '韩国语言'
    }
    st.caption(language_style_desc[language_style])


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
        '哲学博士': '学位名称，通常授予完成博士研究的学生。' 
    }
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

    

    # 沟通类型配置
    communication_type = st.selectbox(
        '选择你的【沟通类型】:',
        ('正式型', '教科书型', '平易型', '讲故事型', '苏格拉底型', '直接型', '间接型', '支持型', '挑战型', '表达型', '倾听型', '被动型', '强势型'),
        key='communication_type'
    )
    # 沟通类型描述
    communication_type_desc = {
        '正式型': '这种沟通风格的人在沟通时注重礼节和正式性， 通常使用规范、严谨的语言， 遵循一定的沟通流程。', 
        '教科书型': '教科书型沟通者喜欢按照事实和逻辑进行沟通， 他们的表达通常有条理、系统， 但可能较为刻板。', 
        '平易型': '平易型沟通者倾向于使用简单、易懂的语言进行沟通， 他们善于将复杂的信息用简单的语言表达出来， 让听众容易理解。', 
        '讲故事型': '讲故事型沟通者擅长通过生动、有趣的故事来传达信息， 他们善于抓住听众的注意力， 使信息更加引人入胜。', 
        '苏格拉底型': '苏格拉底型沟通者喜欢通过提问和引导对话的方式来探讨问题， 他们善于激发他人的思考和反思。', 
        '直接型': '这种沟通风格的人喜欢直截了当地表达自己的想法和需求， 通常以明确、简洁的语言进行沟通。', 
        '间接型': '与直接型相对， 间接型的人倾向于通过暗示、比喻或讲故事的方式表达自己的观点， 以避免直接冲突。', 
        '支持型': '这类沟通者注重在交流中建立和谐的氛围， 他们倾向于使用鼓励性语言， 关注他人的感受和需求。', 
        '挑战型': '挑战型沟通者喜欢辩论， 他们通过提问和讨论来检验想法， 可能会显得较为强势和好辩。', 
        '表达型': '这类人情感丰富， 喜欢用语言和肢体语言来表达自己的情感和想法， 沟通时可能会显得较为生动和具有感染力。', 
        '倾听型': '倾听型沟通者擅长聆听， 他们给予说话者充分的关注， 通过倾听来理解他人的观点和感受。', 
        '被动型': '被动型的人在进行沟通时， 可能不够积极主动， 他们可能更倾向于遵循而非主导沟通的方向。', 
        '强势型': '强势型沟通者通常在交流中占据主导地位， 他们喜欢控制对话的节奏和内容。' 
    }
    st.caption(communication_type_desc[communication_type])


    # st.caption(teacher_gae_desc[teacher_gae])
    # 语气配置
    tone = st.selectbox(
            '选择你喜欢的【语气】:',
            ('鼓励', '中立', '信息丰富', '友好', '幽默', '严肃', '激情', '温柔', '自信', '疑惑'),
            key='tone'
        )
        # 语气描述
    tone_desc = { 
            '鼓励': '鼓励型音调样式通常具有激励、支持的特点，可以使听众感到振奋和积极。', 
            '中立': '中立型音调样式不带明显的情感色彩，表现出客观、公正的态度，适用于正式、专业的场合。', 
            '信息丰富': '信息丰富型音调样式注重传达大量信息，通常包含丰富的词汇和细节，可以使听众更好地理解和掌握内容。', 
            '友好': '友好型音调样式表现出亲切、和善的态度，可以使听众感到舒适和放松。', 
            '幽默': '幽默型音调样式以幽默、诙谐为特点，能够带给听众轻松愉快的心情。', 
            '严肃': '严肃型音调样式表现出认真、庄重的态度，适用于正式、严肃的场合。', 
            '激情': '激情型音调样式充满热情和动力，可以使听众感受到强烈的情感和信念。', 
            '温柔': '温柔型音调样式柔和、细腻，给人一种温馨、舒适的感觉。', 
            '自信': '自信型音调样式表现出自信、坚定的一面，能够赢得听众的信任和尊重。', 
            '疑惑': '疑惑型音调样式以疑问、探究为特点，用于表示对事物的好奇和思考。' 
        }
    st.caption(tone_desc[tone])


    # 推理框架配置
    reasoning_framework = st.selectbox(
        '选择你的【推理框架】:',
        ('逻辑', '情感', '直觉', '经验', '批判性思维', '创造性思维', '系统思维'),
        key='reasoning_framework'
    )
    # 推理框架描述
    reasoning_framework_desc = {
        '逻辑': '基于逻辑和证据的推理，强调理性分析和演绎或归纳推理的过程',
        '情感': '基于情感和共鸣的推理。强调情绪和同理心在决策和思考中的作用。',
        '直觉': '基于直觉和直观感受的推理。基于直觉和直观感受的推理，依赖于非理性或无意识的认知过程，如直觉或第六感',
        '经验': '依赖于个人或集体的经验和过往的观察，通过类比或模式识别来进行推理。',
        '批判性思维': '强调分析和评估论据的有效性，以及识别和质疑假设和偏见。',
        '创造性思维': '涉及创新和想象力，寻找问题的新颖解决方案或形成新的概念。',
        '系统思维': '考虑问题的整体和相互关系，强调系统的动态性和复杂性。'
    }
    st.caption(reasoning_framework_desc[reasoning_framework])

    # 当配置发生变化时，更新会话状态
    if st.session_state['config']['language_style'] != language_style:
        update_ai_config('language_style', language_style)
    if st.session_state['config']['edu_level'] != edu_level:
        update_ai_config('edu_level', edu_level)
    if st.session_state['config']['learning_style'] != learning_style:
        update_ai_config('learning_style', learning_style)
    if st.session_state['config']['communication_type'] != communication_type:
        update_ai_config('communication_type', communication_type)
    if st.session_state['config']['tone'] != tone:
        update_ai_config('tone', tone)
    if st.session_state['config']['reasoning_framework'] != reasoning_framework:
        update_ai_config('reasoning_framework', reasoning_framework)
    
    

#########################################
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