import sys

def create_dictionary(AFINN_file):
	scores = {} # initialize an empty dictionary
	for line in AFINN_file:
  		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)   # Convert the score to an integer.
  		# print scores.items() # Print every (term, score) pair in the dictionary

def hw():
    print 'Hello, world!'

def lines(tweet_file):
    print tweet_file[0]
    # print str(len(passed_file.readlines()))

def main():
    AFINN_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])    
    create_dictionary(AFINN_file)
    hw()
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
