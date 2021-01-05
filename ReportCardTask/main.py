from reportcard import ReportCard
class Main:
    def main():
        rep=ReportCard()
        n=0
        print('Hello, welcome to Report card program')
        while n!=6:
            n=input('Enter one of the options:\n\
            1.Add a student to the report card list\n\
            2.Update the details of an existing student\n\
            3. Display the marks of an existing student\n\
            4. Display the top 10 students of the class\n\
            5. Display the students eligible for Scholar Badge\n\
            6. Exit the Report Card program\n')
            if(not(n>='1' and n<='6')):
                print('Invalid Input. Try again')
                continue
            n=int(n)
            if(n==1):
                rep.insert()
            if(n==2):
                rep.update()
            if(n==3):
                rep.displaymarksheet()
            if(n==4):
                rep.compute_ranks()
            if(n==5):
                rep.Merit_students()
        
    if __name__=='__main__':
        main()
