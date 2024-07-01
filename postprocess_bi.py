import sys


def main():
    print("word llmsurp bori bprob iprob")
    all_word, all_llmsurp, all_bori, all_bprob, all_iprob = [], [], [], [], []
    with open(sys.argv[1], "r+") as f:
        lines = f.readlines()
        for line in lines[1:]:
            word, llmsurp, bori, bprob, iprob = line.strip().split(" ")
            all_word.append(word)
            all_llmsurp.append(float(llmsurp))
            all_bori.append(bori)
            all_bprob.append(float(bprob))
            all_iprob.append(float(iprob))
    assert len(all_word) == len(all_llmsurp) == len(all_bori) == len(all_bprob) == len(all_iprob)

    for i in range(len(all_word)-1):
        if all_bori[i+1] == "B":
            all_llmsurp[i] -= all_bprob[i+1]
            all_llmsurp[i+1] += all_bprob[i+1]
            print(all_word[i], all_llmsurp[i], all_bori[i], all_bprob[i], all_iprob[i])
        else:
            print(all_word[i], all_llmsurp[i], all_bori[i], all_bprob[i], all_iprob[i])
    print(all_word[-1], all_llmsurp[-1], all_bori[-1], all_bprob[-1], all_iprob[-1])


if __name__ == "__main__":
    main()
