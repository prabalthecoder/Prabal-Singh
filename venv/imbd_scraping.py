from xlwt import Workbook
import xlrd
from tkinter.filedialog import asksaveasfile, askopenfilename
from bs4 import BeautifulSoup
import requests
import cx_Oracle



wb_obj = Workbook()
my_sheet = wb_obj.add_sheet('IMDB')

def main():
    con = cx_Oracle.connect('SYSTEM/oracle@localhost:1521/orclcdb')
    cur = con.cursor()
    movie_list = []
    filename = askopenfilename()
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)

    for i in range(sheet.nrows):
        if i == 0:
            continue
        movie_list.append(sheet.cell_value(i, 0))
    my_sheet.write(0, 0, 'Title')
    my_sheet.write(0, 1, 'IMDB Rating')
    my_sheet.write(0, 2, 'Year')
    my_sheet.write(0, 3, 'Time')
    my_sheet.write(0, 4, 'Genre')
    my_sheet.write(0, 5, 'Release Date')
    my_sheet.write(0, 6, 'Country')
    my_sheet.write(0, 7, 'Language')
    my_sheet.write(0, 8, 'Gross USA')
    my_sheet.write(0, 9, 'Budget')
    my_sheet.write(0, 10, 'Opening Weekend USA')
    my_sheet.write(0, 11, 'Aspect Ratio')
    my_sheet.write(0, 12, 'Cumulative Worldwide Gross')
    my_sheet.write(0, 13, 'Taglines')

    k = 1
    for movie_name in movie_list:
        std_url     = 'https://www.imdb.com/find?s=tt&q=' + movie_name + '&ref_=nv_sr_sm'
        page        = requests.get(std_url)
        data        = page.content
        soup        = BeautifulSoup(data, 'html5lib')
        movie_id    = soup.select(".findList tr a")[0].get('href')
        movie_link  = 'https://www.imdb.com' + movie_id
        movie_page  = requests.get(movie_link)
        data2       = movie_page.content
        soup2       = BeautifulSoup(data2, 'html5lib')
        movie_title = soup2.select(".title_wrapper h1")[0].text
        movie_title = movie_title.strip()
        movie_name  = movie_title[:-7]
        movie_year  = movie_title[-5:-1]
        print("Movie year: " + movie_year)
        try:
            movie_rating = soup2.select(".ratingValue span")[0].text
            print("Movie rating: " + movie_rating)
        except Exception as e:
            print("Check rating link, eg batman movie didn't work")
            movie_rating = 'dummy'

        movie_time  = soup2.select(".subtext time")[0].text.strip()
        print("Movie time: " + movie_time)
        movie_genre = [i.text for i in soup2.select(".subtext a")][:-1]
        movie_genre = ', '.join(movie_genre)
        print("Movie genre: " + movie_genre)
        movie_release_date = [i.text for i in soup2.select(".subtext a")][-1:][0].strip()
        print("Movie release date: " + movie_release_date)

        for i in soup2.findAll("div", "txt-block"):
            if i.h4:
                if i.h4.text == "Country:":
                    movie_country = i.h4.next_sibling.next_element.text
                    print("Country: " + movie_country)
                if i.h4.text == "Language:":
                    movie_language = ", ".join([k.string for k in i.findAll('a')])
                    print("Language: " + movie_language)
                if i.h4.text == "Gross USA:":
                    Gross_Usa = i.h4.next_sibling.strip()
                    print("Gross USA: " + Gross_Usa)
                if i.h4.text == "Budget:":
                    Budget = i.h4.next_sibling.strip()
                    print("Budget: " + Budget)
                if i.h4.text == "Opening Weekend USA:":
                    Opening_Weekend_USA = i.h4.next_sibling.strip()
                    print("Opening Weekend USA: " + Opening_Weekend_USA)
                if i.h4.text == "Aspect Ratio:":
                    aspect_ratio = i.h4.next_sibling.strip()
                    print("Aspect Ratio: " + aspect_ratio)
                if i.h4.text == "Cumulative Worldwide Gross:":
                    Cumulative_Worldwide_Gross = i.h4.next_sibling.strip()
                    print("Cumulative Worldwide Gross: " + Cumulative_Worldwide_Gross)
                if i.h4.text == "Also Known As:":
                    also_known_as = i.h4.next_sibling.strip()
                    print("Also Known A: " + also_known_as)
                if i.h4.text == "Taglines:":
                    taglines = i.h4.next_sibling.strip()
                    print("Taglines: " + taglines)

        sql = ('insert into IMDB'
               '(IMDB_RATING, YEAR, TIME, GENRE, REALEASE_DATE,COUNTRY, LANGUAGE, '
               'GROSS_USA, BUDGET, OPENING_WEEKEND, ASPECT_RATIO, WORLD_RATE, TAGLINES) '
               'values (:myIMDB_RATING, :myYEAR, :myTIME, :myGENRE, :myREALEASE_DATE, :myCOUNTRY'
               ', :myLANGUAGE, :myGROSS_USA, :myBUDGET, :myOPENING_WEEKEND, :myASPECT_RATIO, :myWORLD_RATE,'
               ' :myTAGLINES)')
        res = cur.execute(sql, [movie_rating, movie_year, movie_time, movie_genre, movie_release_date,
                                movie_country, movie_language, Gross_Usa, Budget, Opening_Weekend_USA,
                                aspect_ratio, Cumulative_Worldwide_Gross, taglines])

        my_sheet.write(k, 0, movie_name)
        my_sheet.write(k, 1, movie_rating)
        my_sheet.write(k, 2, movie_year)
        my_sheet.write(k, 3, movie_time)
        my_sheet.write(k, 4, movie_genre)
        my_sheet.write(k, 5, movie_release_date)
        my_sheet.write(k, 6, movie_country)
        my_sheet.write(k, 7, movie_language)
        my_sheet.write(k, 8, Gross_Usa)
        my_sheet.write(k, 9, Budget)
        my_sheet.write(k, 10, Opening_Weekend_USA)
        my_sheet.write(k, 11, aspect_ratio)
        my_sheet.write(k, 12, Cumulative_Worldwide_Gross)
        my_sheet.write(k, 13, taglines)
        k = k + 1

    f = asksaveasfile(mode = 'w', defaultextension = ".csv")
    if f is not None:
        wb_obj.save(f.name)
    f.close()


    con.commit()


if __name__ == '__main__':
    main()
