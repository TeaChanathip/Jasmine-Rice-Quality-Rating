import streamlit as st
from pathlib import Path
import gdown
import datetime

@st.cache_data
def createWorkingDir():
    # create working directory
    Path('./models').mkdir(parents=True, exist_ok=True)
    Path('./output').mkdir(parents=True, exist_ok=True)
    time = datetime.datetime.now().strftime("%y%m%d%H%M")
    save_dir = f"./output/run-{time}"
    Path(save_dir).mkdir(parents=True, exist_ok=True)

    # download the model
    seg_model_url = "1lB8lhWyuUWVZ3YLuzhFm0uUQrrkditWe"
    germ_cls_model_url = "1LwKwyoAwR_esRkkv2mG4Ej-_PZYsl6rr"

    gdown.download(f"https://drive.google.com/uc?id={seg_model_url}", "./models/seg-model.onnx", quiet=True)
    gdown.download(f"https://drive.google.com/uc?id={germ_cls_model_url}", "./models/rice-germ-cls-model.onnx", quiet=True)
    
    return save_dir