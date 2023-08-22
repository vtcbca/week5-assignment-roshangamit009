import csv
# direct insert 5 record
with open('student.csv', 'w', newline='') as f:
    w = csv.writer(f)
    header = ['sid', 'sname', 'city', 'contact']
    w.writerow(header)
    row =[[1, 'om', 'bardoli', 9835775732],[2, 'sai', 'surat', 7857694876],[3, 'ram', 'vyara', 8495768390],[4, 'tulsi', 'karod', 6728495828],[5, 'gopal', 'bardoli', 9327638989]]
    w.writerows(row)

# input 5 records with user input
with open('student.csv', 'a', newline='') as f:
    w = csv.writer(f)
    for i in range(5):
        sid = int(input("Enter Student id:"))
        sname = input("Enter Student name:")
        city = input("Enter Student city:")
        contact = input("Enter Student contact:")
        row = [sid, sname, city, contact]
        w.writerow(row)

# read and print using csv file
with open('student.csv', 'r') as read:
    j = csv.reader(read)
    for i in j:
        print(i)
"""
Enter Student id:6
Enter Student name:ROSHAN
Enter Student city:BARDOLI
Enter Student contact:932765436
Enter Student id:7
Enter Student name:TRACK
Enter Student city:SURAT
Enter Student contact:6899685849
Enter Student id:8
Enter Student name:SAHIL
Enter Student city:KAROD
Enter Student contact:8969394857
Enter Student id:9
Enter Student name:BHARGAV
Enter Student city:BEDKUA
Enter Student contact:384758345
Enter Student id:10
Enter Student name:DINESH
Enter Student city:JARUN
Enter Student contact:2834792874
['sid', 'sname', 'city', 'contact']
['1', 'om', 'bardoli', '9835775732']
['2', 'sai', 'surat', '7857694876']
['3', 'ram', 'vyara', '8495768390']
['4', 'tulsi', 'karod', '6728495828']
['5', 'gopal', 'bardoli', '9327638989']
['6', 'ROSHAN', 'BARDOLI', '932765436']
['7', 'TRACK', 'SURAT', '6899685849']
['8', 'SAHIL', 'KAROD', '8969394857']
['9', 'BHARGAV', 'BEDKUA', '384758345']
['10', 'DINESH', 'JARUN', '2834792874']
>>>
"""
