def summarize_text(text):
    sentences = text.split(".")
    summary = ". ".join(sentences[:2])
    return summary


if __name__ == "__main__":
    with open("../data/sample_article.txt", "r") as f:
        article = f.read()

    summary = summarize_text(article)

    print("Generated Summary:\n")
    print(summary)