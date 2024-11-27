"""Build methods

1) KG_Build: Knowledge Graph method

"""

def KG_Build(self, 
             context: str):
    """Knowledge Graph method.

    Using knowledge graph extraction method to extract multiple 
    triples from the context. Also, rebuild the W set

    Args:
        context: context of the conversation
                eg. Albert developed the theory. Henry learns it.

    Returns:
        triples: A list of tuples. The W set.
                 eg. [(Albert, developed, theory), 
                      (Henry, learns, it)]

    Raises:
        TypeError: context must be a string
    """
    if not isinstance(context, str):
        raise TypeError("context must be a string")

    # extract triples
    output = self.model.predict(sentence=context)

    triples = []
    for verb in output['verbs']:
        tags = verb['tags']
        words = output['words']
        subject, predicate, obj = "", "", ""
        for word, tag in zip(words, tags):
            if "ARG0" in tag:
                subject += word + " "
            elif "V" in tag:
                predicate += word + " "
            elif "ARG1" in tag:
                obj += word + " "
        if subject and predicate and obj:
            triples.append((subject.strip(), predicate.strip(), obj.strip()))

    # rebuild the W set
    self.W_set = triples

    return triples



