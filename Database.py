#["Freshman", "Sophomore", "Junior", "Senior"]

#["College of Agriculture and Natural Resources", "School of Architecture, Planning, and Preservation",
#                       "College of Arts and Humanities", "College of Behavioral and Social Sciences",
#                       "Robert H. Smith School of Business", "College of Computer, Mathematical and Natural Sciences",
#                       "College of Education", "A. James Clark School of Engineering", "Philip Merrill College of Journalism",
#                       "College of Information Studies", "School of Public Health", "School of Public Policy"]

#["2.8", "2.9", "3.0", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "3.8", "3.9", "4.0"]

#["None","Arabic", "French", "German", "Hindi", "Italian", "Japanese", "Korean", "Mandarin",
#                        "Portuguese", "Russian", "Spanish", "Vietnamese"]



#"Academic"     "Internship"

#"Resident Credit"      "Transfer Credit"

#["Africa - Central", "Africa - East", "Africa - North", "Africa - South", "Africa - West",
#                        "America - Central", "America - North", "America - South", "Asia - Central", "Asia - East",
#                        "Asia - South", "Asia - SouthEast","Asia - West", "Caribbean", "Europe - East",
#                        "Europe - North", "Europe - South", "Europe - West", "Middle East", "Oceania"]

#["$15000 - $20000", "$20000 - $25000", "$25000 - $30000", "$30000 - $35000", "$35000 - $40000",
#                        "$40000 - $45000", "$45000 - $50000", "$50000 - $55000", "$55000 - $60000"]

#["Apartment", "Campus", "Host"]

#"Cultural"     "Leisure"   "Athletic"      "Vocational"    "Educational"   "Volunteer"

#["Semester - Spring", "Semester - Summer", "Semester - Fall", "Semester - Winter", "Full Year"]


def data():
    study_abroad_dict = {
        "Clark-in-Madrid(Spain) - Semester": {
            "index":0,
            "year": ["Sophomore", "Junior", "Senior"],
            "school": ["A. James Clark School of Engineering"],
            "gpa": 3.0,
            "purpose": ["academic"],
            "region": ["Europe"],
            "seclang": ["Spanish"],
            "cost": 18650,
            "housing": ["Host", "Apartment"],
            "extra": ["organized trips","outdoor activities"],
            "length": ["Semester - Spring", "Semester - Fall"],
            "credit": ["transfer"]
            },
        "Global Entrepreneurship Semester in Seoul": {
            "index":0,
            "year": ["Sophomore", "Junior", "Senior"],
            "school": [],
            "gpa": 3.0,
            "purpose": ["internship"],
            "region": ["Asia"],
            "seclang": ["Korean"],
            "cost": 28629,
            "housing": ["Campus"],
            "extra": ["sports", "career development"],
            "length": ["Semester - Spring"],
            "credit": ["transfer","resident"]
        },
        "Maryland-in-Berlin(Germany) - Full Year": {
            "index":0,
            "year": ["Sophomore", "Junior", "Senior"],
            "school": [],
            "gpa": 3.0,
            "purpose": ["academic"],
            "region": ["Europe"],
            "seclang": ["German"],
            "cost": 33080,
            "housing": ["Host", "Apartment"],
            "extra": ["organized trips", "educational"],
            "length": ["Full Year"],
            "credit": ["transfer", "resident"]
        },
        "Maryland-in-Buenos-Aires(Argentina) - Semester": {
            "index": 0,
            "year": ["Sophomore", "Junior", "Senior"],
            "school": [],
            "gpa": 2.75,
            "purpose": ["academic"],
            "region": ["America"],
            "seclang": ["Spanish", "Portuguese"],
            "cost": 18370,
            "housing": ["Host"],
            "extra": ["outdoor activities", "sports", "career development"],
            "length": ["Semester - Spring"],
            "credit": ["transfer", "resident"]
        },
        "Maryland-in-Copenhagen(Denmark) - Full Year": {
            "index": 0,
            "year": ["Sophomore", "Junior", "Senior"],
            "school": [],
            "gpa": 3.0,
            "purpose": ["academic"],
            "region": ["Europe"],
            "seclang": [],
            "cost": 52990,
            "housing": ["Host", "Apartment"],
            "extra": ["outdoor activities", "sports"],
            "length": ["Full Year"],
            "credit": ["transfer", "resident"]
        },
        "Maryland-in-Florence(Italy) - Semester": {
            "index": 0,
            "year": ["Sophomore", "Junior", "Senior"],
            "school": [],
            "gpa": 2.75,
            "purpose": ["academic"],
            "region": ["Europe"],
            "seclang": ["Italian"],
            "cost": 20950,
            "housing": ["Apartment"],
            "extra": ["outdoor activities", "sports", "volunteer"],
            "length": ["Semester - Spring","Semester - Fall"],
            "credit": ["transfer", "resident"]
        },
        "Maryland-in-Nice(France) - Full Year": {
            "index": 0,
            "year": ["Sophomore", "Junior", "Senior"],
            "school": [],
            "gpa": 2.75,
            "purpose": ["academic"],
            "region": ["Europe"],
            "seclang": ["French"],
            "cost": 32790,
            "housing": ["Apartment", "Host"],
            "extra": ["organized trips"],
            "length": ["Full Year"],
            "credit": ["transfer", "resident"]
        },
        "BMGT Exchange: RMIT (Royal Melbourne Institute of Technology) (Australia)": {
            "index": 0,
            "year": ["Sophomore", "Junior", "Senior"],
            "school": ["Robert H. Smith School of Business"],
            "gpa": 3.0,
            "purpose": ["academic"],
            "region": ["Oceania"],
            "seclang": [],
            "cost": 31796,
            "housing": ["Apartment"],
            "extra": ["outdoor activities", "educational"],
            "length": ["Semester - Spring","Semester - Fall"],
            "credit": ["transfer"]
        },
        "University of Maryland Hong Kong Exchange": {
            "index": 0,
            "year": ["Sophomore", "Junior", "Senior"],
            "school": [],
            "gpa": 3.0,
            "purpose": ["academic"],
            "region": ["Asia"],
            "seclang": ["Chinese"],
            "cost": 25661,
            "housing": ["Campus"],
            "extra": ["organized trips", "educational"],
            "length": ["Semester - Spring", "Semester - Fall"],
            "credit": ["transfer"]
        },
    }
    return study_abroad_dict

