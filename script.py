from bs4 import BeautifulSoup
from urllib.request import urlopen

def main():
    def get_data(total_pages):
        page_number = 1
        data = []
        while page_number <= total_pages:
            url = "http://mga.edu/course-schedule/index.php?quick=ALL&page="+str(page_number)+"&sort=subj&asc&term=201601"
            soup = BeautifulSoup(urlopen(url), "html.parser")
            tbody = soup.find("tbody")

            for row in tbody.findAll("tr"):
                classData = []
                #The [1:] slicing skips the first TD in every TR because the first TD is the online course icon indicator
                for cell in row.findAll("td")[1:]:
                    classData.append(cell.text.strip())
                data.append(classData)

            page_number += 1
            print("On page ", page_number)
        return data

    def print_data(data):
        file = open('course-data.yml', 'w')
        for row in data:
            file.write("- crn: " + str(row[0]) + "\n")
            file.write("  ptrm: " + str(row[1]) + "\n")
            file.write("  subject: " + str(row[2]) + "\n")
            file.write("  number: " + str(row[3]) + "\n")
            file.write("  section: " + str(row[4]) + "\n")
            file.write("  campus: " + str(row[5]) + "\n")
            file.write("  title: " + str(row[6]) + "\n")
            file.write("  seats: " + str(row[7]) + "\n")
            file.write("  hours: " + str(row[8]) + "\n")
            file.write("  begin: " + str(row[9]) + "\n")
            file.write("  end: " + str(row[10]) + "\n")
            file.write("  building: " + str(row[11]) + "\n")
            file.write("  room: " + str(row[12]) + "\n")
            file.write("  days: " + str(row[13]) + "\n")
            file.write("  instructor: " + str(row[14]) + "\n")
            file.write("\n")
        file.close()

    print("Working...")
    course_info = get_data(35)
    print("Writing to file...")
    #print_data(course_info)
    print("Done")


if __name__ == '__main__':
    main()