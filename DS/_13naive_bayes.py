import re
import math

def tokensize(message):
    #convert to lower case
    message = message.lower()
    all_words = re.findall("[a-z0-9']+", mesage)
    return set(all_words)


def count_words(training_set):
    """training set consists of pairs (message, is_spam)"""
    counts = defaultdict(lambda: [0, 0])
    for message, is_spam in training_set:
        for word in tokensize(message):
            counts[word][0 if is_spam else 1] += 1
    return counts


def word_probabilities(counts, total_spams, total_non_spams, k=0.5):
    """turn the word_counts into a list of triplets
        w, p(w|spam) and p(w|~spam)"""
    return [(w,
             (spam + k) / (2*k + total_spams),
             (non_spam + k) / (2*k + total_non_spams))
            for w, (spam, non_spam) in counts.iteritems()]


def spam_probability(word_probs, message):
    message_words = tokensize(message)
    log_prob_if_spam = log_prob_if_not_spam = 0.0
    #iterate through each word in our vocabulary
    for word, prob_if_spam, prob_if_not_spam in word_probs:
        # if word appears in the message,
        # add the log probability of seeing ot
        if word in message_words:
            log_prob_if_spam += math.log(prob_if_spam)
            log_prob_if_not_spam += math.log(prob_if_not_spam)
        #if word does not appear in the message
        #add the log probability of not seeing it
        #which is log(1 - probability of seeing it)
        else:
            log_prob_if_spam += math.log(1.0 - prob_if_spam)
            log_prob_if_not_spam += math.log(1.0 - prob_if_not_spam)
    prob_if_spam = math.exp(log_prob_if_spam)
    prob_if_not_spam = math.exp(log_prob_if_not_spam)
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)


class NaiveBayesClassifier:

    def __init__(self, k=0.5):
        self.k = k
        self.word_probs = []

    def train(self, trainig_set):
        #count spam and non-spam mesages
        num_spams = len([is_spam
                        for message, is_spam in trainig_set
                        if is_spam])
        num_non_spams = len(trainig_set) - num_spams
        #run training data through our pipeline
        word_counts = counts_words(training_set)
        self.word_probs = word_probabilities(word_counts, num_spams, num_non_spams, self.k)

    def classify(self, message):
        return spam_probability(self.word_probs, message)
