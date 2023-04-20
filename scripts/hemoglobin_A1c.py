import matplotlib.pyplot as plt

def chart_pie(title, list_d, labels_d ):
    plt.title(title)
    plt.pie(list_d, labels=labels_d, autopct="%0.1f %%")
    plt.show()

def chart_scatter( title, list_x, list_y):
    #grafica de dispersión
    plt.title(title)
    plt.scatter(list_x, list_y)
    plt.show()

def filter_gender(gender , list_d):
    list_bmi = []
    list_a1c = []
    list_glucose = []
    for row in list_d:
        if row["gender"] == gender:
            list_bmi.append( row["bmi"] )
            list_a1c.append( row["HbA1c_level"] )
            list_glucose.append( row["blood_glucose_level"] )
        
    return list_bmi, list_a1c, list_glucose

def chart_HbA1c( data ):
    print("hola desde HbA1c!!!")
    # print( data[10] )
    # arrays
    # man = [ 0, 0, 0 ] --> [normal, pred, diabec]
    # woman = [ 0, 0, 0 ] --> --> [normal, pred, diabec]
    # other = [ 0, 0, 0 ] --> --> [normal, pred, diabec]
    man = [ 0, 0, 0 ] 
    woman = [ 0, 0, 0 ]
    other = [ 0, 0, 0 ]
    list_labels = ["normal","prediab","diabetic"]
    for row in data:
        #print( row )
        if row["gender"] == "Male":
            if row["HbA1c_level"] < 5.7:
                man[0] += 1
            elif row["HbA1c_level"] < 6.5:
                man[1] += 1
            else:
                man[2] += 1
        elif row["gender"] == "Female":
            if row["HbA1c_level"] < 5.7:
                woman[0] += 1
            elif row["HbA1c_level"] < 6.5:
                woman[1] += 1
            else:
                woman[2] += 1
        else:
            if row["HbA1c_level"] < 5.7:
                other[0] += 1
            elif row["HbA1c_level"] < 6.5:
                other[1] += 1
            else:
                other[2] += 1

    # print(f"man: { man }")
    # print(f"woman: { woman }")
    # print(f"other: { other }")
    # #print( (man[0] + man[1] + man[2] + woman[0] + woman[1] + woman[2] + other[0] + other[1] + other[2]) )

    chart_pie("Porcentaje de los niveles de glucosa de los hombre", man, list_labels)

    chart_pie("Porcentaje de los niveles de glucosa de las mujeres", woman, list_labels)

    chart_pie('Porcentaje de los niveles de glucosa de "otros"', other, list_labels)


    input("presiona enter")

def chart_relation( data ):
    list_bmi_man, list_a1c_man, list_g_man = filter_gender("Male", data)
    list_bmi_woman, list_a1c_woman, list_g_woman = filter_gender("Female", data)
    list_bmi_oth, list_a1c_oth, list_g_other = filter_gender("Other", data)
    
    chart_scatter('Relacion bmi & A1c hombre', list_bmi_man, list_a1c_man)
    chart_scatter('Relacion bmi & A1c mujer', list_bmi_woman, list_a1c_woman)
    chart_scatter('Relacion bmi & A1c other', list_bmi_oth, list_a1c_oth)
    
    chart_scatter('Relacion bmi & glucosa hombre', list_bmi_man, list_g_man)
    chart_scatter('Relacion bmi & glucosa mujer', list_bmi_woman, list_g_woman)
    chart_scatter('Relacion bmi & glucosa other', list_bmi_oth, list_g_other)