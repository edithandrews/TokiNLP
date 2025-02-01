# Pattern for a capitalized word  
capitalized_word_pattern = [{"TEXT": {"REGEX": "^[A-Z][a-z]*$"}}]  

# jan 'Name'  
person_pattern = [  
    {"LOWER": "jan"},  
    {"TEXT": {"REGEX": "^[A-Z][a-z]*$"}, "OP": "+"}  
]  

# ma 'Name'  
country_pattern = [  
    {"LOWER": "ma"},  
    {"TEXT": {"REGEX": "^[A-Z][a-z]*$"}, "OP": "+"}  
]  

# ma tomo 'Name'  
city_pattern = [  
    {"LOWER": "ma"},  
    {"LOWER": "tomo"},  
    {"TEXT": {"REGEX": "^[A-Z][a-z]*$"}, "OP": "+"}  
]  

# toki 'Name'  
language_pattern = [  
    {"LOWER": "toki"},   
    {"TEXT": {"REGEX": "^[A-Z][a-z]*$"}, "OP": "+"}  
]  

# soweli 'Name'  
animal_pattern = [  
    {"LOWER": "soweli"},  
    {"TEXT": {"REGEX": "^[A-Z][a-z]*$"}, "OP": "+"}  
]  

# nasin sewi 'Name'  
religion_pattern = [  
    {"LOWER": "nasin"},  
    {"LOWER": "sewi"},  
    {"TEXT": {"REGEX": "^[A-Z][a-z]*$"}, "OP": "+"}  
]  

# one or more number words  
number_pattern = [  
    {"LOWER": {"IN": ["wan", "tu", "luka"]}, "OP": "+"}  
]  

ENTITY_PATTERNS = [  
    {"label": "PERSON", "pattern": person_pattern},  
    {"label": "COUNTRY/CONTINENT", "pattern": country_pattern},  
    {"label": "CITY", "pattern": city_pattern},  
    {"label": "LANGUAGE", "pattern": language_pattern},  
    {"label": "ANIMAL", "pattern": animal_pattern},  
    {"label": "RELIGION", "pattern": religion_pattern},  
    {"label": "NUMBER", "pattern": number_pattern},  
]  