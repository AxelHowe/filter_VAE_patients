'''
將PEEP以及FiO2的資料篩掉
只留有連續四天以上的病人資料

因為老師在 "VAE part 2" 的ppt上提到說
患者必須機械通氣至少 4 日才能滿足判斷 VAE 標準
'''
import csv


def main(file1, file2, file3, output):
    input = open(file1, newline='')  # 抓雲端的檔案
    input2 = open(file2, newline='')  # 抓雲端的檔案
    input3 = open(file3, newline='')  # 抓雲端的檔案
    data = csv.reader(input)  # 翻譯csv
    data2 = csv.reader(input2)  # 翻譯csv
    data3 = csv.reader(input3)  # 翻譯csv

    # 新檔案
    output = open(output, 'w', newline='')  # 自己新增新檔案
    writer = csv.writer(output)

    sick_firstday = {}  # 病發第一天
    write_list = []  # 要寫入新檔案的病人ID
    for row in data:
        sick_firstday[row[0]] = int(row[1])

    # 遍歷 白血球 wbc.csv
    for row in data2:
        if row[0] not in sick_firstday:
            continue

        if row[0] in write_list:
            continue

        if abs(int(row[1])-sick_firstday[row[0]]) <= 2:
            write_list.append(row[0])

    # 遍歷 體溫 temp.csv
    for row in data3:
        if row[0] not in sick_firstday:
            continue

        if row[0] in write_list:
            continue

        if abs(int(row[1])-sick_firstday[row[0]]) <= 2:
            write_list.append(row[0])

    for i in write_list:  # 寫入病人ID
        list = []
        list.append(i)
        writer.writerow(list)


if __name__ == "__main__":

    main("peep_merge_fio2.csv", "wbc_final.csv", "temp_final.csv",
         "Finish_third_conditions_id.csv")

    # four_day("fio2_last.csv", "fio2_final.csv", "fio2_more_then_four_days.csv")
