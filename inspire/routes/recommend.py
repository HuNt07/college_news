from flask import Flask, render_template, redirect, url_for, request, session
from inspire.mlmodel.recom_category import get_recommendations
import json
from inspire import app

@app.post('/recommend')
def predict():
    data = request.get_json()
    category = data["category"]
    test = get_recommendations(category).tolist()
    arr = []
    for i in range(1,len(test)+1):
        arr.append(i)
    print(arr)
    print(test)
    dictionary = dict(zip(arr, test))
    print(dictionary)

    return json.dumps(dictionary)

