import psycopg2
import csv

my_file = open('project_contract_matster.csv')
csv_data = csv.reader(my_file)

database = psycopg2.connect (database = "test2", user="postgres", password="wldndkQk2017", host="localhost", port="5432")

cursor = database.cursor()


for row in csv_data:

    cursor.execute("INSERT INTO lgcom_partnerresourcestate (team, pjt_code, pjt_name, crt_code, crt_name, pm_name,sm_si, ptr_cpny,kor_name,crt_period,man_month,level, price)"\
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
               row)


cursor.close()
database.commit()
database.close()

print ("CSV data imported")