import streamlit as st
import os
import matplotlib.pyplot as plt
import cv2
import numpy as np

@st.cache_data
def displayTestImages(test_image_path):
    test_images = os.listdir(test_image_path)
    test_images = [os.path.join(test_image_path, img) for img in test_images]

    num_of_test_img = len(test_images)

    # pick 25 random images from the test set
    picked_images = np.random.choice(test_images, min(25, num_of_test_img), replace=False)

    # define figure size
    num_of_col = min(5, num_of_test_img)
    num_of_row = int(np.ceil(num_of_test_img / num_of_col))
    fig, axs = plt.subplots(num_of_row, num_of_col, figsize=(4*num_of_col, 5*num_of_row))
    
    for i, image_path in enumerate(picked_images):
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        if num_of_row > 1:
            ax = axs[i // num_of_col, i % num_of_col]
        else:
            ax = axs[i % num_of_col]
            
        ax.imshow(image)
        ax.title.set_text(os.path.basename(image_path))
        ax.axis('off')
    
    st.pyplot(fig)