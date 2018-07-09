from datetime import date, timedelta

current_date = date(1901, 1, 1)
end_date = date(2000, 12, 31)

count = 0

while current_date < end_date:
    if current_date.day == 1 and current_date.weekday() == 6:
        print(current_date, current_date.weekday())
        count += 1 

    current_date += timedelta(days = 1)

print(count)