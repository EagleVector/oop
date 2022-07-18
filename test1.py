class Person:
    def calculate_age(self, current_year):
        dob_year = int(input("Enter your date of birth year: "))
        age = current_year - dob_year
        return age

    def ask_name(self):
        name = input("Enter your name: ")
        return name

    def ask_email(self, email_id):
        return email_id

sudh = Person()
hitesh = Person()
krish = Person()
shubham = Person()

print(sudh.calculate_age(2022))