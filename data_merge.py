# coding:utf-8
import pandas as pd
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class NullExistErr(StandardError):
    pass

if __name__ == "__main__":
    data_holiday = []
    data = []
    day_map = {}
    with open('holiday2.csv', 'rU') as fr:
        reader = csv.reader(fr)
        for i, line_list in enumerate(reader):
            date_list = line_list[0].split('/')
            month = date_list[1]

            data_holiday.append(
                [int(month), int(line_list[1]), int(line_list[3])])
            day_map[line_list[0]] = i
    print data_holiday.__len__()

    with open("weather2.csv", "rU") as fr2:
        reader = csv.reader(fr2)
        for i, line_list in enumerate(reader):
            if day_map.has_key(line_list[0]):
                index = day_map[line_list[0]]

                high_t = int(line_list[2].strip())
                low_t = int(line_list[3].strip())
                status = 1
                if "晴" in line_list[4]:
                    status = 1
                elif "雨" in line_list[4]:
                    status = -1
                elif "多云" in line_list[4] or "阴" in line_list[4]:
                    status = 0

                wind = 0

                if "级" in line_list[4]:
                    wind = 1

                data.append([data_holiday[index][0], data_holiday[index][
                            1], data_holiday[index][2], high_t, low_t, status, wind])
                day_map[line_list[0]] = i
            else:
                print "not valuable data"
                raise

    print data, data.__len__()
    with open('data.csv', 'wb') as f:
        writer = csv.writer(f)
        line = ['record_date', 'user_id', 'month', 'weekday',
                'holiday', 'temp_high', 'temp_low', 'weather', 'wind']
        writer.writerow(line)

        with open("Tianchi_power.csv", "rU") as fr:
            reader = csv.reader(fr)
            for i, line_list in enumerate(reader):
                if not day_map.has_key(line_list[0]):
                    raise NullExistErr('num exist date')
                index = day_map[line_list[0]]
                line_list[1:1] = data[index]

                writer.writerow(line_list)
