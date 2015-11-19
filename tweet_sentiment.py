import sys
import json
import string

def create_dictionary(AFINN_file):
    scores = {} # initialize an empty dictionary
    for line in AFINN_file:
  		  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		  scores[term] = int(score)   # Convert the score to an integer.
  		  # print scores.items() # Print every (term, score) pair in the dictionary
    return scores


def lines(tweet_file):
#this def creates a list of english tweets with 0's in the places where the tweets recieved are either not in english or not there
    tweets = []
    for line in tweet_file:
        python_tweet_line = json.loads(line) #changing JSON intp python
        if 'text' in python_tweet_line and python_tweet_line['lang'] == 'en': #must have text and english language       
            tweets.append(python_tweet_line["text"])
        else:
            tweets.append('0')
    return tweets


def match(tweets, scores):
    i = 0
    for tweet in tweets: 
        for c in string.punctuation: # takes out punctuation
            tweet = tweet.replace(c,"")
        tweets[i] = tweet.lower() #makes tweets in all lowercase
        words = tweets[i].split() #splits words at every white space
        i = i+1
        x = 0
        for word in words:
            if word in scores: #checks to see if word is in AFINN file
                x = x + scores[word] #adds together words that have sentiment values
        print x


def main():
    AFINN_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])    
    scores = create_dictionary(AFINN_file)
    tweets = lines(tweet_file)
    match(tweets, scores)


if __name__ == '__main__':
    main()
