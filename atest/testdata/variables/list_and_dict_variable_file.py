from robot.utils import OrderedDict


def get_variables(*args):
    if args:
        return dict((args[i], args[i+1]) for i in range(0, len(args), 2))
    list_ = ['1', '2', 3]
    tuple_ = tuple(list_)
    dict_ = {'a': 1, 2: 'b'}
    ordered = OrderedDict((chr(o), o) for o in range(97, 107))
    return {'LIST__list': list_,
            'LIST__tuple': tuple_,
            'LIST__generator': (i for i in range(5)),
            'DICT__dict': dict_,
            'DICT__ordered': ordered,
            'scalar_list': list_,
            'scalar_tuple': tuple_,
            'scalar_generator': (i for i in range(5)),
            'scalar_dict': dict_,
            'failing_generator': failing_generator,
            'failing_dict': FailingDict({1: 2})}


def failing_generator():
    for i in [2, 1, 0]:
        yield 1/i


class FailingDict(dict):

    def __iter__(self):
        1/0
        raise Exception('Bang!!')

    def keys(self):
        return list(self)
