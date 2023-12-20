# Brain_Tumor_Detection_using_MRI_Images
Deep Learning (Convolutional Neural Networks) to predict whether an MRI image is from a tumorous or non-tumorous sample 

## Problem Description
A Brain tumor is considered as one of the aggressive diseases, among children and adults. Brain tumors account for 85 to 90 percent of all primary Central Nervous System(CNS) tumors. Every year, around 11,700 people are diagnosed with a brain tumor. The 5-year survival rate for people with a cancerous brain or CNS tumor is approximately 34 percent for men and36 percent for women. Brain Tumors are classified as: Benign Tumor, Malignant Tumor, Pituitary Tumor, etc. Proper treatment, planning, and accurate diagnostics should be implemented to improve the life expectancy of the patients. The best technique to detect brain tumors is Magnetic Resonance Imaging (MRI). A huge amount of image data is generated through the scans. These images are examined by the radiologist. A manual examination can be error-prone due to the level of complexities involved in brain tumors and their properties.
Application of automated classification techniques using Machine Learning(ML) and Artificial Intelligence(AI)has consistently shown higher accuracy than manual classification. Hence, proposing a system performing detection and classification by using Deep Learning Algorithms using Convolution-Neural Network (CNN), Artificial Neural Network (ANN), and Transfer-Learning (TL) would be helpful to doctors all around the world.

Brain Tumors are complex. There are a lot of abnormalities in the sizes and location of the brain tumor(s). This makes it really difficult for complete understanding of the nature of the tumor. Also, a professional Neurosurgeon is required for MRI analysis. Often times in developing countries the lack of skillful doctors and lack of knowledge about tumors makes it really challenging and time-consuming to generate reports from MRI’. So an automated system on Cloud can solve this problem.

## Data

Data From: Br35H :: Brain Tumor Detection 2020 on Kaggle (https://www.kaggle.com/datasets/ahmedhamada0/brain-tumor-detection)

## Notebook
The notebook includes
        Data preparation and data cleaning
        EDA, feature importance analysis
        Model selection process and parameter tuning

## Script train.py
The script train.py can be used to:
        Train the final model
        Save it to a file using pickle

## Script predict.py
The script predict.py can be used to:
        Load the model (for use within Docker)
        Define the Lambda handler

Similarly, the script predict_outside_Docker.py can be used to:
        Load the model (for use outside Docker, since we then need to use the tflite version included with Tensorflow)
        Define the Lambda handler

You can execute predict_outside_Docker.py to locally test the model on a single sample (an MRI image from a tumorous sample):

	python predict_outside_Docker.py

The expected output is

{'prediction': 0.9496070146560669}

## Files with dependencies
        Pipenv and Pipenv.lock
        Dockerfile

## Setting up the virtual environment

Install pipenv, to create a virtual environment:

        pip install pipenv

Install dependencies using the requirements file:

        pipenv install -r requirements.txt

Activate the virtual environment:

        pipenv shell

Now run

        python train.py
to train and save the best model, and

        python predict.py
        python test.py

to test the saved model on 1 sample

## Dockerization

Build the Docker container:

        docker build -t brain_cancer_detection .

Run the Docker container:

        docker run -it -p 8080:8080 brain_cancer_detection:latest

As before, to test that the prediction app is running properly via Docker, you can type

        python test.py

to test the saved model on 1 sample (an MRI image from a tumorous sample)

and the expected output is

{'prediction': 0.9496070146560669}

## Deployment

Deployment was carried out using Google Cloud Run

To run the service, go to

https://console.cloud.google.com/run/detail/us-central1/brain-cancer-detection/revisions?project=brain-cancer-detection-408719

The URL is

https://breast-cancer-diagnostic-e7c74nc6ea-wl.a.run.app/

which is specified in

        test_gcloud.py

and once the container is running via Google Cloud Run, you can run

        python test_gcloud.py

to test the saved model on 1 sample (an MRI image from a tumorous sample)

and the expected output is (as before)

{'prediction': 0.9496070146560669}

Here is a screenshot of the service created on Google Cloud Run:

<img src="https://github.com/Optimistix/Brain_Tumor_Detection_using_MRI_Images_from_Kaggle_Br35H/blob/main/Google_Cloud_Run_Service_Screenshot_Brain_Cancer_Detection.png" style="display:block;float:none;margin-left:auto;margin-right:auto;width:100%">
