from Student import Student
from tabulate import tabulate
import csv
class ReportCard:
    
    def __init__(self):
        self.report=[]
        self.fields=['Name','Admission_Number','Roll_Number','Class','Science_Marks','Maths_Marks','Social_studies_marks','English_Marks']
        filewr=csv.DictWriter(open('Student_Details.csv','w',newline=''),fieldnames=self.fields)
        filewr.writeheader()
    report=[]
    
    
    
    def search_name(self,name):
        for j in self.report:
            if(j.Name==name):
                return j
        print('No such name found. Try again')
        return None
    
    
    
    def search_roll(self,roll):
        for j in self.report:
            if(j.Roll_Number==roll):
                return j
        print('No such roll_number found. Try again')
        return None
    
    
    
    def search_class(self,clas):
        for j in self.report:
            if(j.Class==clas):
                return j
        print('No such student with this Class found. Try again')
        return None
    
    
    
    def valid_Name(self):
        Name=input('Enter Name\n')
        for c in Name:
            if(not (c.isalpha() or c==' ')):
                print('Invalid Name. Try again')
                return self.valid_Name()
        return Name
    
    def valid_Class(self):
        Class=14
        while True:
            Class=input('Enter Class\n')
            #Assuming KG UN and LN and 1 to 12 are valid classes
            if(Class!='KG' and Class!='UN' and Class!='LN' and not(Class.isnumeric() and int(Class)>=1 and int(Class)<=12)):
                print('Invalid Class. Try again')
            else:
                break
        return Class
    
    def valid_Admission_Number(self):
        Admission_Number=input('Enter Admission Number\n')
        while not(Admission_Number.isnumeric()):
            print('Invalid Admission_Number. Try again')
            Admission_Number=input('Enter Admission Number\n')
        Admission_Number=int(Admission_Number)
        return Admission_Number

    def valid_Roll_Number(self):
        Roll_Number=input('Enter Roll Number\n')
        while not(Roll_Number.isnumeric()):
            print('Invalid Roll Number. Try again')
            Roll_Number=input('Enter Roll Number\n')
        Roll_Number=int(Roll_Number)
        return Roll_Number


    def valid_Maths_Marks(self):
        Maths_Marks=input('Enter Maths Marks\n')
        while not(Maths_Marks.isnumeric()) or int(Maths_Marks)<0 or int(Maths_Marks)>100:
            print('Invalid Maths Marks. Try again')
            return self.valid_Maths_Marks()
        Maths_Marks=int(Maths_Marks)
        return Maths_Marks
    
    def valid_Science_Marks(self):
        Science_Marks=input('Enter Science Marks\n')
        while not(Science_Marks.isnumeric()) or int(Science_Marks)<0 or int(Science_Marks)>100:
            print('Invalid Science Marks. Try again')
            return self.valid_Science_Marks()
        Science_Marks=int(Science_Marks)
        return Science_Marks

    def valid_social_studies_marks(self):
        Social_studies_marks=input('Enter Social Studies Marks\n')
        while not(Social_studies_marks.isnumeric()) or int(Social_studies_marks)<0 or int(Social_studies_marks)>100:
            print('Invalid Social studies Marks. Try again')
            return self.valid_social_studies_marks()
        Social_studies_marks=int(Social_studies_marks)
        return Social_studies_marks

    def valid_English_Marks(self):
        English_Marks=input('Enter English Marks\n')
        while not(English_Marks.isnumeric()) or int(English_Marks)<0 or int(English_Marks)>100 :
            print('Invalid English Marks. Try again')
            return self.valid_English_Marks()
        English_Marks=int(English_Marks)
        return English_Marks


    def insert(self):
        #Validating each input
        print('Enter the details')
        Name=self.valid_Name()
        Admission_Number=self.valid_Admission_Number()
        Roll_Number=self.valid_Roll_Number()
        Class=self.valid_Class()
        Science_Marks=self.valid_Science_Marks()
        Maths_Marks=self.valid_Maths_Marks()
        Social_studies_marks=self.valid_social_studies_marks()
        English_Marks=self.valid_English_Marks()
        details={'Name':Name,'Admission_Number':Admission_Number,'Roll_Number':Roll_Number,'Class':Class,
        'Science_Marks':Science_Marks,'Maths_Marks':Maths_Marks,'Social_studies_marks':Social_studies_marks,'English_Marks':English_Marks}
        filewr=csv.DictWriter(open('Student_Details.csv','a',newline=''),fieldnames=self.fields)
        filewr.writerow(details)
        self.report.append(Student(Name,Admission_Number,Roll_Number,Class,Science_Marks,Maths_Marks,Social_studies_marks,English_Marks))
        return 0
    
    
    
    def update(self):
        print('Choose How to search the student by:')
        print('1.Class\n2.Roll_Number\n3.Name')
        n=input()
        if(n=='1'):
            Class=self.valid_Class()
            s=self.search_class(Class)
        elif(n=='2'):
            Roll=self.valid_Roll_Number()
            s=self.search_roll(Roll)
        elif(n=='3'):
            Name=self.valid_Name()
            s=self.search_name(Name)
        else:
            print('Wrong option selected. Try again')
            self.update()
        
        if(s==None):
            self.update()
        i=1
        while i==1:
            print('Please select which detail to update:')
            print('\
            1. Name \n\
            2. Admission_Number\n\
            3. Roll_Number\n\
            4. Class\n\
            5. Science_Mark\n\
            6. Maths_Marks\n\
            7. Social_studies_marks\n\
            8. English_Marks\n')
            n=input()

            if(n=='1'):
                s.Name=self.valid_Name()
            elif(n=='2'):
                s.Admission_Number=self.valid_Admission_Number()
            elif(n=='3'):
                s.Roll_Number=self.valid_Roll_Number()
            elif(n=='4'):
                s.Class=self.valid_Class()
            elif(n=='5'):
                s.Science_Marks=self.valid_Science_Marks()
            elif(n=='6'):
                s.Maths_Marks=self.valid_Maths_Marks()
            elif(n=='7'):
                s.Social_studies_marks=self.valid_social_studies_marks()
            elif(n=='8'):
                s.English_Marks=self.valid_English_Marks()
            else:
                println('Invalid Input. Try again')
                continue
            i+=1
        s.Meritcheck()
        filewr=csv.DictWriter(open('Student_Details.csv','w',newline=''),fieldnames=self.fields)
        filewr.writeheader()
        for i in self.report:
            filewr.writerow({'Name':i.Name,'Admission_Number':i.Admission_Number,'Roll_Number':i.Roll_Number,'Class':i.Class,
            'Science_Marks':i.Science_Marks,'Maths_Marks':i.Maths_Marks,'Social_studies_marks':i.Social_studies_marks,'English_Marks':i.English_Marks})
    
    
    
    def comp(self,stud1):
        return stud1.Aggregate_Marks



    def displaymarksheet(self):
        print('Choose How to search the student by:')
        print('1.Class\n2.Roll_Number\n3.Name')
        n=input()
        if(n=='1'):
            Class=self.valid_Class()
            stud=self.search_class(Class)
        elif(n=='2'):
            Roll=self.valid_Roll_Number()
            stud=self.search_roll(Roll)
        elif(n=='3'):
            Name=self.valid_Name()
            stud=self.search_name(Name)
        else:
            print('Wrong option selected. Try again')
            self.displaymarksheet()
        
        if(stud==None):
            return self.displaymarksheet()
            
        headers=['Science','Maths','Social Studies','English']
        table=[[stud.Science_Marks,stud.Maths_Marks,stud.Social_studies_marks,stud.English_Marks]]
        print(tabulate(table,headers))
        return 0

    def compute_ranks(self):
        sortarr=sorted(self.report,reverse=True,key=self.comp)
        lim=min(10,len(sortarr))
        header=["Name","Aggregate marks"]
        table=[]
        for i in range(lim):
            temp=[]
            temp.append(sortarr[i].Name)
            temp.append(sortarr[i].Aggregate_Marks)
            table.append(temp)
        print(tabulate(table,header))



    def Merit_students(self):
        header=['Names eligible for Scholar Badge']
        table=[]
        for student in self.report:
            row=[]
            if(student.Merit):
                row.append(student.Name)
            table.append(row)
        print(tabulate(table,header))
