from collections import defaultdict
from datetime import datetime, timedelta, date


def get_birthdays_per_week(users):

    birthdays = defaultdict(list)

    current_date = date.today()

    days_list = []

    this_week_birthdays = []

    week = current_date + timedelta(weeks=1)

    for user in users:
        days_list.append(user['birthday'])

    for day in days_list:
        new_day = day.replace(year=current_date.year)

        if new_day < current_date:
            new_day = new_day.replace(year=new_day.year+1)

        if week >= new_day >= current_date:
            this_week_birthdays.append(day)

    for d in this_week_birthdays:
        new_d = d.replace(year=current_date.year)

        for user in users:

            if user['birthday'] == d:

                name = user['name']
                key = datetime.strftime(new_d, '%A')

                if key == 'Sunday' or key == 'Saturday':
                    birthdays['Monday'].append(name)

                else:
                    birthdays[key].append(name)

    return birthdays


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
