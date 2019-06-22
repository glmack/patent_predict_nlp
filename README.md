## patent_predict_nlp

The objective of this machine learning model is to help business users evaluate the probability and significance of future market trends by using patent documents to predict companies (entities) who own patent rights (as assignee) for inventions associated with the natural language processing (NLP) space.

### Business value
Early-mover advantages depend on the ability of business decision-makers to acquire knowledge of the pipeline of machine learning technologies that might shape markets into the future.

### Data sources
Data is acquired from public patent documents via the PatentsView API of the US Patent Organization (USPTO). The features for this model are text data from patent titles and abstract summaries of patent documents. The prediction target is the patent assignee of a given patent document.

### Data preparation
The dataset was subsetted to focus on companies that possess the greatest number of patents in the NLP space, resulting in 13 possible output classes (13 companies as patent assignees). Text preprocessing techniques - tokenization, punctuation cleaning are applied to raw text data prior to introduction to models.

### Modeling
The modelling task is multi-class classification task using neural networks with LSTM layers and a softmax activation function in Tensorflow 2.0 beta.

### Evaluation
The project evaluates model performance for multi-class classification using the categorical cross entropy of Tensorflow 2.0 beta as a loss function.

### Deployment
The model targets business consumers in the machine learning space who, as users, want to be able to evaluate the probability and significance of possible future market trends so that they can inform management decisions.
