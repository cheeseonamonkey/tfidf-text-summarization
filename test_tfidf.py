import xml.etree.cElementTree as ET

from tfidf import gettext, tokenizer, compute_tfidf, summarize


def make_xml(title, *paragraphs):
    root = ET.Element("newsitem")
    ET.SubElement(root, "title").text = title
    text_el = ET.SubElement(root, "text")
    for p in paragraphs:
        ET.SubElement(text_el, "p").text = p
    return ET.tostring(root, encoding="unicode")


DOCS = {
    "a.xml": make_xml("Weather", "The weather today is sunny and warm with clear skies."),
    "b.xml": make_xml("Stocks", "Stock markets rallied sharply on positive earnings reports."),
}


def test_summarize_reduces_length():
    tfidf = compute_tfidf(DOCS)
    results = summarize(tfidf, DOCS["a.xml"], 10)
    tokens = tokenizer(gettext(DOCS["a.xml"]))
    assert len(results) < len(tokens)
    assert all(isinstance(s, float) for _, s in results)


def test_gettext_works():
    text = gettext(DOCS["a.xml"])
    assert "Weather" in text and "sunny" in text


def test_tokenizer_works():
    tokens = tokenizer("Running faster and higher")
    assert all(t.islower() for t in tokens)
    assert all(len(t) > 2 for t in tokens)
