import fonction_math
import tkinter

# mettre à jour l'affichage d'un écran

def main_essai():
    print(fonction.addition(2,4))
    print(fonction.puissance_de_dix(2))

app = tkinter.Tk()
app.title("Fenetre de test")

fr = tkinter.Frame(app,background="green",width=100,height=100)
fr.place(x=10,y=20)

lab = tkinter.Label(fr,text="0.000000")
lab.place(x =0,y=0)

app.mainloop()
if __name__ == '__main__':
    main_essai()