"""
{
    "a": [
        {},
        {},
        {}
    ]
}
"student" :
[


"students_emails": {
    "John Smith": "john.smith@example.com","age":22
    "Emma Johnson": "emma.johnson@example.com",
    "Michael Lee": "michael.lee@example.com",
    "Sophia Wang": "sophia.wang@example.com"} ]
"""
contacts = {
    "count" : 4,
    "students": [
        {"name": "John Smith", "age": 22, "email": "john.smith@example.com"},
        {"name": "Emma Johnson", "age": 20, "email":"emma.johnson@example.com"},
        {"name": "Michael Lee", "age": 25, "email": "michael.lee@example.com"},
        {"name": "Sophia Wang", "age": 19, "email": "sophia.wang@example.com"}
    ]
}
print("sr number\t| name\t| age\t| email")
print('-'*40)
# contacts["students"]['name']
for i in range(1,contacts["count"]+1, 1):
    print(f"{i}| {contacts['students'][i-1]['name'] }")
# for key, value in contacts.items():
#     print(f"{key.count()}\t\t |{age}\t\t {email}")

"""
sr number | name | age | email
1 | John | 22 | @

"""
