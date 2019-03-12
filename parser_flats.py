import csv

flats_list = list()
with open('/home/lucio/Загрузки/output.csv', encoding="utf-8") as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=';')
    flats_list = list(flats_csv)
    header = flats_list.pop(0)
    i = 0
    for flat in flats_list:
        i += 1
        flat_dict = {}
        if "новостройка" in flat:
            new_list = list(filter(None, flat))
            flat_dict['id'] = new_list[0]
            flat_dict['rooms'] = new_list[1]
            flat_dict['type of flat'] = new_list[2]
            flat_dict['metro'] = new_list[3]
            flat_dict['time to metro'] = new_list[4]
            flat_dict['price'] = new_list[11]
            flat_dict['description'] = new_list[12]
            print("{}{}{}".format(i, '\n', flat_dict))
