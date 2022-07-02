import streamlit as st
from PIL import Image
import notion
import json
import requests
import urllib3

image = Image.open('image.png')
col1, col2= st.columns(2)


col1.title("Pink Data Hub")
col1.subheader("Our Enquiry Form")
col1.write("Please fill out the following correctly, \n \n We will get in "
           "touch with you shortly. \n \n "
           "We are excited to work with you and help your buiness grow!!!")
col2.image(image)

#ce5f6dabbeb847dcb957552e018f071b?v=9c5f96831d7e4464aa25d64cacc5ece3
secret = "secret_s74bWlSgDpHkb14TmLr46LX7bGO7NLt5yYvh3NbcGjP"
database = "ce5f6dabbeb847dcb957552e018f071b"
url = f"https://api.notion.com/v1/databases/ce5f6dabbeb847dcb957552e018f071b"


form = st.form("forms", clear_on_submit=False)
username = form.text_input("Business Name")
contact = form.text_input("Business Phone Number")
email = form.text_input("Business Email Address")
choice = form.multiselect("Business Requirements",["Notion Templates", "Web Applications", "API",
                                                     "Strategic Business Growth","Business Automations"])
submit = form.form_submit_button('Submit')
if submit:
    st.success("Submitted Successfully")
    form1 = ("Name":username , "Phone":contact , "Email":email, "Business":choice)
    form_app = json.dumps(form1, indent=4)
    
    headers = {
      "Authorization": f"Bearer {secret}",
      "Accept": "application/json",
      "Notion-Version": "2022-06-28",
      "Content-Type": "application/json"
    }
    res = requests.patch(url, headers=headers, json=form_app)
    data = res.json()
    st.write(res.status_code)
    st.json(data)

    #  response = requests.patch(url, headers=headers, json=form)
    #st.write(response.text)
