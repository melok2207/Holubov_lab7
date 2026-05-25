import csv
import random
from faker import Faker
from datetime import datetime

fake = Faker('uk_UA')

male_patronymics = [
    "Олексійович", "Віталійович", "Михайлович", "Артемович",
    "Євгенович", "Русланович", "Вікторович", "Петрович",
    "Іванович", "Максимович", "Андрійович", "Богданович",
    "Сергійович", "Володимирович", "Олегович", "Тарасович",
    "Юрійович", "Денисович", "Павлович", "Степанович"
]

female_patronymics = [
    "Олексіївна", "Віталіївна", "Михайлівна", "Артемівна",
    "Євгенівна", "Русланівна", "Вікторівна", "Петрівна",
    "Іванівна", "Максимівна", "Андріївна", "Богданівна",
    "Сергіївна", "Володимирівна", "Олегівна", "Тарасівна",
    "Юріївна", "Денисівна", "Павлівна", "Степанівна"
]

jobs = [
    "Тестувальник",
    "Системний адміністратор",
    "DevOps інженер",
    "UI/UX дизайнер",
    "Аналітик",
    "Backend розробник"
]

with open("employees.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Прізвище",
        "Ім'я",
        "По батькові",
        "Стать",
        "Дата народження",
        "Посада",
        "Місто",
        "Адреса",
        "Телефон",
        "Email"
    ])

    for i in range(550):

        gender = random.choices(
            ["Чоловіча", "Жіноча"],
            weights=[60, 40]
        )[0]

        if gender == "Жіноча":
            last_name = fake.last_name_female()
            first_name = fake.first_name_female()
            patronymic = random.choice(female_patronymics)
        else:
            last_name = fake.last_name_male()
            first_name = fake.first_name_male()
            patronymic = random.choice(male_patronymics)

        birth_date = fake.date_between(
            start_date=datetime(1946, 1, 1),
            end_date=datetime(2011, 12, 31)
        )

        writer.writerow([
            last_name,
            first_name,
            patronymic,
            gender,
            birth_date.strftime("%d.%m.%Y"),
            random.choice(jobs),
            fake.city(),
            fake.address().replace("\n", " "),
            fake.phone_number(),
            fake.email()
        ])

print("Ok")