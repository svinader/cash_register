#
# Kases aparāts
#
# 0.5pt pievienot jaunu preci - nosaukumu un cenu
#     0.5pt preces nosaukumam jābūt no 2 līdz 120 simboliem (jābūt validācijai, rādīt paziņojumu ja neder)
#     0.5pt preces cenai jābūt veselam skaitlim vai daļskaitlim ar vērtību no 0 līdz 9999 (jābūt validācijai, rādīt paziņojumu ja neder)
# 0.5pt dzēst preci pēc kārtas numura
# 0.5pt atcelt ievadu / iztukšot preču sarakstu
# 0.5pt piemērot atlaidi, ievadīt summu procentos
# 0.5pt samaksāt, ja iedota lielāka summa - izdrukāt atlikumu
# 0.5pt izdrukāt čeku uz ekrāna - preces nosaukumus un summas
#     0.5pt izdrukāt piemēroto atlaidi (ja ir)
#     0.5pt izdrukāt kopējo summu

# 1pt programmas stāvoklis tiek glabāts JSON faila un programmas sākumā tiek ielasīts un beigās saglabāts
# 1pt kodam ir jēdzīgi komentāri, pirms "if, for, while" koda konstrukcijam
# 1pt koda palaišanas brīdī nerādās kļūdas
# 1pt mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# 1pt izmaiņas saglabātas versiju vadības sistēmā Git, savs fork
#
# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
#

import json

check = []

with open('check.json', 'r') as openfile:
    check = json.load(openfile)


while True:
    print("\nMovie Tracker Menu:")
    print("1. Pievienot preci")
    print("2. Dzest preci")
    print("3. Piemērot atlaidi")
    print("4. Samaksat")
    print("5. Izdrukat čeku")
    print("6. Dzest čeku")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        product = {
            "nosaukums" : input("Enter preces nosaukumu : "),
            "price" : input("Enter preces cenu: "),
        }
        check.append(product)
        with open("check.json", "w") as outfile:
            json.dump(check, outfile)
        pass
        
    elif choice == "2":
        index = int(input("Enter the index of the price to remove: "))
        check.pop(index)
        pass
        
    elif choice == "3":
        print("Ievadit atlaide procentos(%)...")
        atlaide = int(input())
        pass

    elif choice == "4":
    
        pass

    elif choice == "5":
        print(check)
        pass
    
    elif choice == "6":
    
        pass

    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

with open("check.json", "w") as check_file:
    json.dump(check, check_file)