class Student:
    def __init__(self,name='',adm=0,roll=0,clas=0,science=0,maths=0,social=0,english=0):
        self.Name=name
        self.Admission_Number=adm
        self.Roll_Number=roll
        self.Class=clas
        self.Science_Marks=science
        self.Maths_Marks=maths
        self.Social_studies_marks=social
        self.English_Marks=english
        self.Aggregate_Marks=(self.Science_Marks+self.Maths_Marks+self.Social_studies_marks+self.English_Marks)/4
        self.Meritcheck()
    def Meritcheck(self):
        self.Merit=False
        if(self.Science_Marks>90 and self.Maths_Marks>90 and self.Social_studies_marks>90 and self.English_Marks>90):
            self.Merit=True
    def marks_table(self):
        return (self.Science_Marks+"\t"+self.Maths_Marks+"\t"+self.Social_studies_marks+"\t"+self.English_Marks+"\t")
    def __str__(self):
        print(self.Name)
    # Roll_Number=input()
    # Class=input()
    # Science_Marks=input()
    # Maths_Marks=input()
    # Social_studies_marks=input()
    # English_Marks=input()
    
