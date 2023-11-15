class GrammarStats:
    def __init__(self):
        self.no_of_checks = 0
        self.checks_good = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        self.no_of_checks += 1
        text = str(text)
        if len(text) < 2:
            return False
        
        if text[0].isupper() and text[-1] in '.?!':
            self.checks_good += 1
            return True
        else:
            return False


    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.no_of_checks == 0:
            return 0
        
        return int((self.checks_good / self.no_of_checks) * 100)