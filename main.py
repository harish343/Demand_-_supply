import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from flask import Flask, render_template, request
# import plotly.express as px

# df = pd.read_csv('data.csv')
# df.shape
# df.info()

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save(file.filename)
        return 'File uploaded successfully'
    return render_template('upload.html')
app.run(debug=True)
