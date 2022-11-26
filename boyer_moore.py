class BoyerMoore:
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text

    def create_shift_table(self) -> dict[str, int]:
        skip_list = {}

        for i in range(0, len(self.pattern)):
            skip_list[self.pattern[i]] = max(1, len(self.pattern) - i - 1)
        return skip_list

    def search(self) -> list[int]:
        bad_char = self.create_shift_table()
        print("Shift table is ", bad_char)

        i = len(self.pattern) - 1

        result_of_search = []

        while i <= len(self.text) - 1:
            j = 0

            while j < len(self.pattern) and self.pattern[len(self.pattern) - j - 1] == self.text[i - j]:
                j += 1

            if j == len(self.pattern):
                result_of_search.append(i - len(self.pattern) + 1)
                i += 1
                continue

            else:
                shift = bad_char.get(self.text[i+j], len(self.pattern))

                skips = shift - j
                i += skips

        for res in result_of_search:
            print("Find pattern on index ", res)
        print('')

        return result_of_search
