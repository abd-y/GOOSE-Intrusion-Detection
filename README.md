# GOOSE Intrusion Detection system (IDS)
A very simple demo of a machine learning model to classify GOOSE packets if they are normal, injection, masquerade, replay, or fault. GOOSE is based on the IEC-61850 protocol. The model accuracy achieved is 100% on the testing set using random forest classifier. 
## Requirements
1- [Download Docker](https://docs.docker.com/engine/install/)<br>
2- Or python if you want to run it using python but the recommended option using docker.
## 1- Run the code using docker
Make sure before running the following command you're inside the directory where the code exists.
```
docker compose up
```
## 2- Run the code using python
```
pip install -U numpy matplotlib pandas scikit-learn streamlit
```
Make sure before running the following command you're inside the directory where the code exists.
```
streamlit run main.py
```
Then copy the displayed url and paste it in any web browser you have.<br>
Credits to Silvio Quincozes for making the [dataset](https://www.kaggle.com/datasets/sequincozes/power-system-intrusion-dataset?select=Train.csv).
