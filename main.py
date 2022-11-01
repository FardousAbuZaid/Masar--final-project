import sys

from nltk import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

resurants = ["Martin Berasategui", "Agorregi jatetxea", "Misura", "Eme Be Garrote", "Trikuharri Taberna Jatetxea"]
museums = ["San Telmo Museoa", "Eureka! Zientzia Museoa", "Euskal Itsas Museoa", "Cibrian Gallery",
           "Lance and Malone Art Shop"]
walking = ["Donostia - San Sebasti?n Hop On - Hop Off Sightseeing Tour", "Buen Pastor Cathedral",
           "Iglesia de San Vicente", "Small-Group Electric Bike Tour in San Sebasti",
           "Evening Pintxo-Tapas Tour with Discover San Sebastian"]

# questionnare txt
with open('FinalProject/questioner.txt') as f:
    lines = f.read()
# read the files of the resturants
# file1 txt
with open('FinalProject/restaurant1.xls') as f:
    file1 = f.read()
# file2 txt
with open('FinalProject/restaurant2.xls') as f:
    file2 = f.read()
# file3 txt
with open('FinalProject/restaurant3.xls') as f:
    file3 = f.read()
# file4 txt
with open('FinalProject/restaurant4.xls') as f:
    file4 = f.read()
# file5 txt
with open('FinalProject/restaurant5.xls') as f:
    file5 = f.read()
# END of reading the files of the resturants
# read the files of the museums
# file1 txt
with open('FinalProject/museum1.xls') as f:
    Mfile1 = f.read()
# file2 txt
with open('FinalProject/museum2.xls') as f:
    Mfile2 = f.read()
# file3 txt
with open('FinalProject/museum3.xls') as f:
    Mfile3 = f.read()
# file4 txt
with open('FinalProject/museum4.xls') as f:
    Mfile4 = f.read()
# file5 txt
with open('FinalProject/museum5.xls') as f:
    Mfile5 = f.read()

# read the files of the Walking Tours
# file1 txt
with open('FinalProject/walking tour1.xls') as f:
    Rfile1 = f.read()
# file2 txt
with open('FinalProject/walking tour2.xls') as f:
    Rfile2 = f.read()
# file3 txt
with open('FinalProject/walking tour3.xls') as f:
    Rfile3 = f.read()
# file4 txt
with open('FinalProject/walking tour4.xls') as f:
    Rfile4 = f.read()
# file5 txt
with open('FinalProject/walking tour5.xls') as f:
    Rfile5 = f.read()

# List of documents of the restaurants;
reviews1 = [file1]
reviews2 = [file2]
reviews3 = [file3]
reviews4 = [file4]
reviews5 = [file5]
# List of documents of the museums;
museum1file = [Mfile1]
museum2file = [Mfile2]
museum3file = [Mfile3]
museum4file = [Mfile4]
museum5file = [Mfile5]
# List of documents of the Walking Tours;
walking1file = [Rfile1]
walking2file = [Rfile2]
walking3file = [Rfile3]
walking4file = [Rfile4]
walking5file = [Rfile5]

questionnare_data = [lines]


