found_secret = False

while not found_secret:
    answer = input("Enter a string: ")
    answer_length = len(answer)
    if answer_length >= 5 and answer_length < 7:
        print("You passed the first level!")
        a_random_number_from_user = int(input("Enter a number: "))
        while a_random_number_from_user >= -3:
            a_random_number_from_user = int(input("Enter a number: "))
        if a_random_number_from_user <= -15 and (a_random_number_from_user * 2) == -30:
            print("You got the right number!")
            a_big_step = input("Enter the correct answer: ")
            is_correct = True
            for i in range(len(a_big_step) - 1):
                if a_big_step[i] > a_big_step[i + 1]:
                    is_correct = False
            if not is_correct:
                print("You failed the final test. Don't give up! :((")
            else:
                print("Finally! Congratulations!")
                print("Here is your flag: LOGI{You_are_a_master_of_python!}")
                found_secret = True
        else:
            print("Give another try :((")
    else:
        print("Try another string :((")
