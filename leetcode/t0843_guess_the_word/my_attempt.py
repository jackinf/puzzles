from typing import List


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        N = len(wordlist[0])
        sign = lambda a: (a>0)-(a<0)
        distances = []
        for word in wordlist:
            for word2 in wordlist:
                if word == word2:
                    continue
                matches = 0
                for i in range(len(word)):
                    matches += 1 if word[i] == word2[i] else 0
                distances.append((word, word2, matches))

        # print(distances)

        distances = sorted([x for x in distances], key=lambda item: item[2], reverse=True)
        # print(distances)

        current_word = distances.pop(0)[0]
        seen = []
        while True:
            seen.append(current_word)
            ans = master.guess(current_word)
            print(f'Guessing {current_word}, matches: {ans}')
            if ans == len(current_word):
                print(f'SOLUTION: {current_word}')
                print(len(seen))
                return

            # distances = [x for x in distances if x[2] != ans and x[0] != current_word]

            delta = 1
            while ans <= N:
                found = None
                for i, item in enumerate(distances):
                    if item[2] == ans and item[0] not in seen:
                        found = item
                # found = next((x for x in distances if x[2] == ans), None)
                if found is not None:
                    current_word = found[0]
                    distances.pop(i)
                    break

                ans += delta
                delta = -1 * (delta + sign(delta))


if __name__ == "__main__":
    s = Solution()

    secret_1, word_list_1 = "eiowzz", ["acckzz","ccbazz","eiowzz","abcczz"]
    secret_2, word_list_2 = "hbaczn", ["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"]

    s.findSecretWord(word_list_2, Master(secret_2))
