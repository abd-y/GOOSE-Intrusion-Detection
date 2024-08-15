# GOOSE Intrusion Detection system (IDS)
A very simple demo of a machine learning model to classify GOOSE packets if they are normal, injection, masquerade, replay, or fault. GOOSE is based on the IEC-61850 protocol. The model accuracy achieved is 100% on the testing set using random forest classifier. 
## Options and requirements to run the code
1- Using docker: [Download Docker](https://docs.docker.com/engine/install/)<br>
2- Or using python, but the recommended option using docker.
## Option 1 run the code using docker
Make sure before running the following command you're inside the directory where the code exists.
```
docker compose up
```
## Option 2 run the code using python
```
pip install -U numpy matplotlib pandas scikit-learn streamlit
```
Make sure before running the following command you're inside the directory where the code exists.
```
streamlit run main.py
```
Then copy the displayed url and paste it in any web browser you have.<br>
Credits to Silvio Quincozes for making the [dataset](https://www.kaggle.com/datasets/sequincozes/power-system-intrusion-dataset?select=Train.csv).
