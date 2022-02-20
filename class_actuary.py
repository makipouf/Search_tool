from datetime import datetime
from calendar import monthrange
from dateutil.relativedelta import relativedelta

now = datetime.now()


# Class job

class Job:

    def __init__(self, date=datetime.now()):

        self.now = date

        self.name = ''
        self.company = ''
        self.description = ''
        self.time_beginning = datetime(self.now.year, self.now.month, monthrange(self.now.year, self.now.month)[1], 0,
                                       0)
        self.time_ending = datetime(self.now.year, self.now.month, monthrange(self.now.year, self.now.month)[1], 0, 0)

    def beginning(self):

        time_beginning_ini = self.time_beginning
        return time_beginning_ini.strftime("%B %Y")

    def ending(self):

        time_ending_ini = self.time_ending
        return time_ending_ini.strftime("%B %Y")

    def length(self):

        try:
            assert ((self.time_ending - self.time_beginning).days >= 0)
            length = self.time_ending - self.time_beginning
            # return divmod(length.total_seconds(), 31536000)[0]
            return round(length.total_seconds() / 31536000, 1)

        except AssertionError:
            print("The length is negative -> Not possible")

    def change_company_name(self, name):

        try:
            assert (isinstance(name, str))
            self.company = name

        except AssertionError:
            print("The name of the company is not a string -> Not possible")

    def change_job_name(self, name):

        try:
            assert (isinstance(name, str))
            self.name = name

        except AssertionError:
            print("The name of the job is not a string -> Not possible")

    def change_time_beginning(self, date):

        try:
            datetime_beginning = datetime.strptime(date, '%b %Y')
            self.time_beginning = datetime_beginning

        except ValueError:
            print("The beginning date format is wrong")

    def change_time_ending(self, date):

        try:
            datetime_ending = datetime.strptime(date, '%b %Y')
            datetime_ending = datetime_ending.replace(day=monthrange(datetime_ending.year, datetime_ending.month)[1])
            self.time_ending = datetime_ending

        except ValueError:
            print("The ending date format is wrong")

    # def __repr__(self):
    #
    #     # return {'Job name':self.name, 'Company':self.company}
    #     return ''

    def __str__(self):
        # print("Job name: ",self.name,"\nCompany name: ",self.company,"\nBeinning date: ",self.beginning(),"\nEnding date: ",self.ending(),"\nJob length (/year): ",self.length())
        return "Job name: " + str(self.name) + "\nCompany name: " + str(self.company) + "\nBeinning date: " + str(
            self.beginning()) + "\nEnding date: " + str(self.ending()) + "\nJob length (/year): " + str(self.length())


# Class job

class Study:

    def __init__(self, date=datetime.now()):

        self.now = date

        self.name_study = ''
        self.school = ''
        self.type_degree = ''
        self.time_beginning = datetime(self.now.year, self.now.month, monthrange(self.now.year, self.now.month)[1], 0,
                                       0)
        self.time_ending = datetime(self.now.year, self.now.month, monthrange(self.now.year, self.now.month)[1], 0, 0)

    def beginning(self):

        time_beginning_ini = self.time_beginning
        return time_beginning_ini.strftime("%B %Y")

    def ending(self):

        time_ending_ini = self.time_ending
        return time_ending_ini.strftime("%B %Y")

    def length(self):

        try:
            assert ((self.time_ending - self.time_beginning).days >= 0)
            length = self.time_ending - self.time_beginning
            # return divmod(length.total_seconds(), 31536000)[0]
            return round(length.total_seconds() / 31536000, 1)

        except AssertionError:
            print("The length is negative -> Not possible")

    def add_name_study(self, name):

        try:
            assert (isinstance(name, str))
            self.name_study = name

        except AssertionError:
            print("The study name of the company is not a string -> Not possible")

    def add_school_name(self, name):

        try:
            assert (isinstance(name, str))
            self.school = name

        except AssertionError:
            print("The school name is not a string -> Not possible")

    def add_type_degree(self, name):

        try:
            assert (isinstance(name, str))
            self.type_degree = name

        except AssertionError:
            print("The type of degree is not a string -> Not possible")

    def change_time_beginning(self, date):

        try:
            datetime_beginning = datetime.strptime(date, '%Y')
            datetime_ending = datetime.strptime(date, '%Y')
            datetime_beginning = datetime_beginning.replace(day=1, month=9)
            datetime_ending = datetime_ending.replace(day=31, month=12)
            self.time_beginning = datetime_beginning
            self.time_ending = datetime_ending

        except ValueError:
            print("The beginning date format is wrong")

    def change_time_ending(self, date):

        try:
            datetime_ending = datetime.strptime(date, '%Y')
            datetime_ending = datetime_ending.replace(day=31, month=8)
            self.time_ending = datetime_ending

        except ValueError:
            print("The ending date format is wrong")

    def __str__(self):
        # print("Job name: ",self.name,"\nCompany name: ",self.company,"\nBeinning date: ",self.beginning(),"\nEnding date: ",self.ending(),"\nJob length (/year): ",self.length())
        return "School: " + str(self.school) + "\n" + str(self.type_degree) + " " + str(
            self.name_study) + "\nBeinning date: " + str(self.beginning()) + "\nEnding date: " + str(
            self.ending()) + "\nJob length (/year): " + str(self.length())


