from leetcode.p0843_guess_the_word.master import Master


class Solution(object):
    def findSecretWord(self, wordlist, master: Master):
        N = len(wordlist)
        self.H = [[sum(a==b for a,b in zip(wordlist[i], wordlist[j]))
                   for j in range(N)] for i in range(N)]
        print(self.H)

        possible, path = range(N), ()
        while possible:
            guess = self.solve(possible, path)
            matches = master.guess(wordlist[guess])
            if matches == len(wordlist[0]):
                return wordlist[guess]
            print(f'Tried guessing {wordlist[guess]} with matches: {matches}')
            possible = [j for j in possible if self.H[guess][j] == matches]
            path = path + (guess,)
            print(path)
        return None

    def solve(self, possible, path = ()):
        if len(possible) <= 2: return possible[0]

        ansgrp, ansguess = possible, None
        for guess, row in enumerate(self.H):
            if guess not in path:
                groups = [[] for _ in range(7)]
                for j in possible:
                    if j != guess:
                        groups[row[j]].append(j)
                maxgroup = max(groups, key = len)
                if len(maxgroup) < len(ansgrp):
                    ansgrp, ansguess = maxgroup, guess

        return ansguess


if __name__ == "__main__":
    s = Solution()

    secret_word1, word_list1 = "acckzz", ["acckzz", "ccbazz", "eiowzz", "abcczz"]
    secret_word2, word_list2 = "hbaczn", ["gaxckt", "trlccr", "jxwhkz", "ycbfps", "peayuf", "yiejjw", "ldzccp", "nqsjoa", "qrjasy", "pcldos", "acrtag",
     "buyeia", "ubmtpj", "drtclz", "zqderp", "snywek", "caoztp", "ibpghw", "evtkhl", "bhpfla", "ymqhxk", "qkvipb",
     "tvmued", "rvbass", "axeasm", "qolsjg", "roswcb", "vdjgxx", "bugbyv", "zipjpc", "tamszl", "osdifo", "dvxlxm",
     "iwmyfb", "wmnwhe", "hslnop", "nkrfwn", "puvgve", "rqsqpq", "jwoswl", "tittgf", "evqsqe", "aishiv", "pmwovj",
     "sorbte", "hbaczn", "coifed", "hrctvp", "vkytbw", "dizcxz", "arabol", "uywurk", "ppywdo", "resfls", "tmoliy",
     "etriev", "oanvlx", "wcsnzy", "loufkw", "onnwcy", "novblw", "mtxgwe", "rgrdbt", "ckolob", "kxnflb", "phonmg",
     "egcdab", "cykndr", "lkzobv", "ifwmwp", "jqmbib", "mypnvf", "lnrgnj", "clijwa", "kiioqr", "syzebr", "rqsmhg",
     "sczjmz", "hsdjfp", "mjcgvm", "ajotcx", "olgnfv", "mjyjxj", "wzgbmg", "lpcnbj", "yjjlwn", "blrogv", "bdplzs",
     "oxblph", "twejel", "rupapy", "euwrrz", "apiqzu", "ydcroj", "ldvzgq", "zailgu", "xgqpsr", "wxdyho", "alrplq",
     "brklfk"]

    # print(s.findSecretWord(word_list1, Master(secret_word1)))
    print(s.findSecretWord(word_list2, Master(secret_word2)))