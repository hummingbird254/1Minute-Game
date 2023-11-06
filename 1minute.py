import time, logging, secrets
from faker import Faker

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

intro = input(
    "Welcome to the 1 minute game where you finesse your ability to describe things properly. Type 'NO' to quit game. Click 'ENTER to continue.").lower()

if intro == 'no':
    quit("Goodbye!")

group_prompt = input("How many groups do we have?")
grp_num = int(group_prompt)
groups = {}
already_asked = []


def main(grp_num, groups):
    for x in range(1, grp_num + 1):
        player1 = input(f"Enter the name of the 1st player for Group {x}.")
        player2 = input(f"Enter the name of the 2nd player for Group {x}.")
        groups[x] = [player1, player2]

    fake = Faker()

    while True:
        check = input("Type 'quit' to exit.").lower()
        if check == "quit":
            break

        for x in [0, 1]:
            for keys in groups.keys():
                print(f"Group {keys} I hope you're ready!")

                print(
                    f"{groups[keys][x]} you are the current player. Try and describe these words properly for you group partner.")
                time.sleep(3)
                for v in range(5):
                    r = fake.word()
                    if r not in already_asked:
                        print(r)

                    already_asked.append(r)
                time.sleep(30)
                marks = int(input("How many did you get correct?"))
                groups[keys].append(marks)



def calc_marks(groups):
    total = 0
    print(groups)
    for keys in groups.keys():
        for items in groups[keys][2:]:
            total = total + items
        print(f"GROUP {keys} has {total} points.")
        total = 0

main(grp_num, groups)
calc_marks(groups)



