import tkinter
import fonction_wdgets

app = tkinter.Tk()
app.title("CALCULATRICE")
txt = tkinter.StringVar()
txt.set("0.00")
n = " "
#fonctions : ======================================================DEBUT==================================================================#

def zero_affiche():
    global txt
    global n
    n += "0"
    txt.set(n)
    fonction_wdgets.zero()
def un_affiche():
    global txt
    global n
    n += "1"
    txt.set(n)
    fonction_wdgets.un()
def deux_affiche():
    global txt
    global n
    n += "2"
    txt.set(n)
    fonction_wdgets.deux()
def trois_affiche():
    global txt
    global n
    n += "3"
    txt.set(n)
    fonction_wdgets.trois()
def quatre_affiche():
    global txt
    global n
    n += "4"
    txt.set(n)
    fonction_wdgets.quatre()
def cinq_affiche():
    global txt
    global n
    n += "5"
    txt.set(n)
    fonction_wdgets.cinq()
def six_affiche():
    global txt
    global n
    n += "6"
    txt.set(n)
    fonction_wdgets.six()
def sept_affiche():
    global txt
    global n
    n += "7"
    txt.set(n)
    fonction_wdgets.sept()
def huit_affiche():
    global txt
    global n
    n += "8"
    txt.set(n)
    fonction_wdgets.huit()
def neuf_affiche():
    global txt
    global n
    n += "9"
    txt.set(n)
    fonction_wdgets.neuf()
def plus_affiche():
    global txt
    global n
    n += "+"
    txt.set(n)
    fonction_wdgets.plus()
def moins_affiche():
    global txt
    global n
    n += "-"
    txt.set(n)
    fonction_wdgets.moins()
def fois_affiche():
    global txt
    global n
    n += "x"
    txt.set(n)
    fonction_wdgets.mul()
def div_affiche():
    global txt
    global n
    n += "/"
    txt.set(n)
    fonction_wdgets.div()
def egal_affiche():
    global txt
    global n
    res = fonction_wdgets.egal()
    txt.set("= " + str(res))
    n = " "

def sinus_affiche():
    global txt
    txt.set("Sin")
    fonction_wdgets.sinus()
    
def clear_affiche():
    global txt
    txt.set(" ")
    fonction_wdgets.clear()

def cosinus_affiche():
    global txt
    txt.set("Cos")
    fonction_wdgets.cosinus()

def tangente_affiche():
    global txt
    txt.set("Tan")
    fonction_wdgets.tangente()

def cotan_affiche():
    global txt
    txt.set("Cotan")
    fonction_wdgets.cotangente()

def logarithme_affiche():
    global txt
    txt.set("log")
    fonction_wdgets.logarithme()

def logarithme_neperien_affiche():
    global txt
    txt.set("ln")
    fonction_wdgets.logarithme_neperien()

def exponentielle_affiche():
    global txt
    txt.set("exp")
    fonction_wdgets.exponentielle()

def puissance_affiche():
    global txt
    txt.set("10exp")
    fonction_wdgets.puissance()
# ===============================================================FIN======================================================================#

# attributs du frame
largeur_frame = 400
hauteur_frame = 650

#frame de la calculatrice
frame = tkinter.Frame(app, bg='lightgray', width=largeur_frame, height=hauteur_frame)
frame.pack(padx=10, pady=10)

#attributs frame boutons
largeur_frame_touche = largeur_frame
hauteur_frame_touche = 500

#frame des touches 
frame_touche = tkinter.Frame(frame, bg='blue', width=largeur_frame_touche, height=hauteur_frame_touche)
frame_touche.place(x=0, y =hauteur_frame - hauteur_frame_touche)

#frame pour l'écran
frame_ecran = tkinter.Frame(frame,background="black",width=380,height=120)
frame_ecran.place(x=10,y=10)

#pas verticale et horizontale des boutons
pas_boutton_x = largeur_frame_touche / 4
pas_boutton_y = hauteur_frame_touche / 7

# hauteur bouttons
h = 3
l = 9

# ==========================================================================#
#bt sin
bt_sin = tkinter.Button(frame_touche,text="Sin",background='red',width=l,height=h,command=sinus_affiche)
bt_sin.place(x= 0,y = 0)

#bt cos
bt_cos = tkinter.Button(frame_touche,text="Cos",background='red',width=l,height=h,command=cosinus_affiche)
bt_cos.place(x= pas_boutton_x,y = 0)

#bt tan
bt_tan = tkinter.Button(frame_touche,text="Tan",background='red',width=l,height=h,command=tangente_affiche)
bt_tan.place(x= 2*pas_boutton_x,y = 0)

#bt cotan
bt_cotan = tkinter.Button(frame_touche,text="Cotan",background='red',width=l,height=h,command=cotan_affiche)
bt_cotan.place(x= 3*pas_boutton_x,y = 0)

#============================================================================#
#bt log 
bt_cotan = tkinter.Button(frame_touche,text="log",background='red',width=l,height=h,command=logarithme_affiche)
bt_cotan.place(x= 0,y = pas_boutton_y )

