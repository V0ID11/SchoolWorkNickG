name_list = ['John', 'Luka', 'Matei', 'Josh', 'Eric', 'Alex', 'Ryan', 'Isaac', 'Nikita', 'Thomas', 'Theo', 'Owen']
scores_list = [[] for i in name_list]           # Create a lists of empty lists


def add_scores():
    name = input("Enter name: ") #takes the name of the person you want to find scores of
    name_index = name_list.index(name) #find the poistion of the name in the name_list
    new_score = int(input("Enter score: ")) 
    scores_list[name_index].append(new_score) #add to the position in scores_list the new score
    display_scores(name_index) 


def display_scores(pupil_index):
    print("Scores for", name_list[pupil_index], ":", end=" ") #display the name of the student whose scores will be printed
    for score in scores_list[pupil_index]: 
        print(score, end=" ") #print each score in scores_list without any new lines
    print("")


def display_all_scores():
    for pupil_index in range(len(name_list)): #takes each index and runs through display_scores
        display_scores(pupil_index)

    total_points = 0
    total_scores = 0
    for scores in scores_list:
        total_points += sum(scores) #for each index take the total of all the scores and the length
        total_scores += len(scores)
    print("Total points for class: ", total_points) 
    print("Average for class: ", total_points / total_scores) #create average of the scores

#display menu to allow choice from user
def menu():
    while True:
        print(""" What would you like to do?
        1. Add a new score
        2. Display all scores
        3. Exit""")
        menu_choice = int(input(":"))
        if menu_choice == 1:
            add_scores()
        elif menu_choice == 2:
            display_all_scores()
        elif menu_choice == 3:
            break

menu()
