'''1. Product Review Analysis'''

# Task 1: Keyword Highlighter
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
key_words= ['good','excellent','bad','Poor','average']
'''
for i in range(len(key_words)):
    for j in range(len(reviews)):
        if key_words[i] in reviews[j]:
            print(reviews[j].upper())
'''
# Task 2: Sentiment Tally
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tally(word_list1,word_list2,review_list):
    new_review_list = []
    for string in range(len(review_list)):
        new_review_list.append(review_list[string].lower())

    for i in range(len(word_list1)):
        for j in range(len(new_review_list)):
            if word_list1[i] in new_review_list[j]:
                print(f"{word_list1[i]} shows up {new_review_list[j].count(word_list1[i])} times in this revview: ")
                print(new_review_list[j])
    
    for e in range(len(word_list2)):
        for d in range(len(new_review_list)):
            if word_list2[e] in new_review_list[d]:
                print(f"{word_list2[e]} shows up {new_review_list[d].count(word_list2[e])} times in this review: ")
                print(new_review_list[d])
#test
#tally(positive_words,negative_words,reviews)


# Task 3: Review Summary
import pdb

def summary(review_list):
    summary_reviews = [ ]
    for i in range(len(review_list)):
        first_characters = review_list[i]
        if len(first_characters) > 30 :
            first_characters.split()
            print(first_characters)
            thirty_characters = []
            for i in range(30):
                thirty_characters.append(first_characters[i])
               
            final_review = "".join(first_characters)
            summary_reviews.append(f'{final_review}...')
    return print(summary_reviews)

#test
summary(reviews)