class Actuary:

    def __init__(self, date=datetime.datetime.now()):

        self.now = date

        self.name = ''
        self.title = ''
        self.connection = ''
        self.location = ''
        self.link = ''
        self.description = ''
        self.career = list()
        self.education = list()
        self.career_nb = 0
        self.education_nb = 0
        self.birthday_appr = None

    def add_name(self, name):

        try:
            assert (isinstance(name, str))
            self.name = name

        except AssertionError:
            print("The name of the actuary is not a string -> Not possible")

    def add_title(self, title):

        try:
            assert (isinstance(title, str))
            self.title = title

        except AssertionError:
            print("The title of the person is not a string -> Not possible")

    def add_location(self, location):

        try:
            assert (isinstance(location, str))
            self.location = location

        except AssertionError:
            print("The location of the actuary is not a string -> Not possible")

    def add_link(self, link):

        try:
            assert (isinstance(link, str))
            self.link = link

        except AssertionError:
            print("The link is not a string -> Not possible")

    def add_description(self, description):

        try:
            assert (isinstance(description, str))
            self.description = description

        except AssertionError:
            print("The description is not a string -> Not possible")

    def add_connection(self, connection):

        try:
            assert (isinstance(connection, str))
            self.connection = connection

        except AssertionError:
            print("The number of connections is not a string -> Not possible")

    def add_job(self, job):

        try:
            assert (isinstance(job, Job))
            career_update = self.career
            career_nb_update = self.career_nb
            career_update.append(job)
            career_nb_update += 1
            self.career = career_update
            self.career_nb = career_nb_update

        except AssertionError:
            print("This is not a Job class used with add_job")

    def add_education(self, study):

        try:
            assert (isinstance(study, Study))
            education_update = self.education
            education_nb_update = self.education_nb
            education_update.append(study)
            education_nb_update += 1
            self.education = education_update
            self.education_nb = education_nb_update

        except AssertionError:
            print("This is not a Study class used with add_education")

    def add_birthday_appr(self):
        nb = self.education_nb
        new_appr = self.birthday_appr
        if (nb != 0):
            m = nb-1
            while (m!=0):
                if(self.education[m].type_degree in ("Bachelor's degree")):
                    new_appr = self.education[m].time_beginning - relativedelta(years=18)
                    self.birthday_appr = new_appr
                    m=0
                elif(self.education[m].type_degree in ("Master's degree")):
                    new_appr = self.education[m].time_beginning - relativedelta(years=21)
                    self.birthday_appr = new_appr
                    m=0
                else:
                    m-=1

    def get_birthday_appr(self):
        birthday = self.birthday_appr
        # now = datetime.now()
        now_curr = self.now
        time_difference = relativedelta(now_curr, birthday)
        return str(time_difference.years) + " years"


    def __str__(self):
        # print("Job name: ",self.name,"\nCompany name: ",self.company,"\nBeinning date: ",self.beginning(),"\nEnding date: ",self.ending(),"\nJob length (/year): ",self.length())
        return " Name:          " + str(self.name) + "\n Title:         " + str(self.title) + "\n Location:      " + str(
            self.location) + "\n LinkedIn link: " + str(self.link)

# a = Job()
# print(a.beginning())
# print(a)
# a.beginning()
# a.ending()
# a.beginning()
# a.change_time_beginning('Jun 2005a')
# a.change_time_beginning('Jun 2005')
# a.change_time_ending('Jun 2005a')
# a.change_time_ending('Jun 2005')
# a.beginning()
# a.ending()
# a.length()
#
# a.name
# a.change_name('BNB')
