import pandas as pd
import glob as glob
import numpy as np
import os as os
import csv
from csv import writer
from csv import reader
from csv import DictReader
from csv import DictWriter

befComb_1 = pd.read_csv('/media/adit/TOSHIBA/data/edit/Attack_data/csv/attack_automate_down.csv', dtype=str, delimiter=',')
befComb_2 = pd.read_csv('/media/adit/TOSHIBA/data/edit/Attack_data/csv/attack_automate_up.csv', dtype=str, delimiter=',')

befCombFinal = befComb_1.join(befComb_2)

befCombFinal = befCombFinal.dropna()

spec_chars = ["-"]

#print(type(befCombFinal['wlan_radio.signal_dbm(1)']))

for char in spec_chars:
    befCombFinal['wlan_radio.signal_dbm(1)'] = befCombFinal['wlan_radio.signal_dbm(1)'].str.replace(char, ' ')
    befCombFinal['wlan_radio.signal_dbm(2)'] = befCombFinal['wlan_radio.signal_dbm(2)'].str.replace(char, ' ')

print(befCombFinal)

comb = befCombFinal

listComb = [list(row) for row in comb.values]

#number of row
nor = len(listComb)
split = int(nor/11)+1
print(split)

comb.to_csv('/home/adit/Documents/test_automate_2/Comb.csv', index=False, header=None )

with open('/home/adit/Documents/test_automate_2/Comb.csv', 'r') as read_obj, \
        open('/home/adit/Documents/test_automate_2/Comb.csv', 'r') as read_obj2, \
        open('/home/adit/Documents/test_automate_2/test_auto (1).csv', 'w', newline='') as write_obj1, \
        open('/home/adit/Documents/test_automate_2/test_auto (2).csv', 'w', newline='') as write_obj2, \
        open('/home/adit/Documents/test_automate_2/test_auto (3).csv', 'w', newline='') as write_obj3, \
        open('/home/adit/Documents/test_automate_2/test_auto (4).csv', 'w', newline='') as write_obj4, \
        open('/home/adit/Documents/test_automate_2/test_auto (5).csv', 'w', newline='') as write_obj5, \
        open('/home/adit/Documents/test_automate_2/test_auto (6).csv', 'w', newline='') as write_obj6, \
        open('/home/adit/Documents/test_automate_2/test_auto (7).csv', 'w', newline='') as write_obj7, \
        open('/home/adit/Documents/test_automate_2/test_auto (8).csv', 'w', newline='') as write_obj8, \
        open('/home/adit/Documents/test_automate_2/test_auto (9).csv', 'w', newline='') as write_obj9, \
        open('/home/adit/Documents/test_automate_2/test_auto (10).csv', 'w', newline='') as write_obj10, \
        open('/home/adit/Documents/test_automate_2/test_auto (11).csv', 'w', newline='') as write_obj11, \
        open('/home/adit/Documents/test_automate_2/test_label.csv', 'w', newline='') as write_obj12:

            inp = csv.reader(read_obj)
            inp2 = csv.reader(read_obj2)

            out1 = csv.writer(write_obj1)
            out2 = csv.writer(write_obj2)
            out3 = csv.writer(write_obj3)
            out4 = csv.writer(write_obj4)
            out5 = csv.writer(write_obj5)
            out6 = csv.writer(write_obj6)
            out7 = csv.writer(write_obj7)
            out8 = csv.writer(write_obj8)
            out9 = csv.writer(write_obj9)
            out10 = csv.writer(write_obj10)
            out11 = csv.writer(write_obj11)
            out12 = csv.writer(write_obj12)

            i=1
            j=1
            k=1

            for row in inp:
                if ((i % split) == 0) & (j == 1):
                    j = j + 1
                    i = i + 1
                    out1.writerow(row)
                    continue
                if ((i % split) == 1) & (j == 1):
                    out1.writerow(['S1A1']+['S2A1'])
                if j == 1:
                    out1.writerow(row)

                if ((i % split) == 0) & (j == 2):
                    j = j + 1
                    i = i + 1
                    out2.writerow(row)
                    continue
                if ((i % split) == 1) & (j == 2):
                    out2.writerow(['S1A1(1)']+['S2A1(1)'])
                if j == 2:
                    out2.writerow(row)

                if ((i % split) == 0) & (j == 3):
                    j = j + 1
                    i = i + 1
                    out3.writerow(row)
                    continue
                if ((i % split) == 1) & (j == 3):
                    out3.writerow(['S1A1(2)']+['S2A1(2)'])
                if j == 3:
                    out3.writerow(row)

                if ((i % split) == 0) & (j == 4):
                    j = j + 1
                    i = i + 1
                    out4.writerow(row)
                    continue
                if ((i % split) == 1) & (j == 4):
                    out4.writerow(['S1A1(3)']+['S2A1(3)'])
                if j == 4:
                    out4.writerow(row)

                if ((i % split) == 0) & (j == 5):
                    j = j + 1
                    i = i + 1
                    out5.writerow(row)
                    continue
                if ((i % split) == 1) & (j == 5):
                    out5.writerow(['S1A1(4)']+['S2A1(4)'])
                if j == 5:
                    out5.writerow(row)

                if ((i % split) == 0) & (j == 6):
                    j = j + 1
                    i = i + 1
                    out6.writerow(row)
                    continue
                if ((i % split) == 1) & (j == 6):
                    out6.writerow(['S1A1(5)']+['S2A1(5)'])
                if j == 6:
                    out6.writerow(row)

                if ((i % split) == 0) & (j == 7):
                    j = j + 1
                    i = i + 1
                    out7.writerow(row)
                    continue
                if ((i % split) == 1) & (j == 7):
                    out7.writerow(['S1A1(6)']+['S2A1(6)'])
                if j == 7:
                    out7.writerow(row)

                if ((i % split) == 0) & (j == 8):
                    j = j + 1
                    i = i + 1
                    out8.writerow(row)
                    continue
                if ((i % split) == 1) & (j == 8):
                    out8.writerow(['S1A1(7)']+['S2A1(7)'])
                if j == 8:
                    out8.writerow(row)

                if ((i % split) == 0) & (j == 9):
                    j = j + 1
                    i = i + 1
                    out9.writerow(row)
                    continue
                if ((i % split) == 1) & (j == 9):
                    out9.writerow(['S1A1(8)']+['S2A1(8)'])
                if j == 9:
                    out9.writerow(row)

                if ((i % split) == 0) & (j == 10):
                    j = j + 1
                    i = i + 1
                    out10.writerow(row)
                    continue
                if ((i % split) == 1) & (j == 10):
                    out10.writerow(['S1A1(9)']+['S2A1(9)'])
                if j == 10:
                    out10.writerow(row)

                if ((i % split) == 0) & (j == 11):
                    j = j + 1
                    i = i + 1
                    out11.writerow(row)
                    continue
                if ((i % split) == 1) & (j == 11):
                    out11.writerow(['S1A1(10)']+['S2A1(10)'])
                if j == 11:
                    out11.writerow(row)

                print(i)
                i = i + 1

            i=1

            for row in inp2:
                if i == split:
                    out12.writerow(['1'])
                    break
                if ((i % split) == 1):
                    out12.writerow(['label'])
                out12.writerow(['1'])
                i = i + 1


