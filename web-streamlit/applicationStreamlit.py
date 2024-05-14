import streamlit as st
import os
import sys
import shutil
import cv2
import numpy as np
import gdown
from ultralytics import YOLO
import matplotlib.pyplot as plt
from pathlib import Path
import random
import pandas as pd
import wx

from createWorkingDir import createWorkingDir
from displayTestImages import displayTestImages

# create working directory
save_dir = createWorkingDir()
st.write(f"Saving directory: {save_dir}")


# browse user directory to select the testing image directory
# st.header("Select the testing image directory")

# test_image_path = None

# if st.button("Browse"):
#     # use wxPython to open a file dialog
#     app = wx.App(None)
#     style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE
#     dialog = wx.DirDialog(None, "Choose a directory:", style=style)
#     if dialog.ShowModal() == wx.ID_OK:
#         test_image_path = dialog.GetPath()
#     dialog.Destroy()

test_image_path = '../test'
    
st.write(f"Selected testing image directory: {test_image_path}")
    
# display example of testing image
st.header("Display the example of your testing images?")
if st.button("Display"):
    displayTestImages(test_image_path)



