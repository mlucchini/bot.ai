def get():
    return {
        'entities': {
            'person': 'People, including fictional.',
            'norp': 'Nationalities or religious or political groups.',
            'facility': 'Buildings, airports, highways, bridges, etc.',
            'org': 'Companies, agencies, institutions, etc.',
            'gpe': 'Countries, cities, states.',
            'loc': 'Non-GPE locations, mountain ranges, bodies of water.',
            'product': 'Objects, vehicles, foods, etc. (Not services.)',
            'event': 'Named hurricanes, battles, wars, sports events, etc.',
            'word_of_art': 'Titles of books, songs, etc.',
            'language': 'Any named language.',
            'date':'Absolute or relative dates or periods.',
            'time': 'Times smaller than a day.',
            'percent': 'Percentage, including "%".',
            'money': 'Monetary values, including unit.',
            'quality': 'Measurements, as of weight or distance.',
            'ordinal': '"first", "second", etc.',
            'cardinal': 'Numerals that do not fall under another type.'
        }
    }
