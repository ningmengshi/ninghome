import streamlit as st

st.set_page_config(page_title="动物园",page_icon="🐕")

images=[
 {
       'url':'https://wallpapercat.com/w/full/6/5/4/24272-1920x1440-desktop-hd-dog-wallpaper.jpg',
       'parm':'狗'
       },
 {
       'url':'https://cdn.pixabay.com/photo/2020/03/31/19/27/dog-4989019__340.jpg',
       'parm':'狗'
       },
  {
       'url':'https://www.wallpaperbetter.com/wallpaper/524/805/269/cute-puppy-dog-pet-face-hand-1080P-wallpaper.jpg',
       'parm':'狗'
       },
  {
       'url':'https://pic.baike.soso.com/p/20090105/20090105120000-108352.jpg',
       'parm':'狗'
       },
  {
       'url':'https://png.pngtree.com/background/20230519/original/pngtree-puppies-pomeranians-picture-image_2655558.jpg',
       'parm':'狗'
       }
 ]
if 'ind' not in st.session_state:
    st.session_state['ind']=0

#define:定义
def nextImg():
    global ind
    st.session_state['ind']=(st.session_state['ind']+1)%len(images)
def lastImg():
    st.session_state['ind']=(st.session_state['ind']-1)%len(images)   
st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['parm'])
col1,col2=st.columns(2)
with col1:
   st.button('上一张',on_click=lastImg,use_container_width=True)
with col2:
   st.button('下一张',on_click=nextImg) 
