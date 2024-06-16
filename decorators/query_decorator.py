import functools
import time

from django.db import connection, reset_queries


def query_debugger(func):
    """
    Decorator for tracking the number of database queries and the execution time of a function.
    Applied to a function or class method to provide information on the number of executed queries
    and the execution time of the function.

    Usage example:
        from decorators.query_decorator import query_debugger
        from django.utils.decorators import method_decorator

        # Applying the decorator to 'get', 'post' methods
        or to all 'dispatch' methods of a view class:
        @method_decorator(query_debugger, name='dispatch')
        class MyView(View):
            # class methods
    """

    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Function : {func.__name__}")  # noqa
        print(f"Number of Queries : {end_queries - start_queries}")  # noqa
        print(f"Finished in : {(end - start):.2f}s")  # noqa
        return result

    return inner_func
