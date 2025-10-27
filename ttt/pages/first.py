import pandas as pd   # 导入Pandas并用pd代替
import streamlit as st

st.title("学生 小宁-数字档案")
st.header("基础信息🐕",help="这是我的基础信息")
st.subheader("2.1文本类")          
st.text("学生ID：23031310107🐕")
st.text("性别:👩")
st.image("https://cdn.pixabay.com/photo/2016/03/27/21/16/pet-1284307_960_720.jpg")
st.markdown('**:red[注册时间：2025-10-20🐕]**')
st.text("当前教室实训楼204🐕")
st.markdown('**:green[安全等级：绝密🐕]**')
st.header("👒技能举证🐕",help="c语音")
import streamlit as st  # 导入Streamlit并用st代表它

st.subheader('技能')
# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="c语言", value="0%", delta="0", delta_color="off")
c2.metric(label="python", value="60%", delta="60%")
c3.metric(label="java", value="0%", delta="0", delta_color="off")

st.subheader('Streamlit课程进度')
st.metric(label="Streamlit课程进度", value="20%", delta="10", label_visibility='hidden')


# 定义数据,以便创建数据框
data = {
    '日期':['2025-10-01','2025-10-15','2025-10-20'],
    '任务':['学生数字档案','课程管理系统','数据图表展示'],
    '状态':['完成','进行中','未完成'],
    '难度':['两颗星','一颗星','三颗星']
}

# 定义数据框所用的索引
index = pd.Series(['0', '1', '2'], name='  ')
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)

st.subheader('任务日志👒')
st.table(df)
st.header("最新代码成果")
str='''
a=50
b=50
print(a+b)
'''
st.code(str,language=None)
st.caption("这是一段python代码")
st.code(str,language="python",line_numbers=True)
'_________________________________________________'

st.markdown("#### **现状态：混乱中**")
st.markdown(':green[>>>SYSTEH MESSAGE:]下一个任务目标')
st.markdown(':green[>>>TARGET:]课程管理系统')
st.markdown(':green[>>>COUNTDOWN:]2025年10月20日11:55:54')
st.markdown("#### **连接状态：已加密**")


