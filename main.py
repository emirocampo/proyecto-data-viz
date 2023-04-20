import scripts.data as sd
import scripts.hemoglobin_A1c as hem
import os

pathFile = "./data/diabetes_prediction.csv"

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def operation( k, data ):
    # dict_oper = {
    #     1 : hem.chart_HbA1c( data ),
    #     2 : hem.chart_relation( data )
    # }
    # dict_oper[ k ]

    match k:
        case 1:
            hem.chart_HbA1c( data )
        case 2:
            hem.chart_relation( data )
        case _:
            print("Error en las llaves del match - case")




def main():
    # print("Entré!!!")
    # sd.saludo()

    list_dt = sd.readData(pathFile)
    
    flag = True
    while flag:
        clear()
        print("########## MENÚ ##########")
        print("1. % HbA1c en hombres y mujeres")
        print("2. relacion bmi y A1c")
        print("0. salir")
        try:
            opc = int( input() )
        except:
            clear()
            print("Se debe escribir un numero de la lista.")
            input("presione enter")
        else:
            if opc >=1  and opc < 3:
                # print("Opción valida")
                # input("presione enter")
                operation( opc, list_dt )
                pass
            else:
                print("saliste del programa.")
                flag = False
                
        

if __name__ == "__main__":
    main()