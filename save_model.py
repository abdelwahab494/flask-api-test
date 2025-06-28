import pickle
from model_utils import is_even_model

with open("model.pkl", "wb") as f:
    pickle.dump(is_even_model, f)