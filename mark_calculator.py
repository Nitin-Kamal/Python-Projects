subjects = ['English', 'Maths','Science','Social science','Computer']
Addsub = input(F"The existing subjects are {subjects}. Would you like to add more(yes or no): ")
if Addsub.upper() == "YES":
    Addsub2 = int(input('How many subjects do you want to add(in numbers): '))
    i = 0
    while i < Addsub2:
        i = i + 1
        Addsub1 = input('What subject do you want to add(One by one): ')
        subjects.append(Addsub1)
        print(subjects)
marks = int(input('How much marks does each of these subjects contain: '))
len_of_subjects = len(subjects)
a = 0
total_marks = marks * len_of_subjects
print(f"Total marks is {total_marks}")
fail_mark = int(input('what is the fail mark: '))
subjects_list = ''
for_100 = ''
for_100_2 = ''
fail_notice = ''
total_marks2 = 0
for700 = 0
while a < len_of_subjects:
    subjects_list = subjects[a]
    get_mark = int(input(f'How much marks did you get in {subjects_list}: '))
    total_marks2 = total_marks2 + get_mark
    if get_mark < fail_mark:
        fail_notice = 'You are fail in this subject. Study well and better luck next time'
    else:
        fail_notice = 'You have passed in this subject! Congratulations.'
    for_100 = get_mark / marks
    for_100_2 = for_100 * 100
    for700 = for700 + for_100_2
    print(f"""Your mark for {subjects_list} is {get_mark}/{marks}
    Your {subjects_list} for 100 is {for_100_2}/100
    {fail_notice}""")
    a = a + 1
total_for100 = total_marks2 / total_marks
total_for100_2 = total_for100 * 100
total_for100_3 = len_of_subjects * 100
print(f"""You got {total_marks2} out of {total_marks}
      in percent it is {total_for100_2}%/100%
      or {for700}/{total_for100_3}""")
print('Congratulations for your next exams')