# with open('/home/adit/Documents/test_automate/test_auto (1).csv', 'r') as read_obj1, \
#     open('/home/adit/Documents/test_automate/test_auto (2).csv', 'r') as read_obj2, \
#     open('/home/adit/Documents/test_automate/test_auto (3).csv', 'r') as read_obj3, \
#     open('/home/adit/Documents/test_automate/test_auto (4).csv', 'r') as read_obj4, \
#     open('/home/adit/Documents/test_automate/test_auto (5).csv', 'r') as read_obj5, \
#     open('/home/adit/Documents/test_automate/test_auto (6).csv', 'r') as read_obj6, \
#     open('/home/adit/Documents/test_automate/test_auto (7).csv', 'r') as read_obj7, \
#     open('/home/adit/Documents/test_automate/test_auto (8).csv', 'r') as read_obj8, \
#     open('/home/adit/Documents/test_automate/test_auto (9).csv', 'r') as read_obj9, \
#     open('/home/adit/Documents/test_automate/test_auto (10).csv', 'r') as read_obj10, \
#     open('/home/adit/Documents/test_automate/test_auto (11).csv', 'r') as read_obj11, \
#         open('/home/adit/Documents/test_automate/test_auto_comb.csv', 'w', newline='') as write_obj_comb:
#
#             inp1 = csv.reader(read_obj1)
#             inp2 = csv.reader(read_obj2)
#             inp3 = csv.reader(read_obj3)
#             inp4 = csv.reader(read_obj4)
#             inp5 = csv.reader(read_obj5)
#             inp6 = csv.reader(read_obj6)
#             inp7 = csv.reader(read_obj7)
#             inp8 = csv.reader(read_obj8)
#             inp9 = csv.reader(read_obj9)
#             inp10 = csv.reader(read_obj10)
#             inp11 = csv.reader(read_obj11)
#
#             outfinal = csv.writer(write_obj_comb)
#
#             for row in inp1:
#                 row.append(read_obj2)
#                 outfinal.writerow(row)

comb1 = pd.read_csv('/home/adit/Documents/test_automate_2/test_auto (1).csv', delimiter=',')
comb2 = pd.read_csv('/home/adit/Documents/test_automate_2/test_auto (2).csv', delimiter=',')
comb3 = pd.read_csv('/home/adit/Documents/test_automate_2/test_auto (3).csv', delimiter=',')
comb4 = pd.read_csv('/home/adit/Documents/test_automate_2/test_auto (4).csv', delimiter=',')
comb5 = pd.read_csv('/home/adit/Documents/test_automate_2/test_auto (5).csv', delimiter=',')
comb6 = pd.read_csv('/home/adit/Documents/test_automate_2/test_auto (6).csv', delimiter=',')
comb7 = pd.read_csv('/home/adit/Documents/test_automate_2/test_auto (7).csv', delimiter=',')
comb8 = pd.read_csv('/home/adit/Documents/test_automate_2/test_auto (8).csv', delimiter=',')
comb9 = pd.read_csv('/home/adit/Documents/test_automate_2/test_auto (9).csv', delimiter=',')
comb10 = pd.read_csv('/home/adit/Documents/test_automate_2/test_auto (10).csv', delimiter=',')
comb11 = pd.read_csv('/home/adit/Documents/test_automate_2/test_auto (11).csv', delimiter=',')
label = pd.read_csv('/home/adit/Documents/test_automate_2/test_label.csv', delimiter=',')
combFinal = pd.read_csv('/home/adit/Documents/test_automate_2/ori/A1Master(test10)empty_2.csv', delimiter=',')


master = comb1.join(comb2.join(comb3.join(comb4.join(comb5.join(comb6.join(comb7.join(comb8.join(comb9.join(comb10.join(comb11.join(label)))))))))))

print(master)

master2 = combFinal.append(master,sort=False)

print(master2)

master2 = master2.dropna()

print(master2)

master2.to_csv('/home/adit/Documents/test_automate_2/MasterComplete.csv',index=False)


# ,comb3,comb4,comb5,comb6,comb7,comb8,comb9,comb10,comb11,
