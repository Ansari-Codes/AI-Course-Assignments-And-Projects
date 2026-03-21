'''
This Python file is for Task 01, stated as:

- Create a Python program that takes user input (a question or topic).
- Use if/else conditions to categorize the input into Technology, Education, or General
Knowledge.
- Print a custom response based on the detected category.
'''

#########################################
## STEP 1: Import required library (s) ##
## Which is only `string` in our case! ##
#########################################

import string

##########################################
## STEP 2: Define list of related words ##
##########################################

tech_related_words = [
    "algorithm",
    "programming",
    "python",
    "database",
    "network",
    "server",
    "cloud",
    "machine learning",
    "artificial intelligence",
    "encryption",
    "API",
    "framework",
    "compiler",
    "debugging",
    "cybersecurity",
    "blockchain",
    "data science",
    "automation",
    "robotics",
    "virtualization"
]

edu_related_words = [
    "school",
    "university",
    "student",
    "teacher",
    "curriculum",
    "lecture",
    "homework",
    "assignment",
    "exam",
    "research",
    "scholarship",
    "learning",
    "education",
    "classroom",
    "study",
    "knowledge",
    "training",
    "academic",
    "discipline",
    "degree"
]

gk_related_words = [
    "history",
    "geography",
    "politics",
    "economics",
    "culture",
    "science",
    "environment",
    "population",
    "government",
    "continent",
    "country",
    "capital",
    "currency",
    "climate",
    "ocean",
    "planet",
    "universe",
    "civilization",
    "tradition",
    "society"
]

#####################################################
## STEP 3: Replace puncuation for clear word split ##
#####################################################

def replace_punctuation(query):
    q = ''
    for i in query:
        if i.isspace():
            q += ' '
        elif i in string.punctuation:
            continue
        else:
            q += i
    return q

###########################################
## STEP 4: Create category word countrer ##
###########################################

def count_categories(query):
    cat_counts = {
        "tech": 0,
        "edu": 0,
        "gk": 0
    }

    for w in query.split(' '):
        if w in tech_related_words:
            cat_counts['tech'] += 1
        elif w in edu_related_words:
            cat_counts['edu'] += 1
        elif w in gk_related_words:
            cat_counts['gk'] += 1
    return cat_counts

###############################
## STEP 5: Generate response ##
###############################

def response(query):
    res = 'This is a '
    replaced = replace_punctuation(query)
    cat_counts = count_categories(replaced)
    cat_to_adverb = {
        "tech": "technical",
        "edu": "educational",
        "gk": "general"
    }
    cats = []
    prev = 0
    for c, count in cat_counts.items():
        if count > 0 and abs(count - prev) < 5:
            cats.append(c)
        prev = count
    res += f"very {' and '.join([cat_to_adverb[c] for c in cats])} question! lemme think about it...."
    return res


####################
## Test yourself! ##
####################

if __name__ == "__main__":
    inp = input("Query: ")
    print(response(inp))