#bt exp
bt_cotan = tkinter.Button(frame_touche,text="exp",background='red',width=l,height=h,command= exponentielle_affiche)
bt_cotan.place(x= pas_boutton_x,y = pas_boutton_y )

#bt 10 exp
bt_cotan = tkinter.Button(frame_touche,text="10 exp",background='red',width=l,height=h,command=puissance_affiche)
bt_cotan.place(x= 2*pas_boutton_x,y = pas_boutton_y )

#bt ln
bt_cotan = tkinter.Button(frame_touche,text="ln",background='red',width=l,height=h,command=logarithme_neperien_affiche)
bt_cotan.place(x= 3*pas_boutton_x,y = pas_boutton_y )

#==============================================================================#
#bt C effacement
bt_cotan = tkinter.Button(frame_touche,text="C",background='red',width=l,height=h,command= clear_affiche)
bt_cotan.place(x= 0,y = 2*pas_boutton_y )   

#bt de division
bt_cotan = tkinter.Button(frame_touche,text="/",background='red',width=l,height=h,command= div_affiche)
bt_cotan.place(x= pas_boutton_x,y = 2*pas_boutton_y ) 

#bt de multiplication
bt_cotan = tkinter.Button(frame_touche,text="x",background='red',width=l,height=h,command= fois_affiche)
bt_cotan.place(x= 2*pas_boutton_x,y = 2*pas_boutton_y ) 

#bt de delete
bt_cotan = tkinter.Button(frame_touche,text="del",background='red',width=l,height=h)
bt_cotan.place(x= 3*pas_boutton_x,y = 2*pas_boutton_y )

#===============================================================================#
#bt 7
bt_cotan = tkinter.Button(frame_touche,text="7",background='red',width=l,height=h,command=sept_affiche)
bt_cotan.place(x= 0,y = 3*pas_boutton_y )  

#bt 8
bt_cotan = tkinter.Button(frame_touche,text="8",background='red',width=l,height=h,command=huit_affiche)
bt_cotan.place(x= pas_boutton_x,y = 3*pas_boutton_y )  

#bt 9
bt_cotan = tkinter.Button(frame_touche,text="9",background='red',width=l,height=h,command=neuf_affiche)
bt_cotan.place(x= 2*pas_boutton_x,y = 3*pas_boutton_y ) 

#bt soustraction -
bt_cotan = tkinter.Button(frame_touche,text="-",background='red',width=l,height=h,command=moins_affiche)
bt_cotan.place(x= 3*pas_boutton_x,y = 3*pas_boutton_y ) 

#===============================================================================#
#bt 4
bt_cotan = tkinter.Button(frame_touche,text="4",background='red',width=l,height=h,command=quatre_affiche)
bt_cotan.place(x= 0,y = 4*pas_boutton_y )  

#bt 5
bt_cotan = tkinter.Button(frame_touche,text="5",background='red',width=l,height=h,command=cinq_affiche)
bt_cotan.place(x= pas_boutton_x,y = 4*pas_boutton_y )  

#bt 6
bt_cotan = tkinter.Button(frame_touche,text="6",background='red',width=l,height=h,command=six_affiche)
bt_cotan.place(x= 2*pas_boutton_x,y = 4*pas_boutton_y )  

#bt +
bt_cotan = tkinter.Button(frame_touche,text="+",background='red',width=l,height=h,command=plus_affiche)
bt_cotan.place(x= 3*pas_boutton_x,y = 4*pas_boutton_y )  

#============================================================================#
#bt 1
bt_cotan = tkinter.Button(frame_touche,text="1",background='red',width=l,height=h,command=un_affiche)
bt_cotan.place(x= 0,y = 5*pas_boutton_y)  

#bt 2
bt_cotan = tkinter.Button(frame_touche,text="2",background='red',width=l,height=h,command=deux_affiche)
bt_cotan.place(x= pas_boutton_x,y = 5*pas_boutton_y) 

#bt 3
bt_cotan = tkinter.Button(frame_touche,text="3",background='red',width=l,height=h,command=trois_affiche)
bt_cotan.place(x= 2*pas_boutton_x,y = 5*pas_boutton_y) 

#bt =
bt_cotan = tkinter.Button(frame_touche,text="=",background='red',width=l,height=2*h+2,command=egal_affiche)
bt_cotan.place(x= 3*pas_boutton_x,y = 5*pas_boutton_y) 

#============================================================================#
#bt %
bt_cotan = tkinter.Button(frame_touche,text="%",background='red',width=l,height=h)
bt_cotan.place(x= 0,y = 6*pas_boutton_y )  

#bt 0
bt_cotan = tkinter.Button(frame_touche,text="0",background='red',width=l,height=h,command= zero_affiche )
bt_cotan.place(x= pas_boutton_x,y = 6*pas_boutton_y )  

#bt ,
bt_cotan = tkinter.Button(frame_touche,text=",",background='red',width=l,height=h)
bt_cotan.place(x= 2*pas_boutton_x,y = 6*pas_boutton_y )

#Text à afficher sur l'écran
text = tkinter.Label(frame_ecran,textvariable=txt,width=18,height=2,font=("ubuntu",30))
text.place(x=15,y=20)    

app.mainloop()
    

#if __name__ == '__main__':
 #   main()