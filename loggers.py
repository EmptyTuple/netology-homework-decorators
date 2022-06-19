from functools import wraps
from datetime import datetime
import os

def just_logger(func):
    
    @wraps(func)
    def log_it(*args, **kwargs):
        with open('logfile.log', 'a') as f:
            f.write(datetime.now().strftime('%Y-%m-%d %H:%S:%f') + '\n')
            f.write(f'The function "{func.__name__}" was called,\n')
            f.write(f'with arguments: {args}{kwargs},\n')
            res = func(*args, **kwargs)
            f.write(f'{res} was returned.\n---------\n')
            return res
        
    return log_it

def logger_with_path(path_to_log):
    '''It's not a trivial to wrap recursive functions :)'''
    
    def _logger_with_path(func):
        if not os.path.isdir(path_to_log):
            os.makedirs(path_to_log)
        top_step = True
        @wraps(func)
        def log_it(*args, **kwargs):
            nonlocal top_step
            if top_step:
                top_step = False
                with open(f'{path_to_log}/logfile.log', 'a') as f:
                    f.write(datetime.now().strftime('%Y-%m-%d %H:%S:%f') + '\n')
                    f.write(f'The function "{func.__name__}" was called,\n')
                    f.write(f'with arguments: {args}{kwargs},\n')
                    res = func(*args, **kwargs)
                    f.write(f'{res} was returned.\n---------\n')
            else:
                res = func(*args, **kwargs)
                top_step = True
            return res
            
        return log_it
    return _logger_with_path
