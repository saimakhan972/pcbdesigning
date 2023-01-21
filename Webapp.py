
from PIL import Image
import requests 
import streamlit as st
#from streamlit_lottie import st_lottie

st.set_page_config(page_title = "My webpage" , page_icon=":tada" , layout="wide")

##def load_lottieurl(url):
   ## r = requests.get(url)
    #if r.status_code != 200:
        #return None
##return r.json()##
#--------------USE Local CSS---------------

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>" , unsafe_allow_html=True)

local_css("Designs/style.css")
#------------------Header section-----------

with st.container():
  st.subheader("Hi ,I am Kasmani Kasrim :wave:")
  st.title("An experinced PCB designer from Malaysia")
  st.write("I am passionate about PCB design with 25 years of experience , well versed with PCB schematics")
  st.write("[Learn More > ](https://www.linkedin.com)")

  #-------------LOAD Assets--------------------

  #lottie_coding =load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_tdurmal6.json")
  img_contact_form =Image.open("images/Image2.jpg")
  img_lottie_Animation =Image.open("images/Image3.jpg")
#----------------WHAT I DO---------------
  
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
        I am the PCB Designer who can server different services like Schematic Capture,PCB Layout and Libraries , 3D Modelling

        If this sounds like intresting to you please hit that contact me button!

        """
    )
        st.write("[Click here > ]{https://youtube.com)")   
#with right_column:
    #st_lottie(lottie_coding, height=300, key="coding")

#-----------Projects------------------------------

with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_Animation)

    with text_column:
        st.subheader("Intergration of lottie animation inside your site")
        st.write(
            """
            Printed circuit board (PCB) design brings your electronic circuits to life in the
            physical form. Using layout software, the PCB design process combines component placement
            and routing to define electrical connectivity on a manufactured circuit board.
            """
            )

st.markdown("[Watch video...](https://em-cad.com/)")
with st.container():
    image_column, text_column = st.columns((1,2))

with image_column:
    st.image(img_contact_form)

with text_column:
    st.subheader("My Second Project")
    st.write(
        """
            Printed circuit board (PCB) design brings your electronic circuits to life in the
            physical form. Using layout software, the PCB design process combines component placement
            and routing to define electrical connectivity on a manufactured circuit board.

        """
        )

#--------Contact Me----------------------
    with st.container():
        st.write("---")
        st.header("Get in Touch with Me")
        st.write("##")
       



    contact_form = """
    <form action="https://formsubmit.co/bushrak99517@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="False">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your Email address" required>
     <textarea name= "message"  placeholder="Your Message Here" required></textarea>
     <button type="submit">Send</button>
   </form>

 """

left_column , right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
        
