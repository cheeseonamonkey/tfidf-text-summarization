from tfidf import compute_tfidf, load_corpus, summarize
import sys


def main():
    zipfilename = sys.argv[1]
    summarizefile = sys.argv[2]
    files_dic = load_corpus(zipfilename)
    tfidf = compute_tfidf(files_dic)
    score_lst = summarize(tfidf, files_dic[summarizefile], 20)
    for word, score in score_lst:
        print(f"{word} {round(score, 3)}")


if __name__ == "__main__":
    main()
