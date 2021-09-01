import pickle

def Predictor(data):
    filename = 'models\model.sav'
    print(filename)
    loaded_model = pickle.load(open(filename, 'rb'))
    pred = loaded_model.predict(data)
    return pred