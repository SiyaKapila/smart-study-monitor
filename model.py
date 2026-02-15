from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
texts = [
    "easy concept introduction",
    "simple example basic topic",
    "deadlock operating system confusing",
    "advanced algorithm complexity hard"
]

labels = ["easy", "easy", "risk", "risk"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)
def predict_confusion(text):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]



