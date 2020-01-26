from typing import List


class Solution:
    def numberToWords(self, num: int) -> str:
        ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        ndigits = {3: "Thousand", 6: "Million", 9: "Billion", 12: "Trillion", 15: "Quadrillion", 18: "Quintillion", 21: "Sextillion", 24: "Septillion", 27: "Octillion", 30: "Nonillion"}
        num_s = str(num)
        words = []
        if len(num_s) == 1 and num_s == "0":
            return "Zero"

        if len(num_s) > 3:
            digits = len(num_s)

            haha = len(num_s)%3
            if haha != 0:
                part = int(num_s[0:haha])
                num_s = num_s[haha:]
                words += self.get_less_than_thousand_in_words(part)

            for xx in reversed(range(3, digits+1, 3)):
                part = int(num_s[0:3])
                # words.append(ones[int(num_s[0])])
                num_s = num_s[3:]
                words.append(ndigits[xx])
                if part == 0:
                    continue
                words += self.get_less_than_thousand_in_words(part)

        words2 = self.get_less_than_thousand_in_words(num)
        return " ".join(words + words2)

    def get_less_than_thousand_in_words(self, num: int) -> List[str]:
        ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        twodigits = ["xxx", "xxx", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        words = []

        arr = [int(x) for x in str(num)]

        # word = ""
        if len(arr) == 3:
            # word += f"{ones[arr[0]]} Hundred "
            words.append(ones[arr[0]])
            words.append("Hundred")
            arr.pop(0)

        if len(arr) == 2:
            if arr[0] != 0:
                twodigit = int(f"{arr[0]}{arr[1]}")
                if twodigit > 19:
                    # word += f"{twodigits[arr[0]]} "
                    words.append(twodigits[arr[0]])
                    if arr[1] != 0:
                        # word += ones[arr[1]]
                        words.append(ones[arr[1]])
                    arr.pop(0)
                elif 19 >= twodigit >= 10:
                    # word += f"{tens[arr[1]]}"
                    words.append(tens[arr[1]])
                    return words
            elif arr[1] != 0:
                # word += ones[arr[1]]
                words.append(ones[arr[1]])
            return words

        if len(arr) == 1 and arr[0] != 0:
            words.append(ones[arr[0]])
            return words

        return words


if __name__ == "__main__":
    s = Solution()
    # print(s.numberToWords(123))
    # print(s.numberToWords(587))
    # print(s.numberToWords(12))
    # print(s.numberToWords(21))
    # print(s.numberToWords(105))
    # print(s.numberToWords(100))
    # print(s.numberToWords(119))
    # print(s.numberToWords(5))
    # print(s.numberToWords(11234567))
    # print(s.numberToWords(0))
    # print(s.numberToWords(1234567890))
    # print(s.numberToWords(2000001))
    print(s.numberToWords(1000))
    print(s.numberToWords(100000))
