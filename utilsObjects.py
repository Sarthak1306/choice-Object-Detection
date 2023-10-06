import yaml
import os
from streamlit_extras.app_logo import add_logo
import streamlit as st


def logo():
    add_logo("./images/dkg_logo.png", height=300)


class Utils:
    objectList = []
    dataList = []
    detectionClasses = []

    @classmethod
    def set_object_list(self,objList):
        Utils.objectList = objList
        print(Utils.objectList)


    @classmethod
    def get_object_list(self):
        return Utils.objectList


    @classmethod
    def set_yaml_data_list(self,recievedList):
        Utils.dataList = recievedList
        print(Utils.dataList)

    @classmethod
    def get_yaml_data_list(self):
        return Utils.dataList
    
    @classmethod
    def return_detection_list(self):
        Utils.detectionClasses = list(map(lambda x: Utils.dataList.index(x), Utils.objectList))
        return Utils.detectionClasses