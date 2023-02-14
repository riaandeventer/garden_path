# Software Engineer: RIAAN VAN DEVENTER (SN: RV22110005417)
# This was programmed for the Software Engineering BOOTCAMP
# Written on 14 February 2023

# ************** L3T11 - TASK ASSIGNMENT ************** 
# ● Find at least 5 garden path sentences from the web or think up your own.
# ● Store the sentences you have identified or created in a list called gardenpathSentences.
# ● Tokenise each sentence in the list and perform entity recognition.
# ● Examine how spaCy has categorised each sentence. Then, use spacy.explain 
#   to look up and print the meaning of entities that you don’t understand. 
#   For example: print(spacy.explain("FAC"))
# ● At the bottom of your file, write a comment about two entities that you looked up. 
#   For each entity answer the following questions:
#       ○ What was the entity and its explanation that you looked up?
#       ○ Did the entity make sense in terms of the word associated with it?
#******************************************************

# ======= Working with spaCy ===== #

import spacy

nlp = spacy.load('en_core_web_sm')

# Initialize the list and store 5 sentences in the list.
gardenpathSentences = []

gardenpathSentences.append ("Have the students who failed the June exam take the supplementary.")

gardenpathSentences.append ("Mary gave the child the dog bit a Band-Aid.")

gardenpathSentences.append ("She told me in Johannesburg a little white lie will come back to haunt me.")

gardenpathSentences.append ("The man who whistles tunes Steinway pianos.")

gardenpathSentences.append ("The one man who hunts ducks out on Saturdays.")

print()
print("--------------------------------------------------------------")

for i in range (len(gardenpathSentences)):
    doc = nlp(gardenpathSentences[i])
    print(f"Sentence {i+1} : {gardenpathSentences[i]}")
    # Tokenisation------------------------------------------------------------------

    # We want to recognise elements like punctuation of the text that help us (and a machine) 
    # to understand its structure and meaning. Let’s see how spaCy handles this.
    print()
    print(f"Tokens: {[token.orth_ for token in doc]}")

    # Entity recognition ------------------------------------------------------------------

    # Let’s take each sentence from gardenpathSentences entry. We will parse this text, 
    # then access the identified entities using the doc object’s .ents method. 
    # With this method called on the doc we can access additional token methods, specifically .label_ and .label.

    # Get labels and entities and print them
    print(f"Entities: {[(i, i.label_, i.label) for i in doc.ents]}")
    print("--------------------------------------------------------------")

'''Output of for i in range:

--------------------------------------------------------------
Sentence 1 : Have the students who failed the June exam take the supplementary.

Tokens: ['Have', 'the', 'students', 'who', 'failed', 'the', 'June', 'exam', 'take', 'the', 'supplementary', '.']
Entities: [(June, 'DATE', 391)]
--------------------------------------------------------------
Sentence 2 : Mary gave the child the dog bit a Band-Aid.

Tokens: ['Mary', 'gave', 'the', 'child', 'the', 'dog', 'bit', 'a', 'Band', '-', 'Aid', '.']
Entities: [(Mary, 'PERSON', 380)]
--------------------------------------------------------------
Sentence 3 : She told me in Johannesburg a little white lie will come back to haunt me.

Tokens: ['She', 'told', 'me', 'in', 'Johannesburg', 'a', 'little', 'white', 'lie', 'will', 'come', 'back', 'to', 'haunt', 'me', '.']
Entities: [(Johannesburg, 'GPE', 384)]
--------------------------------------------------------------
Sentence 4 : The man who whistles tunes Steinway pianos.

Tokens: ['The', 'man', 'who', 'whistles', 'tunes', 'Steinway', 'pianos', '.']
Entities: [(Steinway, 'ORG', 383)]
--------------------------------------------------------------
Sentence 5 : The one man who hunts ducks out on Saturdays.

Tokens: ['The', 'one', 'man', 'who', 'hunts', 'ducks', 'out', 'on', 'Saturdays', '.']
Entities: [(one, 'CARDINAL', 397), (Saturdays, 'DATE', 391)]
--------------------------------------------------------------
'''

# Get an explanation of 2 entities and print it.
entity_type = spacy.explain("GPE")
print()
print(f"GPE: {entity_type}")
print()

'''
-   In Sentence 3, Johannesburg was identified as a GPE.
    I looked this up and the explanation was as follow:
    GPE: Countries, cities, states
-   This indeed made sense since Johannesburg is a city as explained.
'''

entity_type = spacy.explain("ORG")
print(f"ORG: {entity_type}")
print()

'''
-   In Sentence 4, Steinway was identified as an ORG.
    I looked this up and the explanation was as follow:
    ORG: Companies, agencies, institutions, etc.
-   This indeed made sense since Steinway & Sons is a company making pianos, as explained.
'''