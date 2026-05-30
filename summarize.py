from tfidf import *


def main():
    zipfilename = sys.argv[1]
    summarizefile = sys.argv[2]
    files_dic = load_corpus(zipfilename)
    tfidf = compute_tfidf(files_dic)
    score_lst = summarize(tfidf, files_dic[summarizefile], 20)
    for i in range(len(score_lst)):
        print(score_lst[i][0] + " " + str(round(score_lst[i][1], 3)))


if __name__ == "__main__":
    main()
