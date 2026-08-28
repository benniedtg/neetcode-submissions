class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        # Every pattern character must have one corresponding word
        if len(pattern) != len(words):
            return False
        
        # Create 2 dictionaries
        letter_to_word = {}
        word_to_letter = {}

        for letter, word in zip(pattern, words):
            # The letter already maps to a different word
            if letter in letter_to_word and letter_to_word[letter] != word:
                    return False
            
            # The word already maps to a different letter
            if word in word_to_letter and word_to_letter[word] != letter:
                    return False
            
            # Create the mappings if they are new
            letter_to_word[letter] = word
            word_to_letter[word] = letter

        return True

