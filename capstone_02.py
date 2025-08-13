all_lists = {
    'G10': [
        {'id': '1100', 'name': 'MANDY', 'grade': '10A', 'gender': 'F', 'score': '85'},
        {'id': '1101', 'name': 'NICOLE', 'grade': '10B', 'gender': 'F', 'score': '92'},
        {'id': '1102', 'name': 'BOB', 'grade': '10C', 'gender': 'M', 'score': '78'}
    ],
    'G11': [
        {'id': '1110', 'name': 'ALICE', 'grade': '11A', 'gender': 'F', 'score': '88'},
        {'id': '1111', 'name': 'JOHN', 'grade': '11B', 'gender': 'M', 'score': '90'},
        {'id': '1112', 'name': 'EMMA', 'grade': '11C', 'gender': 'F', 'score': '95'}
    ],
    'G12':[
        {'id': '1120', 'name': 'KELLY', 'grade': '12A', 'gender': 'F', 'score': '99'}   
    ]
}
homepage = [ '\tHOME PAGE',
            ' 1. Read Score List',
            ' 2. Add Score List',
            ' 3. Edit Score List',
            ' 4. Delete Score List',
            ' 5. Exit'
]
students = []
list_name = ""
read = ['\t READ SCORE LIST',
        ' 1. Read List',
        ' 2. Read Specific Data',
        ' 3. Back to Home Page'
]
add = ['\tADD SCORE LIST',
       ' 1. Add Score',
       ' 2. Back to Home Page'
]
edit = ['\tEDIT SCORE LIST',
        ' 1. Edit List',
        ' 2. Back to Home Page'
]
delete = ['\tDELETE SOCRE LIST',
          ' 1. Delete Specific Data',
          ' 2. Back to Home Page'
]
def invalid():
    print ('Inavlid Choice. Try Again')
    
def show_all_lists():
    if not all_lists:
        print("No lists available.")
        return False
    
    print("\nAvailable lists:")
    count = 1
    for list_name in all_lists:
        student_count = len(all_lists[list_name])
        print(f"{count}. {list_name} ({student_count} students)")
        count += 1
    return True
def select_list():
   
    while True:
        if not show_all_lists():
            return None, None
        
        choice = int(input("Select list number: ")) - 1
        list_names = list(all_lists.keys())
        if 0 <= choice < len(list_names):
            if len(all_lists[list_names[choice]]) == 0:
                print ('No student in the list.')
                continue
            selected_name = list_names[choice]
            return selected_name, all_lists[selected_name]
        else:
            print("Invalid selection. Please try again.")
            continue

def get_student_data():
    """Get student information from user"""
    student_id = input('SID: ')
    name = input('Name: ').upper()
    grade = input('Class: ').upper()
    
    # Get valid gender
    while True:
        gender = input('Gender (M/F): ').upper()
        if gender in ['M', 'F']:
            break
        print("Please enter 'M' or 'F' only.")
    
    # Get valid score
    while True:
        try:
            score = input('Score: ')
            float(score) 
            break
        except:
            print("Please enter a valid number for score.")
    
    return {
        'id': student_id,      
        'name': name,         
        'grade': grade,        
        'gender': gender,      
        'score': score        
    }

def find_student(students, student_id):
    for i, student in enumerate(students):
        if student['id'] == student_id:
            return i, student
    return -1, None

def continue_choice():
    while True:
        choice = input('Would you like to continue? (Y/N): ').upper()
        if choice in ['Y', 'N']:
            return choice
        invalid()
while True:
    for h in homepage:
        print(h)
    choice_h = input ('Please Select a Menu:')

##READ
    if choice_h == '1':
       while True:
            for r in read:
                print (r)
            choice_r = input('Please Select a Menu:')
            if choice_r == '1':
                list_name, students = select_list()
                if list_name:
                    for student in students:
                        print(f"""SID: {student['id']}, 
Name: {student['name']}
Grade: {student['grade']}
Gender: {student['gender']}
Score: {student['score']}""")
                        print('-'*50)

            elif choice_r == '2':
                list_name, students = select_list()
                if list_name:
                    while True:
                        search_id = input('Enter Student ID: ')
                        index, student = find_student(students, search_id)
                        
                        if student:
                            print(f"\nStudent found in '{list_name}':")
                            print(f"ID: {student['id']}")
                            print(f"Name: {student['name']}")
                            print(f"Grade: {student['grade']}")
                            print(f"Gender: {student['gender']}")
                            print(f"Score: {student['score']}")
                        else:
                            print("Student not found.")
                        if continue_choice() == 'N':
                            break
            elif choice_r == '3':
                break
            else:
                print ('Invalid Choice. Try Again')
     
##ADD
    elif choice_h == '2':
        while True:
            for a in add:
                print (a)
            choice_a = input('Please Select a Menu:')
            if choice_a == '1':
                list_name, students = select_list()
                if list_name:
                    while True:
                        print(f"Adding to: {list_name}")
                        student = get_student_data()
                        all_lists[list_name].append(student)
                        print("Student added!")
                        
                        if continue_choice() == 'N':
                            break
            elif choice_a == '2':
                break
            else:
                print ('Invalid Choice. Try Again')
 
##EDIT
    elif choice_h == '3':
        while True:
            for e in edit:
                print (e)
            choice_e = input('Please Select a Menu:')
            if choice_e == '1':
                list_name, students = select_list()
                if list_name:
                    search_id = input('Enter Student ID to edit: ')
                    index, student = find_student(students, search_id)
                    
                    if student:
                        print(f"\nEditing {student['name']}:")
                        print("1. Name  2. Grade  3. Gender  4. Score")
                        edit_what = input("Edit what? ")
                        
                        if edit_what == '1':
                            all_lists[list_name][index]['name'] = input('New Name: ').upper()
                        elif edit_what == '2':
                            all_lists[list_name][index]['grade'] = input('New Grade: ').upper()
                        elif edit_what == '3':
                            while True:
                                gender = input('New Gender (M/F): ').upper()
                                if gender in ['M', 'F']:
                                    all_lists[list_name][index]['gender'] = gender
                                    break
                        elif edit_what == '4':
                            while True:
                                try:
                                    score = input('New Score: ')
                                    float(score)
                                    all_lists[list_name][index]['score'] = score
                                    break
                                except:
                                    print("Enter valid number")
                        print("Updated!")
                        print(f"List '{list_name}' saved!")
                        break
                    else:
                        print("Student not found.")
            elif choice_e == '2':
                break
            else:
                print ('Invalid Choice. Try Again')
        
##DELETE
    elif choice_h == '4':   
        while True:
            for d in delete:
                print (d)
            choice_d = input('Please Select a Menu:')
            if choice_d == '1':
                    list_name, students = select_list()
                    while True:
                        if list_name:
                            search_id = input('Student ID to delete: ')
                            index, student = find_student(students, search_id)
                    
                            if student:
                                while True:
                                    confirm = input(f"Delete {student['name']}? (Y/N): ").upper()
                                    if confirm == 'Y':
                                        all_lists[list_name].pop(index)
                                        print("Student deleted!")
                                        break
                                    elif confirm == 'N':
                                        print ('Delete Canceled')
                                        break
                                    else:
                                        print ('Please choose only Y or N')
                                break   
                            else:
                                print('Student not found')
            elif choice_d == '2':
                break
            else:
                print ('Invalid Choice. Try Again')
##EXIT
    elif choice_h == '5':
        break
##ELSE
    else:
        print ('Invalid Choice. Try Again')