# alternative method to write singleton pattern without using metaclassed
class _Spam:
    def __init__(self):
        print('Creating Spam')


_spam_instance = None


def spam():
    global _spam_instance
    if _spam_instance is not None:
        return _spam_instance
    else:
        _spam_instance = _Spam()
        return _spam_instance
