import tkinter
import fonction
import fonction_wdgets

def main():
    app = tkinter.Tk()
    app.title("CALCULATRICE")

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
    bt_sin = tkinter.Button(frame_touche,text="Sin",background='red',width=l,height=h)
    bt_sin.place(x= 0,y = 0)

    #bt cos
    bt_cos = tkinter.Button(frame_touche,text="Cos",background='red',width=l,height=h)
    bt_cos.place(x= pas_boutton_x,y = 0)

    #bt tan
    bt_tan = tkinter.Button(frame_touche,text="Tan",background='red',width=l,height=h)
    bt_tan.place(x= 2*pas_boutton_x,y = 0)

    #bt cotan
    bt_cotan = tkinter.Button(frame_touche,text="Cotan",background='red',width=l,height=h)
    bt_cotan.place(x= 3*pas_boutton_x,y = 0)

    #============================================================================#
    #bt log 
    bt_cotan = tkinter.Button(frame_touche,text="log",background='red',width=l,height=h)
    bt_cotan.place(x= 0,y = pas_boutton_y )

    #bt exp
    bt_cotan = tkinter.Button(frame_touche,text="exp",background='red',width=l,height=h)
    bt_cotan.place(x= pas_boutton_x,y = pas_boutton_y )

    #bt 10 exp
    bt_cotan = tkinter.Button(frame_touche,text="10 exp",background='red',width=l,height=h)
    bt_cotan.place(x= 2*pas_boutton_x,y = pas_boutton_y )

    #bt ln
    bt_cotan = tkinter.Button(frame_touche,text="ln",background='red',width=l,height=h)
    bt_cotan.place(x= 3*pas_boutton_x,y = pas_boutton_y )

    #==============================================================================#
    #bt C effacement
    bt_cotan = tkinter.Button(frame_touche,text="C",background='red',width=l,height=h,command=fonction_wdgets.clear)
    bt_cotan.place(x= 0,y = 2*pas_boutton_y )   

    #bt de division
    bt_cotan = tkinter.Button(frame_touche,text="/",background='red',width=l,height=h,command=fonction_wdgets.div)
    bt_cotan.place(x= pas_boutton_x,y = 2*pas_boutton_y ) 
    
    #bt de multiplication
    bt_cotan = tkinter.Button(frame_touche,text="x",background='red',width=l,height=h,command=fonction_wdgets.mul)
    bt_cotan.place(x= 2*pas_boutton_x,y = 2*pas_boutton_y ) 
    
    #bt de delete
    bt_cotan = tkinter.Button(frame_touche,text="del",background='red',width=l,height=h)
    bt_cotan.place(x= 3*pas_boutton_x,y = 2*pas_boutton_y )

    #===============================================================================#
    #bt 7
    bt_cotan = tkinter.Button(frame_touche,text="7",background='red',width=l,height=h,command=fonction_wdgets.sept)
    bt_cotan.place(x= 0,y = 3*pas_boutton_y )  

    #bt 8
    bt_cotan = tkinter.Button(frame_touche,text="8",background='red',width=l,height=h,command=fonction_wdgets.huit)
    bt_cotan.place(x= pas_boutton_x,y = 3*pas_boutton_y )  
    
    #bt 9
    bt_cotan = tkinter.Button(frame_touche,text="9",background='red',width=l,height=h,command=fonction_wdgets.neuf)
    bt_cotan.place(x= 2*pas_boutton_x,y = 3*pas_boutton_y ) 

    #bt soustraction -
    bt_cotan = tkinter.Button(frame_touche,text="-",background='red',width=l,height=h,command=fonction_wdgets.moins)
    bt_cotan.place(x= 3*pas_boutton_x,y = 3*pas_boutton_y ) 

    #===============================================================================#
    #bt 4
    bt_cotan = tkinter.Button(frame_touche,text="4",background='red',width=l,height=h,command=fonction_wdgets.quatre)
    bt_cotan.place(x= 0,y = 4*pas_boutton_y )  

    #bt 5
    bt_cotan = tkinter.Button(frame_touche,text="5",background='red',width=l,height=h,command=fonction_wdgets.cinq)
    bt_cotan.place(x= pas_boutton_x,y = 4*pas_boutton_y )  

    #bt 6
    bt_cotan = tkinter.Button(frame_touche,text="6",background='red',width=l,height=h,command=fonction_wdgets.six)
    bt_cotan.place(x= 2*pas_boutton_x,y = 4*pas_boutton_y )  

    #bt +
    bt_cotan = tkinter.Button(frame_touche,text="+",background='red',width=l,height=h,command=fonction_wdgets.plus)
    bt_cotan.place(x= 3*pas_boutton_x,y = 4*pas_boutton_y )  

    #============================================================================#
    #bt 1
    bt_cotan = tkinter.Button(frame_touche,text="1",background='red',width=l,height=h,command=fonction_wdgets.un)
    bt_cotan.place(x= 0,y = 5*pas_boutton_y)  

    #bt 2
    bt_cotan = tkinter.Button(frame_touche,text="2",background='red',width=l,height=h,command=fonction_wdgets.deux)
    bt_cotan.place(x= pas_boutton_x,y = 5*pas_boutton_y) 

    #bt 3
    bt_cotan = tkinter.Button(frame_touche,text="3",background='red',width=l,height=h,command=fonction_wdgets.trois)
    bt_cotan.place(x= 2*pas_boutton_x,y = 5*pas_boutton_y) 

    #bt =
    bt_cotan = tkinter.Button(frame_touche,text="=",background='red',width=l,height=2*h+2,command=fonction_wdgets.egal)
    bt_cotan.place(x= 3*pas_boutton_x,y = 5*pas_boutton_y) 

    #============================================================================#
    #bt %
    bt_cotan = tkinter.Button(frame_touche,text="%",background='red',width=l,height=h)
    bt_cotan.place(x= 0,y = 6*pas_boutton_y )  

    #bt 0
    bt_cotan = tkinter.Button(frame_touche,text="0",background='red',width=l,height=h,command=fonction_wdgets.zero)
    bt_cotan.place(x= pas_boutton_x,y = 6*pas_boutton_y )  

    #bt ,
    bt_cotan = tkinter.Button(frame_touche,text=",",background='red',width=l,height=h)
    bt_cotan.place(x= 2*pas_boutton_x,y = 6*pas_boutton_y )

    #Text à afficher sur l'écran
    text = tkinter.Label(frame_ecran,text=fonction_wdgets.afficher_nombre(),width=18,height=2,font=("ubuntu",30))
    text.place(x=15,y=20)  
  
    app.mainloop()

if __name__ == '__main__':
    main()