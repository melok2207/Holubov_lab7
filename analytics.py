import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

try:
    df = pd.read_csv("employees.csv")
    print("Ok")

except:
    print("Помилка відкриття CSV файлу")
    exit()


def calculate_age(date):
    birth = datetime.strptime(date, "%d.%m.%Y")
    today = datetime.today()

    return today.year - birth.year - (
        (today.month, today.day) < (birth.month, birth.day)
    )


df["Вік"] = df["Дата народження"].apply(calculate_age)

# Кількість чоловіків та жінок
gender_count = df["Стать"].value_counts()

print("Кількість працівників за статтю:")
print(gender_count)

gender_count.plot(kind="bar")
plt.title("Працівники за статтю")
plt.xlabel("Стать")
plt.ylabel("Кількість")
plt.show()

# Вікові категорії
age_categories = {
    "younger_18": len(df[df["Вік"] < 18]),
    "18-45": len(df[(df["Вік"] >= 18) & (df["Вік"] < 45)]),
    "45-70": len(df[(df["Вік"] >= 45) & (df["Вік"] < 70)]),
    "older_70": len(df[df["Вік"] >= 70])
}

print("\nКількість працівників за віковими категоріями:")
print(age_categories)

plt.bar(age_categories.keys(), age_categories.values())
plt.title("Вікові категорії")
plt.xlabel("Категорія")
plt.ylabel("Кількість")
plt.show()

# Стать у кожній віковій категорії
for category in age_categories.keys():

    if category == "younger_18":
        temp = df[df["Вік"] < 18]

    elif category == "18-45":
        temp = df[(df["Вік"] >= 18) & (df["Вік"] < 45)]

    elif category == "45-70":
        temp = df[(df["Вік"] >= 45) & (df["Вік"] < 70)]

    else:
        temp = df[df["Вік"] >= 70]

    data = temp["Стать"].value_counts()

    print(f"\n{category}")
    print(data)

    data.plot(kind="bar")

    plt.title(f"Стать у категорії {category}")
    plt.xlabel("Стать")
    plt.ylabel("Кількість")

    plt.show()