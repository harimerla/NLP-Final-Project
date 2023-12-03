# NLP-Final-Project
By harimerla and Bhanuvardhan

The goal of this project is to build chatbot so that it will answer queries using large language models.

### Dataset
we took the data from below link and converted the data from json file to csv format. If you want to directly
use the csv format file. Kindly check the csv file in data folder.

https://www.kaggle.com/datasets/antonkozyriev/unity3d-faq?select=intents.json

### Model 

Models for chatbot - 

1. Bert (Bhanuvardhan)
2. OPEN-AI GPT (Harimerla)

Model Evaluation - 

1. Trainer (Transformers)

### Clone repository
1. open your directory where you want to clone the project
2. run the below GITHUB CLI
gh repo clone harimerla/NLP-Final-Project

### Running Instructions

1. Find the models which you want to run which starts with modelname.ipynb
2. To load the data file for bert store the csv file in data folder
3. Download the required dataset from the repository or download the json file from provided link
4. Download the required libraries.
5. Run the respective jupyter notebook

### Results 

text = "How to make a game?"
predict(text)

(tensor([[2.6690e-03, 1.4602e-03, 1.6699e-03,  ..., 1.7890e-05, 1.4129e-05,
          1.4420e-05]], device='cuda:0', grad_fn=<SoftmaxBackward0>),
 tensor(323, device='cuda:0'),
 'Start with the first, follow just what he does, and then try to experiment and edit things later.')

References:

1. Built a chatbot with Bert | EDA + VIS
https://www.kaggle.com/code/eyadgk/build-a-chatbot-with-bert-eda-vis/notebook#14-||-Load-the-model

2. Wordcount 
https://www.datacamp.com/tutorial/wordcloud-python

3. chatgpt references with prompt like 'below is my training code. what wrong in this '

