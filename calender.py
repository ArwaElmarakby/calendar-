import calendar
import datetime

def display_calendar():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))


    cal = calendar.monthcalendar(year, month)


    month_name = calendar.month_name[month]


    print(f"\n{month_name} {year}")
    print("Mo Tu We Th Fr Sa Su")


    for week in cal:
        for day in week:
            if day == 0:
                print("  ", end=" ")
            else:
                print(f"{day:2d}", end=" ")
        print()


    today = datetime.date.today()
    print(f"\nToday's date: {today.strftime('%B %d, %Y')}")


display_calendar()
