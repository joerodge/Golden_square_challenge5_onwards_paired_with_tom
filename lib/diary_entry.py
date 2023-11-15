class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.index = 0
        

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self.title}: {self.contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        return len(self.contents.split() + self.title.split())


    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        if wpm <= 0:
            raise Exception("wpm must be greater than zero")
        
        word_count = self.count_words()
        reading_mins = word_count / wpm
        if reading_mins % 1 == 0:
            return reading_mins
        else:
            return int(reading_mins + 1)


    def reading_chunk(self, wpm, minutes) -> str:
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        if wpm <= 0:
            raise Exception("WPM must be greater than 0")

        words = self.contents.split()
        words_read_amount = wpm * minutes
        words_read = words[self.index:self.index + words_read_amount]

        self.index += words_read_amount
        if self.index >= len(words):
            self.index = 0

        return ' '.join(words_read)