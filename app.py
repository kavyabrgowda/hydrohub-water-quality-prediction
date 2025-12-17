from flask import Flask, render_template, request, jsonify
import predict, contamination, treatment
from flask import Flask, render_template, request
import predict, contamination, treatment
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64
import os


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def water_quality_prediction():
    if request.method == 'POST':
        ph = float(request.form['ph'])
        tds = float(request.form['tds'])
        hardness = float(request.form['hardness'])  # Replacing EC with Hardness
        
        wqi, classification = predict.calculate_wqi(ph, tds, hardness)
        return render_template('result.html', wqi=wqi, classification=classification)
    
    return render_template('prediction.html')


@app.route('/contamination')
def water_contamination():
    wqi = request.args.get('wqi', type=float)
    contamination_level = contamination.get_contamination_level(wqi)

    # Generate the graph dynamically
    img = BytesIO()
    fig, ax = plt.subplots(figsize=(16, 4))

    # Define WQI categories for visualization (Extended to 20,000)
    levels = [0, 50, 100, 250, 500, 1000, 2000, 3000, 4000, 5000, 10000, 15000, 20000]
    colors = ['lightgreen', 'green', 'yellow', 'orange', 'red', 'darkred', 
        '#8B4513', '#4B0082', '#8B0000', '#800000', '#5B0E2D', 'black']
    labels = [
        "Safe", "Moderate", "Acceptable", "Poor", "Unhealthy", "Severely Polluted", 
        "Toxic", "Hazardous", "Critical", "Extreme Danger", "Lethal Contamination", "Uninhabitable"
    ]

    for i in range(len(levels) - 1):
        ax.barh([0], [levels[i+1] - levels[i]], left=levels[i], color=colors[i], label=labels[i])

    ax.axvline(x=wqi, color='blue', linestyle='dashed', linewidth=2, label=f'Current WQI: {wqi}')
    
    ax.set_xlabel("Water Quality Index (WQI)")
    ax.set_ylabel("Contamination Levels")
    ax.set_title("WQI Contamination Level Analysis")
    ax.legend()

    plt.savefig(img, format='png')
    plt.close(fig)
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()

    return render_template('contamination.html', contamination_level=contamination_level, graph_url=graph_url, wqi=wqi)


@app.route('/treatment')
def water_treatment():
    wqi = request.args.get('wqi', type=float)
    suggestion = treatment.get_treatment_suggestions(wqi)
    return render_template('treatment.html', suggestion=suggestion)




if __name__ == '__main__':
    # Use PORT provided by host (Render/Heroku). Default to 5000 locally.
    port = int(os.environ.get("PORT", 5000))
    # Never run debug=True in production
    app.run(host="0.0.0.0", port=port, debug=False)