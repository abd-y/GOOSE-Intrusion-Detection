import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class Model:
    def __init__(self):
        train = pd.read_csv("./dataset/Train.csv")
        test = pd.read_csv("./dataset/Test.csv")
        train = train[['stnum','time','sqNum', 'class']]
        test = test[['stnum','time','sqNum', 'class']]
        
        self.X_train, self.y_train = train.drop(columns=["class"]), train[["class"]].to_numpy().reshape(-1)
        self.X_test, self.y_test = test.drop(columns=["class"]), test[["class"]].to_numpy().reshape(-1)
        self.model = RandomForestClassifier()

        self.model.fit(self.X_train, self.y_train)

    def get_score(self):
        return self.model.score(self.X_test, self.y_test)
    
    def predict(self, X):
        return self.model.predict(X)
    
    def test(self, index):
        print("true_y: ", self.y_test[index])
        print("predicted value: ", self.model.predict(self.X_test.iloc[index].to_frame().T))

    def feature_importances(self):
        column_names = self.X_train.columns.to_list()
        important_features_dict = {}
        for index, value in enumerate(self.model.feature_importances_):
            important_features_dict[index] = value
            important_features_list = sorted(important_features_dict,
                                 key=important_features_dict.get,
                                 reverse=True)
        for i in important_features_list:
            print(f"{column_names[i]}: {important_features_dict[i]}")



