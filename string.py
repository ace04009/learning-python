import string

doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
keyword = 'casino'

def word_search(doc_list, keyword):
    indexes = []
    for doc in doc_list:
        keywords = doc.split()
        if (keyword in keywords):
            indexes.append(doc_list.index(doc))

    return indexes

print (word_search(doc_list, keyword))