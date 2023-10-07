#!/usr/bin/python3

def multiple_returns(sentence):
    """Generate the length of a string along with its initial character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