def lsaalgo(doc):
    # Initialize regex tokenizer
    # Stop Words: we want to delete this words from the documents.
    stopwords = ['a', 'worth', 'art', 'style', 'cook', 'complex', 'complete', 'pigeons', 'pigeon', 'own',
                 'impeccable',
                 'arzak', 'fond', 'finish',
                 'finding', 'expect', 'except', 'dined', 'architect', 'outstanding', 'akelarre', '2', '25th',
                 'anniversary',
                 'beautiful', 'smoked', 'beyond', 'coarses', 'eal', 'exact', 'found', 'dining', 'bit', 'fine',
                 'feel',
                 '3',
                 'highly', 'greatly', 'overbearing', 'amazing', 'martin', 'wow', 'world', 'able',
                 'dish', 'sirloin', 'ambiance', 'accepted', 'absolute', 'recommended', 'fit', 'friendly', 'truly',
                 'wait',
                 'tasting', 'bottles', 'fantastic', 'pace', 'plus', 'bite', 'san', 'star', 'dishes', 'absolutely',
                 'adequate', 'amazed', 'berasategui', 'meal', 'staff',
                 'menu', 'enjoyed', 'experience', 'incredible', 'nice', 'food', 'service', 'atmosphere', 'cozzy',
                 'family',
                 'restaurants', 'urchin', 'exquisite', 'restaurant', 'about',
                 'above', 'across', 'enjoyed', '14', '24', '4', 'especially', 'after', 'again', 'against',
                 'all', 'almost', 'alone', 'along', 'appreciated', 'gastronomy', 'helpful', 'gras', 'signature',
                 'orher',
                 'makes', 'flexible', 'matched', 'extremely', 'attentive', 'cater', 'favourite', 'already', 'also',
                 'although', 'always', 'stand', 'surpisingly', 'level', 'moreover', 'level', 'perfectly',
                 'regarding',
                 'among', 'an', 'and', 'fake', 'fois', 'goes', 'sebastian', 'another', 'perfect', 'any', 'anybody',
                 'anyone', 'anything',
                 'anywhere', 'are', 'area', 'areas', 'around', 'as', 'ask', 'asked', 'perfectly', 'welcome',
                 'asking', 'asks', 'at', 'away', 'b', 'back', 'backed', 'backing', 'backs', 'be',
                 'became', 'because', 'become', 'becomes', 'been', 'before', 'began', 'behind',
                 'being', 'beings', 'best', 'better', 'between', 'big', 'both', 'but', 'by', 'c',
                 'came', 'can', 'cannot', 'case', 'cases', 'certain', 'certainly', 'clear', 'clearly',
                 'come', 'could', 'd', 'did', 'differ', 'different', 'differently', 'do', 'does', 'done',
                 'down', 'down', 'downed', 'downing', 'downs', 'during', 'e', 'each', 'early', 'either',
                 'end', 'ended', 'ending', 'ends', 'enough', 'even', 'evenly', 'ever', 'every', 'everybody',
                 'everyone', 'everything', 'everywhere', 'f', 'face', 'faces', 'fact', 'facts', 'far',
                 'felt', 'few', 'find', 'finds', 'first', 'for', 'four', 'from', 'full', 'fully',
                 'further', 'furthered', 'furthering', 'furthers', 'g', 'gave', 'general', 'generally',
                 'get', 'gets', 'give', 'given', 'gives', 'go', 'going', 'good', 'goods', 'got', 'great',
                 'greater', 'greatest', 'group', 'grouped', 'grouping', 'groups', 'h', 'had', 'has', 'have',
                 'having', 'he', 'her', 'here', 'herself', 'high', 'high', 'high', 'higher', 'highest',
                 'him', 'himself', 'his', 'how', 'however', 'i', 'if', 'important', 'in', 'interest',
                 'interested', 'interesting', 'interests', 'into', 'is', 'it', 'its', 'itself', 'j',
                 'just', 'k', 'keep', 'keeps', 'kind', 'knew', 'know', 'known', 'knows', 'l', 'large', 'largely',
                 'last', 'later', 'latest', 'least', 'less', 'let', 'lets', 'like', 'likely', 'long', 'longer',
                 'longest', 'm', 'made', 'make', 'making', 'man', 'many', 'may', 'me', 'member', 'members',
                 'men', 'might', 'more', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', 'my', 'myself',
                 'n', 'necessary', 'need', 'needed', 'needing', 'needs', 'never', 'new', 'new', 'newer',
                 'newest', 'next', 'no', 'nobody', 'non', 'noone', 'not', 'nothing', 'now', 'nowhere',
                 'number', 'numbers', 'o', 'of', 'off', 'often', 'old', 'older', 'oldest', 'on',
                 'once', 'one', 'only', 'open', 'opened', 'opening', 'opens', 'or', 'order',
                 'ordered', 'ordering', 'orders', 'other', 'others', 'our', 'out', 'over', 'p',
                 'part', 'parted', 'parting', 'parts', 'per', 'perhaps', 'place', 'places', 'point',
                 'pointed', 'pointing', 'points', 'possible', 'present', 'presented', 'presenting',
                 'presents', 'problem', 'problems', 'put', 'puts', 'q', 'quite', 'r', 'rather',
                 'really', 'right', 'right', 'room', 'rooms', 's', 'said', 'same', 'saw', 'say',
                 'says', 'second', 'seconds', 'see', 'seem', 'seemed', 'seeming', 'seems',
                 'sees', 'several', 'shall', 'she', 'should', 'show', 'showed', 'showing',
                 'shows', 'side', 'sides', 'since', 'small', 'smaller', 'smallest', 'so',
                 'some', 'somebody', 'someone', 'something', 'somewhere', 'state', 'states',
                 'still', 'still', 'such', 'sure', 'range', 'recommend', 'seeing', 'start', 't', 'take', 'taken',
                 'than',
                 'that', 'the',
                 'their', 'them', 'then', 'there', 'therefore', 'these', 'they', 'thing', 'things',
                 'think', 'thinks', 'this', 'those', 'though', 'thought', 'thoughts', 'three',
                 'through', 'thus', 'to', 'today', 'together', 'too', 'took', 'toward', 'turn',
                 'turned', 'turning', 'turns', 'two', 'u', 'under', 'until', 'up', 'upon', 'substitute', 'hours',
                 'day',
                 'finished', 'told', 'vacation',
                 'us', 'use', 'used', 'uses', 'v', 'very', 'w', 'want', 'wanted', 'wanting',
                 'wants', 'was', 'way', 'ways', 'we', 'well', 'wells', 'went', 'were',
                 'what', 'when', 'where', 'whether', 'which', 'while', 'who', 'whole', 'whose',
                 'why', 'will', 'with', 'within', 'without', 'work', 'worked', 'working', 'works',
                 'would', 'x', 'y', 'year', 'years', 'yet', 'you', 'young', 'younger', 'youngest', 'your',
                 'yours', 'z', 'requirements', 'taste', 'specific', 'tailor', 'job', 'appreciating', 'challenge',
                 'matching', 'preferences']
    # Vectorize document using TF-IDF
    tokenizer = RegexpTokenizer(r'\w+')
    tfidf = TfidfVectorizer(lowercase=True,
                            stop_words=stopwords,
                            ngram_range=(1, 1),
                            tokenizer=tokenizer.tokenize)
    porter = PorterStemmer()
    # Fit and Transform the documents
    train_data = tfidf.fit_transform(doc)

    # Define the number of topics or components
    num_components = 3

    # Create SVD object
    # n_iter:
    # random_state:
    lsa = TruncatedSVD(n_components=num_components, n_iter=100, random_state=2)

    # Fit SVD model on data
    lsa.fit_transform(train_data)

    # Get Singular values and Components
    Sigma = lsa.singular_values_
    V_transpose = lsa.components_.T
    # Print the topics with their terms
    terms = tfidf.get_feature_names_out()

    for index, component in enumerate(lsa.components_):
        zipped = zip(terms, component)
        top_terms_key = sorted(zipped, key=lambda t: t[1], reverse=True)[:6]
        top_terms_list = list(dict(top_terms_key).keys())
        return top_terms_list;
        # for w in top_terms_list:
        # print("Topic" + str(index) + ": ", porter.stem(w), end=" ")


