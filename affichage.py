import projet
class affichage:
    def conjuguverbe(self,verb): 
        obconjug=projet.conjuguson()                                                #verb=input("entrer le verbe ")
        preverbe=obconjug.prepareverbe(verb)
        if  preverbe is not None:
            while 1 :
                print("entrer 1 pour conjuguer le verbe au present ")
                print("entrer 2 pour conjuguer le verbe au Futur ")
                print("entrer 3 pour  conjuguer le verbe au passe compose ? ")
                try:
                    i = int(input())
                    if i == 1:
                        print("je " +preverbe + "e")
                        print("tu " + preverbe+ "es")
                        print("il " + preverbe + "e")
                        print("nous " + preverbe + "ons")
                        print("vous " +  preverbe  + "ez")
                        print("ils " +  preverbe+ "ent")   
                        break
                    elif i == 2:
                        print("je " +  preverbe + "ai")
                        print("tu " + preverbe+ "as")
                        print("il " +  preverbe+ "a")
                        print("nous " +  preverbe + "ons")
                        print("vous " + preverbe + "ez")
                        print("ils " + preverbe + "ont")
                        break
                    elif i == 3:
                        print("j'ai " +  preverbe + "é")
                        print("tu as " +  preverbe+ "é")
                        print("il a " +  preverbe + "é")
                        print("nous avons " +  preverbe + "é")
                        print("vous avez " +  preverbe + "é")
                        print("ils ont " + preverbe + "é")
                        break
                except:
                    continue              
        else:
            print("pas de verbe")