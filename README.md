# AI Art Detector

This project focuses on image classification using Convolutional Neural Networks to distinguish between AI-generated and humans made art. The project includes two Jupyter notebooks, "catsvsdogs.ipynb" and "aiartdetector.ipynb," in the "notebooks" folder, which document the process of creating an image classifier for the CatsVSDogs dataset and a custom dataset. Additionally, it provides the dataset containing both AI-generated art and real art for training the image classifier.
In the "webapp" folder, a Flask-based web application is developed to showcase the image classification model. Users can upload images to the web application, and the trained model will predict whether the image falls into the category of AI-generated art, or human made art.


# Project Structure

The project is organized into the following structure:

* notebooks/
    * catsvsdogs.ipynb: Jupyter notebook containing the code for training an image classifier to distinguish between cats and dogs.
    * aiartdetector.ipynb: Jupyter notebook for training a model to differentiate between AI-generated art and real art.

* dataset/
    * ArtDataset/
        * aidataset: Folder containing AI-generated art images.
        * realdataset: Folder containing images of real art.

* webapp/
    * static/: Contains static css file.
        * img/: Folder to store user-uploaded images during the prediction.
    * templates/: HTML templates for the Flask web application.
    * app.py: m=Main Flask application
    * AIArtclassifier.pth: Pretrained fully exported pytorch binary classification model.


## Getting Started

1. Clone the repository:

```sh
git clone https://github.com/angelri03/ai-art-detector.git
```

2. Install the required dependencies:
```sh
pip install -r requirements.txt
```

### Usage

* Open and run the Jupyter notebooks in the "notebooks" folder to train the image classification models. (move the ArtDataset to the same location as the Jupyter notebooks for it to work)

* Running the Flask web application to test if an imagfe is AI-generated or not:

```sh
cd webapp
python app.py
```
The application will be accessible at http://localhost:5000 in your web browser.
Then upload any image and submit it. The web application will send a response with either "ai generated" or "human made".


## Acknowledgments

* Special thanks to my Project Academic Tutor Bereket A. Yilma, who provided guidance and a basis for this image classification project.