# take the result from the function lsaalo of the questionnare
questionnare = lsaalgo(questionnare_data)
# take the result from the function lsaalo of the restaurant reviews
review_file1 = lsaalgo(reviews1)
review_file2 = lsaalgo(reviews2)
review_file3 = lsaalgo(reviews3)
review_file4 = lsaalgo(reviews4)
review_file5 = lsaalgo(reviews5)
# take the result from the function lsaalo of the MUSEUMS reviews
reviewM_file1 = lsaalgo(museum1file)
reviewM_file2 = lsaalgo(museum2file)
reviewM_file3 = lsaalgo(museum3file)
reviewM_file4 = lsaalgo(museum4file)
reviewM_file5 = lsaalgo(museum5file)
# take the result from the function lsaalo of the WALKING TOURS reviews
reviewW_file1 = lsaalgo(walking1file)
reviewW_file2 = lsaalgo(walking2file)
reviewW_file3 = lsaalgo(walking3file)
reviewW_file4 = lsaalgo(walking4file)
reviewW_file5 = lsaalgo(walking5file)


# Jaccard_Similarity FUNCTION
def Jaccard_Similarity(vector1, vector2):
    # Find the intersection of words list of doc1 & doc2
    intersection = vector1.intersection(vector2)
    # Find the union of words list of doc1 & doc2
    union = vector1.union(vector2)
    # Calculate Jaccard similarity score
    # using length of intersection set divided by length of union set
    return float(len(intersection)) / len(union)


