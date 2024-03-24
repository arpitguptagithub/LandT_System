import spacy

def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current



def identify_task_parameters(text, language='en'):
   
    if language == 'en':
        nlp = spacy.load("en_core_web_sm")
    elif language == 'fr':
        nlp = spacy.load("fr_core_news_sm")
    elif language == 'es':
        nlp = spacy.load("es_core_news_sm")
    else:
        raise ValueError("Unsupported language. Supported languages are 'en' (English), 'fr' (French), and 'es' (Spanish).")


    # Define patterns for pressure-related entities
    if language == 'en':
        patterns = [
            {"label": "PRESSURE_OBJECT", "pattern": [{"LOWER": {"IN": ["pressure", "stress", "force", "area"]}}]},
            {"label": "WATER_OBJECT", "pattern": [{"LOWER": {"IN": ["fluid level", "level of water", "water height", "height of liquid"]}}]},
            {"label": "PARAMETER_UNIT_PRESSURE", "pattern": [{"LOWER": {"IN": ["bar", "pascal", "atmospheric", "psi"]}}]},
            {"label": "PARAMETER_UNIT_WATER", "pattern": [{"LOWER": {"IN": ["meter", "centimeter", "inch", "foot"]}}]}
        ]
    elif language == 'fr':
        patterns = [
            {"label": "PRESSURE_OBJECT", "pattern": [{"LOWER": {"IN": ["pression", "force", "surface"]}}]},
            {"label": "WATER_OBJECT", "pattern": [{"LOWER": {"IN": ["niveau de fluide", "niveau d'eau", "hauteur d'eau", "hauteur du liquide"]}}]},
            {"label": "PARAMETER_UNIT_PRESSURE", "pattern": [{"LOWER": {"IN": ["bar", "pascal", "atmosphérique", "psi"]}}]},
            {"label": "PARAMETER_UNIT_WATER", "pattern": [{"LOWER": {"IN": ["mètre", "centimètre", "pouce", "pied"]}}]}
        ]
    elif language == 'es':
        patterns = [
            {"label": "PRESSURE_OBJECT", "pattern": [{"LOWER": {"IN": ["presión", "fuerza", "área"]}}]},
            {"label": "WATER_OBJECT", "pattern": [{"LOWER": {"IN": ["nivel de fluido", "nivel de agua", "altura del agua", "altura del líquido"]}}]},
            {"label": "PARAMETER_UNIT_PRESSURE", "pattern": [{"LOWER": {"IN": ["bar", "pascal", "atmosférico", "psi"]}}]},
            {"label": "PARAMETER_UNIT_WATER", "pattern": [{"LOWER": {"IN": ["metro", "centímetro", "pulgada", "pie"]}}]}
        ]

    # Add the patterns to the entity ruler
    ruler = nlp.add_pipe("entity_ruler", config={"overwrite_ents": True})
    ruler.add_patterns(patterns)

    doc = nlp(text)

    # Initialize variables
    object_to_set = None
    parameter_value = None
    parameter_unit = None

    # Extract identified entities
    for ent in doc.ents:
        if ent.label_ == "PRESSURE_OBJECT":
            object_to_set = ent.text
            print(f"Object to set: {object_to_set}")
        elif ent.label_ == "WATER_OBJECT":
            object_to_set = ent.text
            print(f"Object to set: {object_to_set}")
        elif ent.label_ == "CARDINAL":
            print(ent.text)
            if ent.text.isdigit():
                    parameter_value = float(ent.text)
                    print(f"Parameter value: {parameter_value}")
            else:  
                print(ent.text)
                numeric_value = text2int(ent.text)
                parameter_value = float(numeric_value)
                print(f"Parameter value: {parameter_value}")
             

        elif ent.label_ == "PARAMETER_UNIT_PRESSURE" or ent.label_ == "PARAMETER_UNIT_WATER":
            parameter_unit = ent.text 
            print(f"Parameter unit: {parameter_unit}")

    return object_to_set, parameter_value, parameter_unit

text_samples = [
     "Please set the pressure level to two hundered atmospheric units."
]

for text in text_samples:
    print(f"Processing text: {text}")
    object_to_set, parameter_value, parameter_unit = identify_task_parameters(text, language='en')

    if object_to_set and parameter_value is not None and parameter_unit:
        print(f"Text: {text}")
        print(f"\tObject to set: {object_to_set}")
        print(f"\tParameter value: {parameter_value}")
        print(f"\tParameter unit: {parameter_unit}")
        print("-" * 30)
    else:
        print(f"Could not identify all required parameters for: {text}")
