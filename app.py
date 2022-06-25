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

secret = "secret_J7BGrdtw6ujyteeZKQEDD24Dl0TO8Lx6tglACwZ0w7J"
database = "1c57c0768500436ab8986aeadfc84736"
url = f"https://spangle-basin-670.notion.site/Form-Submission-1c57c0768500436ab8986aeadfc84736"

headers = {
    'Authorization': f"Bearer {secret}",
    'Content-Type': 'application/json',
    'Notion-Version': '2022-04-12'

}

with st.form(key='enquiry_form'):
    username = st.text_input("Business Name")
    contact = st.text_input("Business Phone Number")
    email = st.text_input("Business Email Address")
    choice = st.multiselect("Business Requirements",["Notion Templates", "Web Applications", "API",
                                                     "Strategic Business Growth","Business Automations"])

    submit = st.form_submit_button('Submit')
    if submit:
        st.success("Submitted Successfully")
        #file = open('secret.json')

        #data = json.load(file)
        data = {
            "parent": { "database_id": f"{database}" },
            "Properties" : {
                "Business_Name": [
                    {
                        "text": {
                            "content": "username"
                        }
                    }
                ],
                "Phone_Number": [
                    {
                        "Phone": {
                            "content": "contact"
                        }
                    }
                ],
                "Email_Address": [
                    {
                        "Email": {
                            "content": "email"
                        }
                    }
                ],
                "Business_Requirements": [
                    {
                        "Multi-select": "choice"
                    }
                ]
            }

        }

        response = requests.post(url, headers=headers, json=data)