# the results of the restaurants: Jaccard_Similarity
result1 = Jaccard_Similarity(set(questionnare), set(review_file1))
result2 = Jaccard_Similarity(set(questionnare), set(review_file2))
result3 = Jaccard_Similarity(set(questionnare), set(review_file3))
result4 = Jaccard_Similarity(set(questionnare), set(review_file4))
result5 = Jaccard_Similarity(set(questionnare), set(review_file5))
# the results of the museums: Jaccard_Similarity
M_result1 = Jaccard_Similarity(set(questionnare), set(reviewM_file1))
M_result2 = Jaccard_Similarity(set(questionnare), set(reviewM_file2))
M_result3 = Jaccard_Similarity(set(questionnare), set(reviewM_file3))
M_result4 = Jaccard_Similarity(set(questionnare), set(reviewM_file4))
M_result5 = Jaccard_Similarity(set(questionnare), set(reviewM_file5))
# the results of the WALKING TOURS: Jaccard_Similarity
W_result1 = Jaccard_Similarity(set(questionnare), set(reviewW_file1))
W_result2 = Jaccard_Similarity(set(questionnare), set(reviewW_file2))
W_result3 = Jaccard_Similarity(set(questionnare), set(reviewW_file3))
W_result4 = Jaccard_Similarity(set(questionnare), set(reviewW_file4))
W_result5 = Jaccard_Similarity(set(questionnare), set(reviewW_file5))


# function that return the best place
def best_place(res1, res2, res3, res4, res5):
    if res1 >= res2 and res1 >= res3 and res1 >= result4 and res1 >= res5:
        return [1, res1]
    if res2 >= res3 and res2 >= res4 and res2 >= res5:
        return [2, res2]
    if res3 >= res4 and res3 >= res5:
        return [3, res3]
    if res4 >= res5:
        return [4, res4]
    else:
        return [5, res5]


# the final result of the best Restaurant
resultOfBest_place_Restaurant = best_place(result1, result2, result3, result4, result5)

# the final result of the best Museum
resultOfBest_place_Museum = best_place(M_result1, M_result2, M_result3, M_result4, M_result5)

# the final result of the best Walking Tour
resultOfBest_place_WalkingTour = best_place(W_result1, W_result2, W_result3, W_result4, W_result5)

# print the final result to the file finalResult;
file_path = 'FinalProject/finalResult.txt'
sys.stdout = open(file_path, "w")
print(
    "The best Restaurant is:" + resurants[resultOfBest_place_Restaurant[0] - 1] + "with jaccard similarity: " + str(
        resultOfBest_place_Restaurant[1]))
print("The best Museum is:" + museums[resultOfBest_place_Museum[0] - 1] + "with jaccard similarity: " + str(
    resultOfBest_place_Museum[1]))
print(
    "The best Walking Tour is:" + walking[
        resultOfBest_place_WalkingTour[0] - 1] + "with jaccard similarity: " + str(
        resultOfBest_place_WalkingTour[1]))
