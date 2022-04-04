//Write to Text file

//open file and give write permission
f = open("test_file.txt","w")

//write to file 
f.write("test text")

//close file
f.close()




//Write to csv file 

//library
import csv

//open file and write to using append
f = open("csv_file.csv","a", newline="") //prevents new line after every line 

//write data to the csv file 
tuple1 =("bob",19)

//adding another row to the existing one 
writer = csv.writer(f)
writer.writerow(tuple1)

//close file
f.close()