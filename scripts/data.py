import csv


listReturn = []
def readData( pathFile ):
    with open(pathFile) as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            # print(line)
            #print(f"line[2] : {line[2]} -- company : {company}")
            listReturn.append({
                "gender" : line[0],
                "age" : float( line[1] ),
                "hypertension" : line[2],
                "heart_disease" : int( line[3] ),
                "smoking_history" : line[4],
                "bmi" : float( line[5] ),
                "HbA1c_level" : float( line[6] ),
                "blood_glucose_level" : float( line[7] ),
                "diabetes" : int( line[8] )})
        
        # print("Datos leidos exitosamente!")
        # print(listReturn[10])
        # input("presione enter")
        return listReturn

def saludo():
    print("Saludos desde data.py")
