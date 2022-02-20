import re
from class_actuary import *

def Load_job_single(job_data):
    new_job = Job()
    new_job.change_company_name(str.strip(job_data.find_next("h4").text))
    new_job.change_job_name(str.strip(job_data.find_next("h3").text))

    try:
        assert (job_data.get("data-section") in ('pastPositionsDetails', 'currentPositionsDetails'))

        if (job_data.get("data-section") == 'pastPositionsDetails'):
            new_job.change_time_beginning(job_data.find_next("time").text)
            new_job.change_time_ending(job_data.find_next("time").find_next("time").text)
        elif (job_data.get("data-section") == 'currentPositionsDetails'):
            new_job.change_time_beginning(job_data.find_next("time").text)

    except AssertionError:
        print("'data-section' not 'pastPositionsDetails' or 'currentPositionsDetails' -> Not possible")

    return new_job

def Load_job_multi(job_data):

    list_job = list()
    list_li = job_data.find_all("li")

    for i in range(len(job_data.find_all("li"))):

        new_job = Job()

        new_job.change_company_name(str.strip(job_data.find_next("h4").text))
        new_job.change_job_name(str.strip(list_li[i].find_next("h3").text))

        try:
            assert (list_li[i].get("data-section") in ('pastPositionsDetails', 'currentPositionsDetails'))

            if (list_li[i].get("data-section") == 'pastPositionsDetails'):
                new_job.change_time_beginning(list_li[i].find_next("time").text)
                new_job.change_time_ending(list_li[i].find_next("time").find_next("time").text)
            elif (list_li[i].get("data-section") == 'currentPositionsDetails'):
                new_job.change_time_beginning(list_li[i].find_next("time").text)

            list_job.append(new_job)

        except AssertionError:
            print("'data-section' not 'pastPositionsDetails' or 'currentPositionsDetails' -> Not possible")

    return list_job

def Load_education_single(education_data):

    new_education = Study()
    # new_education.change_company_name(str.strip(job_data.find_next("h4").text))
    new_education.add_school_name(str.strip(education_data.find_next("h3").text))

    try:

        if len(education_data.find_next("h4").contents)==5:

            new_education.add_type_degree(re.search(">(.*?)<", str(education_data.find_next("h4").contents[1])).group(1))


            if (str(education_data.find_next("h4").contents[2]) not in (' ', '  ')):
                new_education.add_name_study(re.search(">(.*?)<", str(education_data.find_next("h4").contents[2])).group(1))

            # except AssertionError:
            #     print("Could not find the right second name for education")

        elif len(education_data.find_next("h4").contents)==4:

            new_education.add_type_degree(re.search(">(.*?)<", str(education_data.find_next("h4").contents[1])).group(1))


    except ValueError:
        print("Could not find the type of degree and study name")

    try:

        time_education = re.findall("<time>(.*?)</time>", str(education_data.find_all("p", {"class": "education__item education__item--duration"}, limit=2)[0]))

        if len(time_education) == 1:

            new_education.change_time_beginning(time_education[0])

        elif len(time_education) == 2:

            new_education.change_time_beginning(time_education[0])

            if (time_education[1]!=time_education[0]):
                new_education.change_time_ending(time_education[1])

    except ValueError:
        print("Could not find the right time value for education")

    return new_education

def Load_actuary(soup,url):

    ### Data partitioning ###

    # Initialization class Actuary
    new_actuary = Actuary()

    # Set up names and description data

    identity_data = soup.find_all("div", {"class": "top-card-layout__entity-info"})

    # Set up career data

    my_career_uls = soup.find_all("ul", {"class": "experience__list"}, limit=2)

    data_job =  my_career_uls[0].find_all("li", {"class": ("profile-section-card experience-item","experience-group experience-item")})
    data_single_job = my_career_uls[0].find_all("li", {"class": "profile-section-card experience-item"})
    data_group_job = my_career_uls[0].find_all("li", {"class": "experience-group experience-item"})

    # Set up education data

    # Education

    my_education_uls = soup.find_all("ul", {"class": "education__list"}, limit=2)

    data_study = my_education_uls[0].find_all("li", {"class": "profile-section-card education__list-item"})

    ### Data extraction ###

    # Name
    new_actuary.add_name(str.strip(identity_data[0].find_next("h1").text))
    # Title
    new_actuary.add_title(str.strip(identity_data[0].find_next("h2").text))
    # Connections
    new_actuary.add_connection(identity_data[0].find_next("h3").find_next("span").find_next("span").text)
    # Location
    new_actuary.add_location(identity_data[0].find_next("h3").find_next("span").text)
    # Link
    new_actuary.add_link(url)

    # Add job experience

    iter_group = 0
    iter_single = 0

    for i in range(len(data_job)):
        iter_class = data_job[i].get("class")[0]
        if(iter_class=='experience-group'):
            update_multi = Load_job_multi(data_group_job[iter_group])
            for j in range(len(update_multi)):
                new_actuary.add_job(update_multi[j])
                iter_group += 1
            del update_multi
        elif(iter_class=='profile-section-card'):
            update_single = Load_job_single(data_single_job[iter_single])
            new_actuary.add_job(update_single)
            iter_single += 1
            del update_single

    # Add job experience

    for k in range(len(data_study)):
        update_single = Load_education_single(data_study[k])
        new_actuary.add_education(update_single)
        del update_single

    # Try to initialize approximated age
    new_actuary.add_birthday_appr()

    return new_actuary

# if __name__ == '__main__':
#     student = Load_actuary(soup,driver.current_url)
#     student.name
#     student.title
#     student.connection
#     student.location
#     student.link
#     student.add_
#     student.add_birthday_appr()
#     student.birthday_appr
#     now=datetime.now()
#     student.birthday_appr()
#     print(student)
#     str(relativedelta(now, student.birthday_appr).years) + ' years'
#     for i in range(len(student.career)):
#         print("\n")
#         print(student.career[i])
#
#     for i in range(len(student.education)):
#         print("\n")
#         print(student.education[i])
#
#
#
#     for i in range(len(student.education)):
#         print("\n")
#         print(student.education[i].type_degree)
#         print(student.education[i].beginning())
#
#     test = Load_job_single(text_single_job[0])
#     print(test)
#
#     test = Load_job_multi(text_group[0])
#     print(test[1])
#
#     test = Load_education_single(text_single_study[0])
#     print(Load_education_single(text_single_study[0]))
#
#
#     student = Actuary()
#     student.add_name('Gaétan')
#     student.add_job(test)
#     student.career[0].name
#     print(student.career[0])
#
#     # Name
#     str.strip(identity_raw[0].find_next("h1").text)
#     # Title
#     str.strip(identity_raw[0].find_next("h2").text)
#     # Connection
#     identity_raw[0].find_next("h3").find_next("span").find_next("span").text
#     # Location
#     identity_raw[0].find_next("h3").find_next("span").text
#     # Link
#     driver.current_url










