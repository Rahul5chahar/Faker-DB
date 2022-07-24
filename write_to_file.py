def main():
    Name = input("Enter Your Name : ")
    Email = input("Enter your Email: ")
    age = input("Enter you age: ")
    number=input("Enter your Number: ")
    
    
    def yes_or_no(question):
    reply = str(input( yes_or_no +' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    else:
        return False
    
    f = open('File.txt', 'w')
    f.write('Name: '+ Name)
    f.write("\n")
    f.write('Email: '+ Email)
    f.write("\n")
    f.write('Age: '+ age)
    f.write("\n")
    f.write('Number:'+ number)
    f.write("\n")
    f.close()

    







