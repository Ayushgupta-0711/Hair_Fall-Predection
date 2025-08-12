import mysql.connector as mc
conn = mc.connect(user='root', password='ayush@#11', host='localhost', database='hairfall_p')

if conn.is_connected():
    print("You are connected.")
else:
    print('Unable to connect.')

mycursor = conn.cursor()


query = """CREATE TABLE data(
    genetics VARCHAR(50),
    hormonal_changes VARCHAR(50),
    medical_conditions VARCHAR(50),
    Medications & Treatments VARCHAR(50),
    nutritional_deficiencies VARCHAR(50),
    stress VARCHAR(50),
    age INT,
    poor_hair_care_habits VARCHAR(50),
    environmental_factors VARCHAR(50),
    smoking VARCHAR(50),
    weight_loss VARCHAR(50),
    predicted INT
)
"""

mycursor.execute(query)
print('Your table is created.')

mycursor.close()
conn.close()

