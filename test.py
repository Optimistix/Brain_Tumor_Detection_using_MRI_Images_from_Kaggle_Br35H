import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'url': 'https://raw.githubusercontent.com/Optimistix/Brain_Tumor_Detection_using_MRI_Images_from_Kaggle_Br35H/main/y234.jpg'}

result = requests.post(url, json=data).json()
print(result)
