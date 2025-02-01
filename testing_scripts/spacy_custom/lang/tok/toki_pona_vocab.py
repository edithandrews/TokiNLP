# Combine all the words from the provided categories into a set to use as the vocabulary  
TOKI_PONA_VOCAB = set([  
    # Adjective words  
    'akesi', 'ala', 'alasa', 'ale', 'ali', 'anpa', 'ante', 'awen', 'esun', 'ijo', 'ike', 'ilo', 'insa', 'jaki',  
    'jan', 'jelo', 'jo', 'kala', 'kalama', 'kama', 'kasi', 'kili', 'kin', 'kiwen', 'kon', 'kule', 'kulupu', 'kute',  
    'lape', 'laso', 'lawa', 'len', 'lete', 'lili', 'linja', 'lipu', 'loje', 'lon', 'luka', 'lukin', 'lupa', 'ma',  
    'mama', 'mani', 'meli', 'mije', 'moku', 'moli', 'monsi', 'monsuta', 'mu', 'mun', 'musi', 'mute', 'namako',  
    'nanpa', 'nasa', 'nasin', 'nena', 'noka', 'oko', 'olin', 'open', 'pakala', 'pali', 'palisa', 'pana', 'pilin',  
    'pimeja', 'pini', 'poka', 'pona', 'pu', 'sama', 'seli', 'sewi', 'sijelo', 'sike', 'sin', 'sinpin', 'sitelen',  
    'sona', 'soweli', 'suli', 'suno', 'supa', 'suwi', 'tan', 'taso', 'tawa', 'telo', 'tenpo', 'toki', 'tomo', 'unpa',  
    'uta', 'utala', 'walo', 'waso', 'wawa', 'weka', 'wile',  
  
    # Adverb words  
    'ala', 'ale', 'ali', 'anpa', 'awen', 'ijo', 'ike', 'ilo', 'jaki', 'jan', 'kama', 'kili', 'kin', 'kiwen', 'kon',  
    'lape', 'lawa', 'lete', 'lili', 'lukin', 'mani', 'moku', 'moli', 'mu', 'musi', 'mute', 'nasa', 'noka', 'pakala',  
    'pali', 'pilin', 'pini', 'pona', 'sama', 'seli', 'sewi', 'sijelo', 'sike', 'sin', 'sitelen', 'suli', 'suno',  
    'taso', 'tawa', 'telo', 'tenpo', 'toki', 'tomo', 'unpa', 'uta', 'utala', 'wawa', 'weka', 'wile',  
  
    # Conjunction words  
    'ante', 'anu', 'en', 'ike', 'kin', 'open', 'pona', 'taso',  
  
    # Interjection words  
    'a', 'mu', 'o',  
  
    # Noun words  
    'akesi', 'ala', 'alasa', 'ale', 'ali', 'anpa', 'ante', 'awen', 'esun', 'ijo', 'ike', 'ilo', 'insa', 'jaki', 'jan',  
    'jelo', 'jo', 'kala', 'kalama', 'kama', 'kasi', 'ken', 'kepeken', 'kili', 'kin', 'kipisi', 'kiwen', 'ko', 'kon',  
    'kule', 'kulupu', 'kute', 'lape', 'laso', 'lawa', 'len', 'lete', 'lili', 'linja', 'lipu', 'loje', 'lon', 'luka',  
    'lukin', 'lupa', 'ma', 'mama', 'mani', 'meli', 'mije', 'moku', 'moli', 'monsi', 'monsuta', 'mu', 'mun', 'musi',  
    'mute', 'namako', 'nanpa', 'nasa', 'nasin', 'nena', 'nimi', 'noka', 'oko', 'olin', 'open', 'pakala', 'pali',  
    'palisa', 'pan', 'pana', 'pilin', 'pimeja', 'pini', 'pipi', 'poka', 'poki', 'pona', 'pu', 'sama', 'seli', 'selo',  
    'sewi', 'sijelo', 'sike', 'sin', 'sinpin', 'sitelen', 'sona', 'soweli', 'suli', 'suno', 'supa', 'suwi', 'tan',  
    'tawa', 'telo', 'tenpo', 'toki', 'tomo', 'tu', 'unpa', 'uta', 'utala', 'walo', 'wan', 'waso', 'wawa', 'weka',  
    'wile',  
  
    # Numeral words  
    'ala', 'wan', 'tu', 'luka', 'ten', 'mute', 'ale',  
  
    # Preposition words  
    'kepeken', 'lon', 'poka', 'sama', 'tan', 'tawa',  
  
    # Pronoun words  
    'mi', 'sina', 'ona', 'ni',  
  
    # Interrogative pronoun  
    'seme',  
  
    # Separator words  
    'e', 'la', 'li', 'o', 'pi',  
  
    # Intransitive verbs  
    'anpa', 'awen', 'ike', 'kalama', 'kama', 'kasi', 'ken', 'kepeken', 'kon', 'lape', 'lon', 'lukin', 'moli', 'mu',  
    'musi', 'pakala', 'pali', 'pilin', 'pu', 'sewi', 'sona', 'tan', 'tawa', 'toki', 'unpa',  
  
    # Transitive verbs  
    'alasa', 'anpa', 'ante', 'awen', 'esun', 'ijo', 'ike', 'ilo', 'jaki', 'jan', 'jelo', 'jo', 'kalama', 'kama',  
    'kasi', 'ken', 'kipisi', 'kiwen', 'ko', 'kon', 'kule', 'kulupu', 'kute', 'lape', 'lawa', 'len', 'lete', 'lili',  
    'lon', 'lukin', 'lupa', 'mama', 'moku', 'moli', 'mu', 'musi', 'mute', 'namako', 'nanpa', 'nasa', 'nimi', 'olin',  
    'open', 'pakala', 'pali', 'palisa', 'pan', 'pana', 'pilin', 'pimeja', 'pini', 'poki', 'pona', 'pu', 'sama',  
    'seli', 'selo', 'sewi', 'sike', 'sin', 'sijelo', 'sitelen', 'sona', 'suli', 'suno', 'supa', 'suwi', 'tawa',  
    'telo', 'toki', 'tomo', 'tu', 'unpa', 'uta', 'utala', 'walo', 'wan', 'wawa', 'weka', 'wile',  
  
    # Verb Prepositions  
    'kama', 'ken', 'kepeken', 'lukin', 'open', 'pini', 'pu', 'sona', 'wile',  
])  
  
# Punctuation marks  
TOKI_PONA_PUNCT = set(['.', '!', '?', ':', ',', '"', "'"])
