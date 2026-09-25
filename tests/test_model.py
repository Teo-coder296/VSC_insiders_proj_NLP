from src.train import train_classifier, predict_label


def test_train_and_predict_label():
    documents = [
        "The market rallied after a strong earnings report",
        "Investors are worried about the falling stock price",
        "The team won the championship in dramatic fashion",
        "A new star athlete scored the winning goal",
    ]
    labels = ["finance", "finance", "sports", "sports"]

    classifier = train_classifier(documents, labels)
    label = predict_label(classifier, "stock market performance is rising")

    assert label == "finance"
