___________________________________________________________________________________________________________
ISSUE 2 FILE => server_MAI.py, file.log (custom server log)

server_MAI.py

Обработчики:

схемы валидации -> ok

кэширование -> failed

логирование -> ok

измерение времени запроса -> failed

Скрипты:

запуск веб-сервера и вывод параметров запуска -> ok

запуск случайных обработчиков -> failed
    
===========================================================================================================

ISSUE 3 FILES => encode.py, decode.py, one_hot_encoder.py, one_hot_pytest.py

___________________________________________________________________________________________________________

encode.py 

используется директива -> ok

используется флаг -> ok

тест с message = 'SOS' -> ok

тест с исклечением (Exception) -> failed, perhaps ok

файл README.md с описанием шагов для запуска -> failed

файл result с командами и результатами запуска -> failed

файл *.py с функцией и доктестами -> ok

нет замечаний от flake8 -> ok


===========================================================================================================

decode.py

минимум 3 тестовых примера -> ok

файл README.md с описанием шагов для запуска -> failed

файл result с командами и результатами запуска -> failed

файл *.py с функцией и тестами -> ok

нет замечаний от flake8 -> ok


===========================================================================================================

one_hot_encoder.py

минимум 4 тестовых примера -> ok

минимум 2 метода проверки (assertEqual, assertNotIn, ...) -> ok

пример с перехватом исключения -> ok

файл README.md с описанием шагов для запуска -> failed

файл result с командами и результатами запуска -> failed

файл *.py с функцией и тестами -> ok

нет замечаний от flake8 -> ok


===========================================================================================================

one_hot_pytest.py

минимум 4 тестовых примера -> ok

пример с перехватом исключения -> ok (?)

файл README.md с описанием шагов для запуска -> failed

файл result с командами и результатами запуска -> failed

файл *.py с функцией и тестами -> ok

нет замечаний от flake8 -> ok

===========================================================================================================

                                          
 
