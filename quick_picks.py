import random


def main():
    picks = []
    rows = []
    get_pick(picks, rows)
    show_picks(picks)


def get_pick(picks, rows):
    pick_num = int(input("How many quick pick? "))
    for p in range(pick_num):
        for i in range(6):
            rows.append(random.randint(1, 45))
        picks.append(rows)
        rows = []


def show_picks(picks):
    for i in range(len(picks)):
        print(picks[i][0], picks[i][1], picks[i][2], picks[i][3], picks[i][4], picks[i][5])


main()
