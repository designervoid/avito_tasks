from schema import Schema, And, Use, SchemaError
import logging
import logger
import re

schema_year = Schema(And(Use(int), lambda year: 0 <= year))

schema_host = Schema(And(Use(str), lambda host: len(str(host)) > 0))

schema_port = Schema(And(Use(int), lambda port: 0 < port))

validated_base_years = {'1': '2020', '2': '2000'}

log = logging.getLogger()


def enum_validated_base(year):
    if year in validated_base_years:
        log.info(validated_base_years)
    else:
        validated_base_years['3'] = year
        log.info(validated_base_years)
        log.info('year was cached')


def validate(schema):
    def wrapper(func):
        def wrapped(parameter):
            try:
                validated = schema.validate(parameter)
            except (ValueError, SchemaError) as e:
                log.error('Invalid data')
                raise e
            else:
                return func(validated)

        return wrapped

    return wrapper


@validate(schema_year)
def is_year_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


@validate(schema_host)
def host_check(request):
    response = re.compile("(?!-)[A-Z]{1,63}(?<!-)$", re.IGNORECASE)
    return all(response.match(x) for x in request.split("."))


@validate(schema_port)
def port_check(request) -> int:
    return 0 < request


def run_server(host='example.com', port=30001):
    year = 400
    if host_check(host) is True:
        log.info('host okay')
        if port_check(port) is True and port is int:
            log.info('port okay')
        else:
            log.warning('warning port')
        if is_year_leap(year) is True:
            enum_validated_base(year)
            log.info('input okay data')
        else:
            log.warning('input not okay data')
    else:
        log.warning('warning host')


if __name__ == '__main__':
    run_server()
