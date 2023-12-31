import csv
import collections

def main():
    # Считаем общее количество посещений из файла, пол и возраст
    visits = []
    genders = {}
    ages = []

    with open('medsi.csv', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            lst = row[0].split(';')
            visits.append(lst[2]) # Посещения
            ages.append(lst[3]) # Возраста
            genders[lst[2]] = lst[4] # Пол

    # Не учитываем оглавление файла
    visits.pop(0)
    ages.pop(0)
    ages = [int(i) for i in ages]
    del genders['PatientKey']

    # Посчитываем для каждого пациента сколько раз он посещал мед. учереждение
    res = collections.Counter(visits)
    
    print(f'Всего посещений: {len(visits)}')
    print(f'Всего пациентов: {len(res)}')
    
    # Пол пациентов
    women = list(genders.values()).count("1") / len(genders) * 100
    men = 100 - women
    print(f'Женщин: {round(women, 3)}%, Мужчин: {round(men, 3)}%')
    
    # Возраста пациентов
    print(f'В данных содежится информация людей от {min(ages) // 365} до {max(ages) // 365} лет')
    # До 20 лет
    ages_to_20 = [i for i in ages if i // 365 <= 20]
    print(f'В возрасте до 20 лет - {round(len(ages_to_20) / len(ages) * 100, 3)}%')
    # От 21 до 40
    ages_to_20_40 = [i for i in ages if 20 < i // 365 <= 40]
    print(f'В возрасте от 21 до 40 лет - {round(len(ages_to_20_40) / len(ages) * 100, 3)}%')
    # От 41 до 60
    ages_to_40_60 = [i for i in ages if 40 < i // 365 <= 60]
    print(f'В возрасте от 41 до 60 лет - {round(len(ages_to_40_60) / len(ages) * 100, 3)}%')
    # От 61 до 80
    ages_to_60_80 = [i for i in ages if 60 < i // 365 <= 80]
    print(f'В возрасте от 61 до 80 лет - {round(len(ages_to_60_80) / len(ages) * 100, 3)}%')
    # От 81
    ages_to_80 = [i for i in ages if 80 < i // 365]
    print(f'В возрасте от 80 лет - {round(len(ages_to_80) / len(ages) * 100, 3)}%')
    

    # Для удобства подготовим список количества посещений
    count_visits = []
    for i in res.values():
        count_visits.append(i)

    # Считаем в процентом соотношении по сколько раз обращались в мед учереждение
    for i in set(count_visits):
        print(f'Посещали: {i} раз {round(count_visits.count(i) / len(count_visits) * 100, 3)}% пациентов.')

main()
