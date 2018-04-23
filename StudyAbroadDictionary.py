study_abroad_dict = {
    1: {
        'academic_year_requirements': ['sophomore', 'junior', 'senior'], 
        'major_requirements': ['Bioengineering', 'Chemical Engineering', 'Civil Engineering', 'Computer Engineering',
                             'Computer Science', 'Electrical Engineering', 'Fire Protection Engineering',
                             'Materials Science & Engineering', 'Mechanical Engineering'],
        'minimum_GPA': 3.0,
        'purpose': 'academic',
        'region': ['Madrid', 'Spain', 'Europe'],
        'second_languages': ['Spanish'],
        'cost': (17050, 18650),
        'housing': ['host', 'apartment'],
        'extracurricular': [],
        'program_season': ['Fall', 'Spring'],
        'program_duration': 'semester',
        'credits': ['transfer']
        },
    3: {
        'academic_year_requirements': ['sophomore', 'junior', 'senior'],
        'major_requirements': [],
        'minimum_GPA': 3.0,
        'purpose': 'internship',
        'region': ['Seoul', 'South Korea', 'Asia'],
        'second_languages': ['Korean'],
        'cost': (17025.50, 28629),
        'housing': ['dorm'],
        'extracurricular': ['aquatic sports','career development'],
        'program_season': ['Spring'],
        'program_duration': 'semester',
        'credits': ['transfer', 'resident']
        }
}

study_abroad_locations = {
    1: 'Clark-in-Madrid (Spain) - Semester',
    2: 'Clark-in-Madrid (Spain) - Full Year',
    3: 'Global Entrepreneurship Semester in Seoul',
    4: 'Maryland-in-Berlin (Germany) - Semester',
    5: 'Maryland-in-Berlin (Germany) - Full Year'
}

# accessing full program name of key
for k in study_abroad_dict: 
    print(study_abroad_locations[k])

print()

# accessing a row
print(study_abroad_dict[1])

print() 

# accessing a cell
print(study_abroad_dict[1]['academic_year_requirements'])
