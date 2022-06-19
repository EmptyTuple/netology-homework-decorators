import itertools
from functools import lru_cache
from loggers import just_logger, logger_with_path

# Use the previous homework functions

@just_logger
def flatten_single_nested(iterable: list | tuple)-> tuple:
    
    try:
        flat_thing = tuple(itertools.chain.from_iterable(iterable))
        return flat_thing
    except Exception as ex:
        print('There is a non-symmetric nesting in the iterable!')
        
@logger_with_path(path_to_log='tmp/logs')
def flatten_many_nested(iterable: list | tuple)-> tuple:
    
    try:
        flat_thing = list(itertools.chain.from_iterable(iterable))
        if any(map(lambda x: type(x) == list, flat_thing)) is True:
            flat_thing = flatten_many_nested(flat_thing)
        return tuple(flat_thing)
    except Exception as ex:
        print('There is a non-symmetric nesting in the iterable!')

def main():
    single_nested = [
	    ['a', 'b', 'c'],
	    ['d', 'e', 'f', 'h', False],
	    [1, 2, None]
    ]

    triple_nested = [
        [[['we', 'all'], ['live', 'in']], [['the', 'yellow'], ['submarine', 'yellow', 'submarine']]],
        [[['we', 'all'], ['live', 'in']], [['the', 'yellow'], ['submarine', 'yellow', 'submarine']]]
    ]

    flatten_single_nested(single_nested)
    flatten_many_nested(triple_nested)

if __name__ == '__main__':
    main()