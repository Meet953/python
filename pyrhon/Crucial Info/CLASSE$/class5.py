# TO CREATE A CLASS OF BOWLERS IN ICG_FRIENDLY_CUP AND DISPLAY THE RECORDS....
class housing:
    print"\n\t\t\t WELC0ME T0 THE LIST OF THE BEST HOUSES.\t\t\t\n"
    def __init__(self,n=" ",ob=0,nom=0,rg=0,wt=0,c=" "):
        self.n=n          # NAME OF PLAYER.
        self.ob=ob        # OVERS BOWLED.
        self.nom=nom     # NO_OF_MAIDIN_OVERS .
        self.rg=rg         # RUNS GIVEN.
        self.wt=wt         # WICKETS TAKEN.
        self.c=c           # COUNTRY.
    def cricket_team(self):
        if self.wt>=50:
            print self.n,"has been awarded the BOWLER OF THE SERIES for taking",self.wt,"wickets."
        else:
            pass
    def __str__(self):
        return"Name of the player:"+str(self.n)+" || "+"Overs bowled:"+str(self.ob)+" || "+"No_of_maidin_overs:"+str(self.nom)+" || "+"Runs given:"+str(self.rg)+" || "+"Wickets Taken:"+str(self.wt)+" || "+"Country --->"+str(self.c)
# ----main----
b1=housing("Yuvraj Singh",40,5,125,50,"INDIA")
b2=housing("Suresh Raina",30,7,75,5,"INDIA")
b3=housing("Irfan Pathan",50,6,185,57,"INDIA")
b4=housing("Tom Horan",30,0,193,3,"NEPAL")
b1.cricket_team()
b2.cricket_team()
b3.cricket_team()
b4.cricket_team()
print"\n\t\t\t THE DATABASE OF THE BOWLERS IS AS FOLLOWS ---> \t\t\n"
print b1
print b2
print b3
print b4

        
