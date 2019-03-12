from schema import Schema, And, Use, SchemaError
import logging
import logger
import re


schema_year = Schema(And(Use(int), lambda year: 0 <= year))

schema_host = Schema(And(Use(str), lambda host: len(str(host)) > 0))

schema_port = Schema(And(Use(int), lambda port: 0 < port))

validated_base_years = {'1': '2020', '2': '2000'}

#DEBUG
#INFO
#WARNING
#ERROR
#CRITICAL

logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)

console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def enum_validated_base(year):
    if year in validated_base_years:
        logger.info(validated_base_years)
    else:
        validated_base_years['3'] = year
        logger.info(validated_base_years)
        logger.info('year was cached')


def validate(schema):
    def wrapper(func):
        def wrapped(parameter):
            try:
                validated = schema.validate(parameter)
            except Exception as e:
                logger.error('Invalid data')
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


def run_server(host='example.com///', port=30001):
    year = 400
    try:
        logger.info('Start server')
        if host_check(host) is True:
            logger.info('host ok')
        else:
            logger.warning('host warning')
            run_server(host='example.com')
        if port_check(port) is True:
            logger.info('port ok')
        else:
            logger.warning('port warning')
        if is_year_leap(year) is True:
            logger.info('year ok')
            enum_validated_base(year)
        else:
            logger.warning('year not ok')
    except Exception as e:
        logger.error('Invalid data')
        raise e

if __name__ == '__main__':
    run_server()
