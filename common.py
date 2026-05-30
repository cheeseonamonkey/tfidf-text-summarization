from tfidf import Counter, gettext, load_corpus, stemwords, tokenize
import sys


def main():
    zipfilename = sys.argv[1]
    targetfile = sys.argv[2]
    xmltext = load_corpus(zipfilename)[targetfile]
    text = gettext(xmltext)
    count = sorted(
        Counter(stemwords(tokenize(text))).items(), key=lambda x: x[1], reverse=True
    )[:10]
    for word, freq in count:
        print(f"{word} {freq}")


if __name__ == "__main__":
    main()
