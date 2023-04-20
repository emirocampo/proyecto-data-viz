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
    dict_oper = {
        1 : hem.chart_HbA1c( data )
    }
    dict_oper[ k ]




def main():
    # print("Entré!!!")
    # sd.saludo()

    list_dt = sd.readData(pathFile)
    
    flag = True
    while flag:
        clear()
        print("########## MENÚ ##########")
        print("1. % HbA1c en hombres y mujeres")
        print("0. salir")
        try:
            opc = int( input() )
        except:
            clear()
            print("Se debe escribir un numero de la lista.")
            input("presione enter")
        else:
            if opc >=1  and opc < 2:
                # print("Opción valida")
                # input("presione enter")
                operation( opc, list_dt )
                pass
            else:
                print("saliste del programa.")
                flag = False
                
        

if __name__ == "__main__":
    main()