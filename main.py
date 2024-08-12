import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

class Model:
    def __init__(self, model, X_train, y_train, X_test, y_test):
        self.model = model
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test

        self.model.fit(X_train, y_train)

    def get_score(self):
        return self.model.score(self.X_test, self.y_test)
    
    def predict(self, X):
        return self.model.predict(X)
    
    def test(self, index):
        print("true_y: ", self.y_test[index])
        print("predicted vaule: ", self.model.predict(self.X_test.iloc[index].to_frame().T))

def run_web():
    st.title("hello world!")

def main():
    train = pd.read_csv("./dataset/Train.csv")
    test = pd.read_csv("./dataset/Test.csv")

    X_train, y_train = train.drop(columns=["class"]), train[["class"]].to_numpy().reshape(-1)
    X_test, y_test = test.drop(columns=["class"]), test[["class"]].to_numpy().reshape(-1)

    rf = RandomForestClassifier()

    model = Model(rf,X_train, y_train, X_test, y_test)

    run_web()

if __name__ == "__main__":
    main()