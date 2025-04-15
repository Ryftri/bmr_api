def calculate_bmr_mifflin(data):
    weight = data.get('weight')
    height = data.get('height')
    age = data.get('age')
    gender = data.get('gender')

    if gender == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    return {"bmr": round(bmr, 2)}

def calculate_bmr_harris_original(data):
    weight = data.get('weight')
    height = data.get('height')
    age = data.get('age')
    gender = data.get('gender')

    if gender == "male":
        bmr = 66.5 + (13.75 * weight) + (5.003 * height) - (6.75 * age)
    else:
        bmr = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)

    return {"bmr": round(bmr, 2)}

def calculate_bmr_harris_revised(data):
    weight = data.get('weight')
    height = data.get('height')
    age = data.get('age')
    gender = data.get('gender')

    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    return {"bmr": round(bmr, 2)}
