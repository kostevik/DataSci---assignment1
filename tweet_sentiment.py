import sys
import json

def create_dictionary(AFINN_file):
    scores = {} # initialize an empty dictionary
    for line in AFINN_file:
  		  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		  scores[term] = int(score)   # Convert the score to an integer.
  		  # print scores.items() # Print every (term, score) pair in the dictionary
    return scores


def hw():
    print 'Hello, world!'


def lines(tweet_file):
#this def creates a list of english tweets with 0's in the places where the tweets are in a bad format
    tweets = []
    for line in tweet_file:
        python_tweet_line = json.loads(line) #changing JSON intp python
        if 'text' in python_tweet_line and python_tweet_line['lang'] == 'en': #must have text and english language       
            tweets.append(python_tweet_line["text"])
        else:
            tweets.append('0')
    print tweets
    return tweets

#def match(tweets, scores):
#this will go through AFINN file and check to see if any of the words are in the tweet
 #  print 'Kari'


def main():
    AFINN_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])    
    create_dictionary(AFINN_file)
    hw()
    lines(tweet_file)
    #match(tweets, scores)

if __name__ == '__main__':
    main()
    #match(tweets, scores)
