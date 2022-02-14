from datetime import datetime
from calendar import monthrange

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

    def add_company_name(self, name):

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
            datetime_beginning = datetime_beginning.replace(day=1,month=9)
            self.time_beginning = datetime_beginning

        except ValueError:
            print("The beginning date format is wrong")

    def change_time_ending(self, date):

        try:
            datetime_ending = datetime.strptime(date, '%Y')
            datetime_ending = datetime_ending.replace(day=31,month=8)
            self.time_ending = datetime_ending

        except ValueError:
            print("The ending date format is wrong")

    def __str__(self):
        # print("Job name: ",self.name,"\nCompany name: ",self.company,"\nBeinning date: ",self.beginning(),"\nEnding date: ",self.ending(),"\nJob length (/year): ",self.length())
        return "School: " + str(self.school) + "\n" + str(self.type_degree) + " " +  str(
            self.name_study) + "\nBeinning date: " + str(self.beginning()) + "\nEnding date: " + str(
            self.ending()) + "\nJob length (/year): " + str(self.length())


class Actuary:

    def __init__(self):

        self.name = ''
        self.link = ''
        self.description = ''
        self.career = list()
        self.education = list()
        self.birthday_appr = None

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

    def add_job(self, job):

        try:
            assert (isinstance(job, Job))

            career_update = self.career
            career_update = career_update.append(job)
            self.career = career_update

        except AssertionError:
            print("This is not a job with the Job class -> Not possible")

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


a = Job()
print(a.beginning())
print(a)
a.beginning()
a.ending()
a.beginning()
a.change_time_beginning('Jun 2005a')
a.change_time_beginning('Jun 2005')
a.change_time_ending('Jun 2005a')
a.change_time_ending('Jun 2005')
a.beginning()
a.ending()
a.length()

a.name
a.change_name('BNB')
