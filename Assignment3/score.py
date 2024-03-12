def score(text:str, model, threshold:float):
    proba = model.predict_proba([text])[0][1]
    prediction = 1 if proba >= threshold else 0
    return prediction, proba
 