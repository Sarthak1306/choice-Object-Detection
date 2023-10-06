# ------------------------------------------------------------------------------
#  <copyright file="HomeObjects.py" company="DKGLabs Pvt Ltd">
#      Copyright (c) DKGLabs Pvt Ltd. All Rights Reserved.
#      Information Contained Herein is Proprietary and Confidential.
#  </copyright>
#  ------------------------------------------------------------------------------

import streamlit as st 
import yaml
from utilsObjects import logo
from utilsObjects import Utils


st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/home.png')   

st.title("YOLO Object Detection App")
st.caption('This web application demostrate Object Detection')
st.header("Which objects/scenarios would you like to detect?")
logo()

labelContainer = st.container()


objectContainer = st.container()
with objectContainer:

    with open("models/Generic_YOLOv8/data.yaml", "r") as file1:
        yaml_file1_data = yaml.safe_load(file1)
    # with open("models/Violence_YOLOv8/data.yaml", "r") as file2:
    #     yaml_file2_data = yaml.safe_load(file2)
    #     Utils.set_yaml_data_list(yaml_file1_data["names"])
        classList = st.multiselect("Choose the objects for detection", options=yaml_file1_data["names"]) #+ yaml_file2_data["names"])

    st.write("You selected : ")
    st.write(classList)
    Utils.set_object_list(classList)

detectionContainer = st.container()
with detectionContainer:
    st.markdown("""
        # - [Image Detection](/Yolo_For_Image)
                """)