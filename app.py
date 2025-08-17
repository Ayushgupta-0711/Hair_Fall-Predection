from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
import mysql.connector as mc
conn = mc.connect(user='root', password='ayush@#11', host='localhost', database='hairfall_p')
import joblib
model = joblib.load("VotingModel.lb")


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('userdata.html') 


import numpy as np  # Import NumPy at the top

@app.route('/userdata', methods=['GET', 'POST'])
def userdata():
    if request.method == 'POST':
        genetics = int(request.form['genetics'])
        hormonal_changes = int(request.form['hormonal_changes'])
        medical_conditions = int(request.form['medical_conditions'])
        medications_treatments = int(request.form['medications_treatments'])
        nutritional_deficiencies = int(request.form['nutritional_deficiencies'])
        stress = int(request.form['stress_level'])
        age = int(request.form['age'])
        poor_hair_care_habits = int(request.form['hair_care_habits'])
        environmental_factors = int(request.form['environmental_factors'])
        smoking = int(request.form['smoking'])
        weight_loss = int(request.form['weight_loss'])

        # Convert to NumPy array and reshape it into a 2D array
        unseen_data = np.array([[genetics, hormonal_changes, medical_conditions, medications_treatments, 
                                  nutritional_deficiencies, stress, age, poor_hair_care_habits, 
                                  environmental_factors, smoking, weight_loss]])
        
        # Predict using the model
        output = model.predict(unseen_data)[0]

        # Insert data into MySQL database
        query = """INSERT INTO data (genetics,hormonal_changes,medical_conditions,medications_treatments,
        nutritional_deficiencies,stress,age,poor_hair_care_habits,environmental_factors,smoking,weight_loss,predicted)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        mycursor = conn.cursor()
        details = (genetics, hormonal_changes, medical_conditions, medications_treatments, 
                   nutritional_deficiencies, stress, age, poor_hair_care_habits, 
                   environmental_factors, smoking, weight_loss, int(output))

        mycursor.execute(query, details)
        conn.commit()
        mycursor.close()

        # Return prediction result
        return "Patient has hairfall." if output == 1 else "Patient doesn't have hairfall."


        # # Return the output
        # if output == 0:
        #     return f"Patient doesn't have hairfall."
        # else:
        #     return f"Patient have hairfall."


@app.route('/patient_history')
def patient_history():
    
    conn = mc.connect(user="root", host="localhost", password="ayush@#11", database='hairfall_p')
    mycursor = conn.cursor()
    query = "SELECT * FROM data"  
    mycursor.execute(query)
    data = mycursor.fetchall()

    mycursor.close()
    conn.close()

    return render_template('patient_history.html', userdetails=data)

if __name__ == "__main__":
    app.run(debug=True)





