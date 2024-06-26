Classes = {
    'Mathematics': {
        'MATH170-Calculus I': 4,
        'MATH190-Calculus II': 4,
        'MATH170-Precalculus': 4,
        'MATH135-Statistics': 4,
    },
    'Computer Science': {
        'CISS125-Computer and Information Security': 3,
        'CISS100-Introduction to Computing and Information Sciences': 4,
        'CISS110-Programming & Logic I': 4,
        'CISS120-Networking I - Introduction to Data Communication': 3,
        'CYBR306-Information Security Assurance': 3,
        'CINF100X-Information in 21st Century': 3,
        'CINF202-Intro to Data & Databases': 3,
        'CINF201-Intro to Web Technologies': 3,
        'CINF303-Intermediate Networking': 3,
        'CINF308-Programming for Informatics': 3,
        'CINF200-Research Methods Informatics': 3,
        'CINF465-Senior Capstone Informatics': 3,
        'CINF467-Tech-Based Community Support - Drone Lab': 3,
        'CINF468-Undergraduate Internship': 3,
    },
    'Engineering': {
        'ENGR120-Programming for Engineers': 3,
        'ENGR100-Engineering Graphics': 2,
        'ENGR110-Intro to Engineering Practices': 4,
        'ENGR540-Introduction to Ship Systems': 4,
    },
    'Science': {
        'CHEM101-General Chemistry I': 4,
        'PHYS101-Physics I': 4,
        'FSCI244-Digital Forensics': 4,
        'FSCI245-Forensic Science I': 4,
    },
    'Humanities': {
        'ENGL103-Freshman English II for Engineers (Technical Writing)': 3,
        'PSYC100-General Psychology': 3,
        'SOCL100-Sociology': 3,
        'HUMN201-World Lit & Culture I-II': 3,
        'ARTS100-The History of Art': 3,
    },
    'Miscellaneous': {
        'CINF305-Digital Project Management': 3,
        'CRJS101-Intro to Criminal Justice': 3,
        'LEAD101-Leadership & Maritime Experience': 1,
        'PS112-STCW Basic Training': 2,
        'CADD100-Topics in 2D AutoCAD': 4,
        'CADD110-Topics in 3D AutoCAD': 4,
    }
}

for category, classes in Classes.items():
    print(f"{category}:")
    for Class, Credits in classes.items():
        print(f"  {Class}: {Credits} credits")

def calculate_total_credits(classes_dict):
    total_credits = 0
    for category, classes in classes_dict.items():
        for Credits in classes.values():
            total_credits += Credits
    return total_credits

total_credits = calculate_total_credits(Classes)
print(f"Total credits: {total_credits}")
