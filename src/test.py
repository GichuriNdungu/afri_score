from preprocessing import df 
import numpy as np
import pickle 


try:
    with open('./models/model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("The file is a valid pickle file.")
except Exception as e:
    print("The file is not a valid pickle file. Error:", str(e))
 