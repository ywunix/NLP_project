
class Parser(object):
    def __init__():





if __name__ == "__main__":
    data = Dataset("tags-universal.txt", "brown-universal.txt", train_test_split=0.8)
    print("There are {} sentences in the corpus.".format(len(data)))
    print("There are {} sentences in the training set.".format(len(data.training_set)))
    print("There are {} sentences in the testing set.".format(len(data.testing_set)))
    assert len(data) == len(data.training_set) + len(data.testing_set), \
       "The number of sentences in the training set + testing set should sum to the number of sentences in the corpus"

    print("There are a total of {} samples of {} unique words in the corpus."
	  .format(data.N, len(data.vocab)))
    print("There are {} samples of {} unique words in the training set."
	  .format(data.training_set.N, len(data.training_set.vocab)))
    print("There are {} samples of {} unique words in the testing set."
	  .format(data.testing_set.N, len(data.testing_set.vocab)))
    print("There are {} words in the test set that are missing in the training set."
	  .format(len(data.testing_set.vocab - data.training_set.vocab)))
    assert data.N == data.training_set.N + data.testing_set.N, \
	   "The number of training + test samples should sum to the total number of samples"
