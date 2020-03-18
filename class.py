class Tech:
    mentor=[]
    learner=[]
    stack=[]
    Time1=[]
    Time2=[]
    a=0
    time1=0
    time2=0
    name=""
    n=""
    
        
    def addStack(self,expertise):
        self.expertise=expertise
    def setMentorOrLearner(self,p):
         self.p=p
         if self.p == 'Mentor':
            while 1:
                print ("Enter your name and available time (from to till in railway time)")
                self.name=input()
                self.time1=input()
                self.time2=input()
                if float(self.time1) <= float(self.time2) and float(self.time2) <= 24.0 :
                    break
                else:
                    print("Entered value of time is wrong!")
            return(1)
         elif self.p == 'Learner':
            print ("Enter your name")
            self.n=input()
            return(0)
    def Learner(self):
        learner.append(self.n)
    def setAvailableTime(self):             
        self.mentor.append(self.name)
        self.Time1.append(self.time1)
        self.Time2.append(self.time2)
        self.stack.append(self.expertise)
         
    def getMentor(self,Stack,Time):
        self.Stack=Stack
        self.Time=Time
        l=len(self.mentor)
        print("The available mentor/mentors are:")
        for i in range(0,l):
            if self.stack[i] == self.Stack and float(self.Time) >= float(self.Time1[i]) and float(self.Time) <= float(self.Time2[i]):
                print(self.mentor[i])
                self.a+=1
        if self.a==0:
            print("Sorry no mentors available!")
ob=Tech()
print("collecting values")
while 1:
    print("Would you like to continue inputing: yes or no")
    c=input()
    if c=='yes':
        print ("Enter your area of interest :")
        e=input()
        ob.addStack(e)
        print ("Enter wheather you area Mentor or Learner:")
        pr=input()
        val=ob.setMentorOrLearner(pr)
        if(val==1):
            ob.setAvailableTime()
        elif(val==0):
            ob.Learner()
        else:
            print("Sorry wrong input!")
        
    elif c=='no':
        break
    else:
        print ("Wrong input!")
print ("Enter your interest and time")
Stack=input()
Time=input()
ob.getMentor(Stack,Time)
input()
        
        
        

            
