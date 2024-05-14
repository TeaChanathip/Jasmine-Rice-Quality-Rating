# Jasmin rice quality measurement

blah blah

## Prepare your environment
```bash
pip install -r requirements.txt
```
 
## Run Run GO GO

run run

## Overview of the project
- Read image
    - Should use `jpg` format
- Preprocess image for segmentation
    - Resize all images to `1440x1440`
- Segmentation
    - Use `YoloV8 Segmentation` for first stage mask and predict if each rice is jasmine rice or not
    - Then, use `Watershed` for quality mask
- Classification
    - Use `YoloV8 Classification` for label rice's quality as `Good`, `Moderate`, `Bad`
- Quality measurement
    - Each rice's score computed by mapping function of:
        1. Ratio of rice's `high`/`width` from convex hull of watershed result
        2. Rotio of `#jasmine rice` / `#total rice`
- Output
    - Overall
        - Segmentated image
        - Overall quality score
        - Ratio of jasmine rice
    - Per rice
        - Rice's image
        - Jasmine rice or not
        - Quality label

## Firstly, Take your rices images
![Rice input image](./assets/input.png)

And put your image in the `test` folder like this:
```
root
|__ test
    |__ input1.jpg
    |__ input2.jpg
    |__ input3.jpg
    |__ ...
|__ main-application.ipynb
|__ ...
```

## Segmentation from YoloV8
![YOLO Segmentation](./assets/segment.png)

## Watershed segmentation
![Watershed1](./assets/watershed-1.png)
![Watershed2](./assets/watershed-2.png)

## Classification from YoloV8
![YOLO Classification](./assets/rice-stats.png)