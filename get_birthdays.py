from collections import defaultdict
from datetime import datetime

def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthdays = defaultdict(list)
    day_names = {
        0: "Monday", 
        1: "Tuesday", 
        2: "Wednesday", 
        3: "Thursday", 
        4: "Friday", 
        5: "Saturday", 
        6: "Sunday"}

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            day_of_week = birthday_this_year.weekday()

            if day_of_week == 5 or day_of_week == 6: 
                day_of_week = 0

            birthdays[day_of_week].append(name)

    for day, names in sorted(birthdays.items()):
        day_name = day_names[day]
        print(f"{day_name}: {', '.join(names)}")

if __name__ == "__main__":
    
    users = [
        {"name": "Tommy Duncan", "birthday": datetime(1970, 7, 12)},
        {"name": "Matthew Carpenter", "birthday": datetime(1984, 5, 10)},
        {"name": "Michael Hicks", "birthday": datetime(1979, 12, 31)},
        {"name": "Debra Hanson", "birthday": datetime(2002, 1, 1)},
        {"name": "Matthew Lee", "birthday": datetime(1994, 4, 2)},
        {"name": "Charles Morris", "birthday": datetime(1968, 8, 20)},
        {"name": "Tyler Williams", "birthday": datetime(1998, 4, 22)},
        {"name": "Christopher Swanson", "birthday": datetime(1964, 3, 1)},
        {"name": "Deborah Meadows", "birthday": datetime(1967, 2, 28)},
        {"name": "Jeremy Davis", "birthday": datetime(1979, 2, 28)}
    ]
    
    get_birthdays_per_week(users)
