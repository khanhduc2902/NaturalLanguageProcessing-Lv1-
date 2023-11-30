from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Load symptoms from CSV file
symptoms_data = {}
with open('trieuchung.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        if row:
            symptoms_data[row[1].lower()] = row[0]

def find_symptoms(text):
    matched_symptoms = []
    for keyword in symptoms_data:
        if keyword in text:
            matched_symptoms.append(symptoms_data[keyword])
    return matched_symptoms

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        text = request.form["text"].lower()

        # Tìm các triệu chứng khớp
        matched_symptoms = find_symptoms(text)

        if matched_symptoms:
            predictions = ", ".join(matched_symptoms)
        else:
            predictions = "Not Found"
         

        return render_template('result.html', input_text=text, prediction=predictions)

if __name__ == '__main__':
    app.run(debug=True)
