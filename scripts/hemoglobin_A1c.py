import matplotlib.pyplot as plt

def chart_pie(title, list_d, labels_d ):
    plt.title(title)
    plt.pie(list_d, labels=labels_d, autopct="%0.1f %%")
    plt.show()

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