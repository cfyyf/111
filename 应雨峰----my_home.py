'''我的主页'''
import streamlit as st
from PIL import Image
import pandas as pd
import time

#roading = st.progress(0, '开始加载')
#for i in range(1, 101, 1):
#    time.sleep(0.02)
#    roading.progress(i, '正在加载'+str(i)+'%   请耐心等待')
#roading.progress(100, '加载完毕！')

msg1 = '将要被打印的信息'
msg2 = ':orange[将要被打印的信息]'
msg3 = ':orange[感谢支持  Thanks♪(･ω･)ﾉ................................mc(小彩蛋)]'

d = {
      '姓名':['阿短', '编程猫', '同学A'],
      '学号':[1, 2, 3]
}
d = pd.DataFrame(d)

number = 12345

#st.write(msg1)
#st.write(msg2)
#st.write(d)
#st.write(number)
st.write(msg3)

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区', '留言'])

def page_1():
    '''我的兴趣推荐'''
    with open('霞光.mp3', 'rb') as f:
        mymap3 = f.read()
    st.audio(mymap3, format = 'audio/mp3', start_time = 0)
    st.image('slogan.png')
    tab1,tab2,tab3,tab4= st.tabs(['电影推荐','游戏推荐','书籍推荐','习题集推荐'])
    with tab1:
        st.write(':blue[我的电影推荐]')
        st.write('--------《飞驰人生》,《野性的呼唤》---------')
    with tab2:
        st.write(':blue[我的游戏推荐]')
        st.write('-------MC(我的世界),皇室战争------')
    with tab3:
        st.write(':blue[我的书籍推荐]')
        st.write('--------《流浪的地球》---------')
    with tab4:
        st.write(':blue[我的习题集推荐]')
        st.write('--------《新课堂》---------')

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type = ['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        #st.image(img)
        #st.image(img_change(img, 0, 2, 1))
        tab1,tab2,tab3,tab4= st.tabs(['原色','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
    st.write(":sunglasses:图片大小变化小程序:sunglasses:")
    uploaded_file1 = st.file_uploader("上传图片1", type = ['png', 'jpeg', 'jpg'])
    if uploaded_file1:
        # 获取图片文件的名称、类型和大小
        file_name1 = uploaded_file1.name
        file_type1 = uploaded_file1.type
        file_size1 = uploaded_file1.size
        img = Image.open(uploaded_file1)
        tb1,tb2,tb3,tb4= st.tabs(["(250,250)", "(500,500)", "(750,750)", "(1000,1000)"])
        with tb1:
            st.image(img)
        with tb2:
            st.image(img)
        with tb3:
            st.image(img)
        with tb4:
            st.image(img)

def page_3():
    '''我的智能词典'''
    st.write(':blue[智能词典]')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        if word == 'python':
            st.code('''
                # 恭喜你触发彩蛋，这是一行python代码
                print('hello world')''')
        if word == 'snow':
            st.snow()
            st.code('''
                # 恭喜你触发彩蛋''')
        if word == 'birthday':
            st.balloons()
            st.code('''
                # 恭喜你触发彩蛋''')
        if word == 'strawberry':
            st.write(":blue[你咋知道我喜欢吃草莓?嘿嘿]")
            st.code('''
                # 恭喜你触发彩蛋''')
        if word == 'china':
            st.write(":blue[你搜这个干嘛？我只知道你爱中国，isn't it?]")
            st.image('111.jpg')
            st.code('''
                # 恭喜你触发彩蛋''')
        

def page_4():
    '''我的留言区'''
    st.write(':blue[留言区]')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    name = st.selectbox('我是……', ['阿短', '编程猫','作者', '路人'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '作者':
            with st.chat_message('y'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
        elif i[1] == '路人':
            with st.chat_message('无'):
                st.write(i[1],':',i[2])

def page_5():
    '''留言'''
    st.balloons()
    st.write(':blue[作者的留言]')
    st.write("没啥好看的，嘻嘻(#^.^#)    我是......cf文墨؏؏☝ᖗ乛◡乛ᖘ☝؏؏!")

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

if page == '我的兴趣推荐':
    st.balloons()
    page_1()
elif page == '我的图片处理工具':
    st.snow()
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    st.snow()
    page_4()
elif page == '留言':
    page_5()