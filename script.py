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
                    if (cell.text != "") or (cell.text != " ") or (cell.text != "  "):
                        classData.append(cell.text)
                data.append(classData)

            page_number += 1

        return data

    course_info = get_data(35)
    for i in course_info:
        print(i, "\n")


if __name__ == '__main__':
    main()