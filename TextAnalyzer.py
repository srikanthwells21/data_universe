class TextAnalyzer(object):
    def __init__(self, text):

        #remove punctuation
        self.text = text
        formattedText = text.replace(',',' ').replace('.',' ').replace('!',' ')

        formattedText = formattedText.lower()

        self.ForText = formattedText

    def freqAll(self):
        #split text into words
        WordList = self.ForText.split(' ')

        #create a dictionary to hold count of strings
        TextDict = {}
        for word in set(WordList):
            TextDict[word] = WordList.count(word)

        return TextDict
    
    def freqAs(self, word):
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0
        
if __name__ == "__main__":
    text = "Hello, World! Hello Python. Python is great!"

    analyzer = TextAnalyzer(text)

    print("Formatted Text:")
    print(analyzer.ForText)
    
    print("\nFrequency of all words:")
    print(analyzer.freqAll())
    
    print("\nFrequency of specific word:")
    print("python:", analyzer.freqAs("python"))
    print("hello:", analyzer.freqAs("hello"))
    print("java:", analyzer.freqAs("java"))
