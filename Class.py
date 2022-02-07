from datetime import datetime
from calendar import monthrange

now = datetime.now()


# Class job

class Job:

    def __init__(self,date = datetime.now()):

        self.now = date

        self.name = ''
        self.company = ''
        self.description = ''
        self.time_beginning = datetime(self.now.year, self.now.month, monthrange(self.now.year, self.now.month)[1], 0, 0)
        self.time_ending = datetime(self.now.year, self.now.month, monthrange(self.now.year, self.now.month)[1], 0, 0)

    def beginning(self):

        time_beginning_ini = self.time_beginning
        return time_beginning_ini.strftime("%B %Y")

    def ending(self):

        time_ending_ini = self.time_ending
        return time_ending_ini.strftime("%B %Y")

    def length(self):

        try:
            assert((self.time_ending - self.time_beginning).days>=0)
            length = self.time_ending - self.time_beginning
            # return divmod(length.total_seconds(), 31536000)[0]
            return round(length.total_seconds()/31536000,1)

        except AssertionError:
            print("The length is negative -> Not possible")

    def change_company_name(self, name):

        try:
            assert(isinstance(name, str))
            self.company = name

        except AssertionError:
            print("The name of the company is not a string -> Not possible")

    def change_job_name(self, name):

        try:
            assert(isinstance(name, str))
            self.name = name

        except AssertionError:
            print("The name of the job is not a string -> Not possible")

    def change_time_beginning(self,date):

        try:
            datetime_beginning = datetime.strptime(date, '%b %Y')
            self.time_beginning = datetime_beginning

        except ValueError:
            print("The beginning date format is wrong")

    def change_time_ending(self,date):

        try:
            datetime_ending = datetime.strptime(date, '%b %Y')
            datetime_ending = datetime_ending.replace(day=monthrange(datetime_ending.year, datetime_ending.month)[1])
            self.time_ending = datetime_ending

        except ValueError:
            print("The ending date format is wrong")


    def __repr__(self):

        return "member of Test"
        #return(self.name)
        #print(self.company)
        #str(self.beginning())
        #str(self.ending())
        #str(self.length())
        #return 0

    def __str__(self):
        return "member of Test"




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