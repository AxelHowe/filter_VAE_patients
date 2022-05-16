'''
將PEEP以及FiO2的資料篩掉
只留有連續四天以上的病人資料

因為老師在 "VAE part 2" 的ppt上提到說
患者必須機械通氣至少 4 日才能滿足判斷 VAE 標準
'''
import csv


def four_day(file1, file2, output):
    input = open(file1, newline='')  # 抓雲端的檔案
    input2 = open(file2, newline='')  # 抓雲端的檔案
    data = csv.reader(input)  # 翻譯csv
    data2 = csv.reader(input2)  # 翻譯csv

    # 新檔案
    output = open(output, 'w', newline='')  # 自己新增新檔案
    writer = csv.writer(output)

    sick_firstdays = {}  # 病發第一天  {病人ID:病發第一天}
    dict = {}  # {病人ID:[有資料的天數]}
    for row in data:
        sick_firstdays[row[0]] = row[1]
        dict[row[0]] = []
        # print(row[0])

    for row in data2:
        if row[0] in sick_firstdays:
            dict[row[0]].append(int(row[1]))

    # print(dict)
    for i in dict:
        set_temp = set(dict[i])  # 換成 set 刪除重複的天數
        dict[i] = sorted(set_temp)  # 用 sorted() 把set轉為list
        if len(dict[i]) >= 4:  # if 有超過4天以上的資料
            print(i, dict[i])
            for j in range(len(dict[i])):  # 檢查是否有連續四天
                try:
                    if dict[i][j]+3 == dict[i][j+3]:
                        list = []
                        list.append(i)
                        list.append(sick_firstdays[i])
                        writer.writerow(list)
                        break
                except Exception as e:
                    # list index out of range 發生時就break
                    # print(e)
                    break


if __name__ == "__main__":

    four_day("peep_last.csv", "peep_final.csv", "peep_more_then_four_days.csv")

    four_day("fio2_last.csv", "fio2_final.csv", "fio2_more_then_four_days.csv")
