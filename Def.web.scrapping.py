import re

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

def Load_education_single(job_data):

    new_education = Study()
    # new_education.change_company_name(str.strip(job_data.find_next("h4").text))
    new_education.add_school_name(str.strip(job_data.find_next("h3").text))

    try:

        if len(job_data.find_next("h4").contents)==5:

            new_education.add_type_degree(re.search(">(.*?)<", str(text_single[0].find_next("h4").contents[1])).group(1))
            new_education.add_name_study(re.search(">(.*?)<", str(text_single[0].find_next("h4").contents[2])).group(1))

        elif len(job_data.find_next("h4").contents)==4:

            new_education.add_type_degree(re.search(">(.*?)<", str(job_data.find_next("h4").contents[1])).group(1))


    except ValueError:
        print("Could not find the type of degree and study name")

    try:

        time_education = re.findall("<time>(.*?)</time>", str(job_data.find_all("p", {"class": "education__item education__item--duration"}, limit=2)[0]))

        if len(time_education) == 1:

            new_education.change_time_beginning(time_education[0])

        elif len(time_education) == 2:

            new_education.change_time_beginning(time_education[0])
            new_education.change_time_ending(time_education[1])

    except ValueError:
        print("Could not find the right time value for education")


    return new_education


test = Load_job_single(text_single[0])
print(test)

test = Load_job_multi(text_group[0])
print(test[1])

test = Load_education_single(text_single[0])
print(Load_education_single(text_single[3]))




