#python -m venv venv
#py -m venv venv
#pip install pandas
#python -m pip install pandas
    
#venv\Scripts\activate
#pip install pandas

#Java vs Python:

#Java:
#int age = 25;
#String name = "Alice";

#if  (age > 18){
#    System.out.println(name);
#    }else{
#        System.out.println("Not eligible");
#    }

#Python:
age = 25
name = "Alice"

if age > 18:
     print(name)
else:
     print("Not eligible")


#Java workflow: Write --> Compile --> Run (3 steps)
#Python workflow: Write --> Run (2 steps, instant testing!)

#Java:
#Source Code (.java)
#Compile (javac)
#Bytecode (.class)
#RUN (java)
#Output

#Python:
#Source Code (.py)
#RUN (python)
#Output

import sys
a = 2
a = 3
print(type(a))
print(a)
print(sys.getsizeof(a))

a = 2.3
print(type(a))
print(a)
print(sys.getsizeof(a))

a="hello"
print(type(a))
print(a)
print(sys.getsizeof(a))

a=True
print(type(a))
print(a)
print(sys.getsizeof(a))


år = 2026

while True:
    name = input("Hva er navnet ditt? ")


    if name == "" or name == " ":
        print("Du må skrive inn et navn. ")
    else:
        print(f"Så du heter {name}? ")
        print("For et fint navn! ")
        break


while True:
    alder = input("Hvor gammel er du? ")


    if alder == "" or alder == " ":
        print("Du må skrive inn et tall. ")
        continue
    
    try:
        alder = int (alder)
        print(f"Så du er {alder}? ")
        break

    except ValueError:
        print ("Du må skrive inn et tall. ")


født = int (år) - int (alder)
print (f"Du heter {name} og du er {alder} år gammel. Du er da født i {født}")

#Endring