class Ciphertext:
    def __init__(self, text, word_delimiter=' '):
        """
        Constructs a Ciphertext object.
        :param text: a string representation of the ciphertext
        :param word_delimiter: set a customised word delimiter - default is the space character
        """
        self.__text = list(text)
        self.__word_delimiter = word_delimiter
        # TODO: decide whether to make function calls to declare and init fields or use assignments to function calls
        self.__is_word_delimited = self.__is_word_delimited()
        # TODO: need to decide the approach here as these booleans can be figured out together
        self.__is_numeric_only = False
        self.__is_alphabetic_only = False
        self.__is_alphanumeric = False
        self.__analyse()

    def __is_word_delimited(self):
        """
        :return: a boolean describing if the text is word delimited or not
        """
        if self.__text.__contains__(self.__word_delimiter):
            return True
        else:
            return False

    def __analyse(self):
        """
        TODO: this private function should analyse the text and set variables on interesting aspects of the text.
        :return: None
        """
        # TODO: check for is_numeric_only, is_alphabetic_only & is_alphanumeric
        #  I think the best way to determine the sets of characters is to iterate over them and split them into
        #  sublists, then take a look at the lists afterwards to set the boolean fields
        #  Also need to figure out if having this stuff in a method call is the best decision
        numeric_character_list = []
        alphabetic_character_list = []
        for item in self.__text:
            if item.isnumeric():
                numeric_character_list += item

    def print_frequency_analysis(self):
        """
        TODO: this function should analyse the text and return a string that describes the frequency
            (count & percentage) of the unique characters contained within it.
            It should work with various types of ciphertext (numeric[hex, binary, decimal], alphabetic, alphanumeric?)
            Optional - a language flag can be set to give an estimation of mappings for that language
            Optional - it should be possible to specify how you want the data to be displayed - i.e. sort by
            highest/lowest frequency, first occurance of letter etc.
        :return: None
        """
        print('Not implemented yet...')

    def print_mapped_text(self, mapping_dict):
        """
        TODO: this function should map the text to a string according to the given mapping dictionary
        :param mapping_dict: the dictionary that defines the mapping to apply to the ciphertext
        :return: the mapped text
        """
        print('Not implemented yet...')

    def __str__(self):
        """
        TODO: this function should return a string representation of the object - add new fields as needed and analysis
            string or something
        :return: a string representation of the ciphertext
        """
        return self.__text

    def __len__(self, exclude=()):
        """
        Dicerns the length of the ciphertext.
        :param exclude: optional tuple to define characters to exclude when discerning the length
        :return: the length of the ciphertext
        """
        if exclude.__len__() > 0:
            count = 0
            for item in self.__text:
                if item not in exclude:
                    count += 1
            return count
        else:
            return list(self.__text).__len__()
