class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i: j])

            start_of_string = j +1
            end_of_string = start_of_string + length
            decoded_string.append(s[start_of_string:end_of_string])
            
            i = end_of_string
        return decoded_string