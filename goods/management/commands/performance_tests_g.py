import time

from django.core.management.base import BaseCommand
from django.db import connection


# Функция для выполнения explain analyze
def explain_analyze(queryset):
    query_str = str(queryset.query)  # Получаем текст SQL-запроса
    explain_query = f"EXPLAIN ANALYZE {query_str}"

    with connection.cursor() as cursor:
        cursor.execute(explain_query)
        results = cursor.fetchall()

    return results


# Функция для измерения времени выполнения запроса
def measure_time(queryset):
    start_time = time.time()
    list(queryset)  # Принудительно выполняем запрос
    end_time = time.time()
    return end_time - start_time


# Основная функция для выполнения тестов
def perform_tests(test_cases):
    results = {}

    for case in test_cases:
        method_name = case['method_name']
        queryset_func = case['queryset_func']

        # Выполняем запрос и собираем результаты
        queryset = queryset_func()
        explain_results = explain_analyze(queryset)
        execution_time = measure_time(queryset)

        results[method_name] = {
            'explain': explain_results,
            'execution_time': execution_time
        }

    # Выводим результаты
    for method, result in results.items():
        print(f"Method: {method}")
        print(f"Execution time: {result['execution_time']} seconds")
        print("EXPLAIN ANALYZE:")
        for row in result['explain']:
            print(row)
        print("=" * 50)


# Примеры запросов для тестирования
def query_prefetch_related():
    from goods.models import Product
    queryset = Product.objects.prefetch_related(
        "flour_name", "brand", "package"
    ).all()
    return queryset


def query_select_related():
    from goods.models import Product
    queryset = Product.objects.select_related(
        "flour_name", "brand", "package"
    ).all()
    return queryset


def query_select_prefetch_related():
    from goods.models import Product
    queryset = Product.objects.select_related(
        "flour_name", "brand").prefetch_related("package").all()
    return queryset


class Command(BaseCommand):
    help = 'Run performance tests for database queries'

    def handle(self, *args, **kwargs):
        test_cases = [
            {
                'method_name': 'prefetch_related',
                'queryset_func': query_prefetch_related
            },
            {
                'method_name': 'select_related',
                'queryset_func': query_select_related
            },
            {
                'method_name': 'select_prefetch_related',
                'queryset_func': query_select_prefetch_related
            }
        ]

        perform_tests(test_cases)
