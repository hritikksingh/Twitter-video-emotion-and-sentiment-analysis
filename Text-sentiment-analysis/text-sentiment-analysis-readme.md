# What is sentiment analysis -

### Essentially, sentiment analysis or sentiment classification fall into the broad category of text classification tasks where you are supplied with a phrase, or a list of phrases and your classifier is supposed to tell if the sentiment behind that is positive, negative or neutral. Sometimes, the third attribute is not taken to keep it a binary classification problem. In recent tasks, sentiments like "somewhat positive" and "somewhat negative" are also being considered. Let's understand with an example now.

Consider the following phrases:

- "Before he makes any purchases, Billy likes to do his research; he’s very economical."
- "Before he makes any purchases, Billy likes to do his research; he’s so cheap."

The phrases correspond to two statements, that how the same thing is expressed using two different set of words which completely changes their meaning and conveys different sentiments. There can also be a case where there is no such word in that phrase which can tell you about anything regarding the sentiment conveyed by it. Hence, that is an example of neutral sentiment.

Now, from a strict machine learning point of view, this task is nothing but a supervised learning task. You will supply a bunch of phrases (with the labels of their respective sentiments) to the machine learning model, and you will test the model on unlabeled phrases.

Here, we have used a sample dataset of US Airlines tweets to analyze the text and label the sentiment expressed by it using Machine Learning.