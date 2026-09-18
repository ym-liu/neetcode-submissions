class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str_array = []

        # prefix
        for s in strs:
            encoded_str_array.append(str(len(s)))
            encoded_str_array.append("-")
        encoded_str_array.append(":")

        # actual elements
        for s in strs:
            encoded_str_array.append(s)

        return "".join(encoded_str_array)

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        str_lengths = []
        str_length = []
        cursor = -1

        # parse prefix
        for i, c in enumerate(s):
            if c == ":":
                cursor = i + 1
                break

            if c != "-":
                str_length.append(c)
            else:
                str_lengths.append(int("".join(str_length)))
                str_length = []

        # decode elements
        for length in str_lengths:
            decoded_str.append(s[cursor : cursor + length])
            cursor = cursor + length

        return decoded_str
