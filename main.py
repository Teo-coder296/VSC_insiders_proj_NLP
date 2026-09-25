from src.train import predict_label, train_classifier


def main() -> None:
    docs = [
        "The market rose after a strong earnings report",
        "Investors worry about falling stock prices",
        "The team won the championship after a dramatic finish",
        "The athlete scored the winning goal in the final minute",
    ]
    labels = ["finance", "finance", "sports", "sports"]

    model = train_classifier(docs, labels)
    print(predict_label(model, "stock prices are climbing after earnings"))


if __name__ == "__main__":
    main()
