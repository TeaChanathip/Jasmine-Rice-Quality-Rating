import streamlit as st
import os
from ultralytics import YOLO
import cv2
import numpy as np
import matplotlib.pyplot as plt

@st.cache_data
def loadSegModel():
    seg_model = YOLO('./models/seg-model.onnx', task='segment')
    return seg_model

@st.cache_data
def runSegModel(test_image_path):
    # load the segmentation model
    seg_model = loadSegModel()
    
    imgsz = 1440 # for new model
    seg_results = seg_model.predict(source=test_image_path, imgsz=imgsz, device="0", conf=0.5)
    
    return seg_results

@st.cache_data
def displaySegResult(save_dir, results, max_display=25, save=False):
    colors = {
        0: (0, 255, 0), # Green mask for Jasmine rice
        1: (255, 0, 0), # Red mask for Non-jasmine rice
    }
    
    if len(results) > max_display:
        results = results[:max_display]
    
    # define figure size
    num_of_results = len(results)
    num_of_col = min(3, num_of_results)
    num_of_row = int(np.ceil(num_of_results / num_of_col))
    fig, axs = plt.subplots(num_of_row, num_of_col, figsize=(8*num_of_col, 8*num_of_row))
    
    for i, result in enumerate(results):
        base_image = result.orig_img
        base_image = cv2.cvtColor(base_image, cv2.COLOR_BGR2RGB)

        labels = result.boxes.cls.cpu().numpy()
        xy = result.masks.xy
        
        # draw masks of the detected objects (iterate over xy)
        blank_image = np.zeros_like(base_image)
        for mask, label in zip(xy, labels):
            mask = mask.reshape((-1, 1, 2))
            mask = mask.astype(np.int32)
            cv2.fillPoly(blank_image, [mask], colors[int(label)])
        
        alpha = 0.35
        cv2.addWeighted(blank_image, alpha, base_image, 1 - alpha, 0, base_image)
        
        if num_of_row > 1:
            ax = axs[i // num_of_col, i % num_of_col]
        else:
            ax = axs[i % num_of_col]
            
        ax.imshow(base_image)
        ax.axis('off')
        ax.title.set_text(os.path.basename(result.path))
    
    fig.suptitle("Results from segmentation model", fontsize=20, y=0.85)
    st.pyplot(fig)
    
    # save the figure
    if save:
        fig.savefig(f"{save_dir}/seg-results{num_of_results}.png")