def Load_job_single_connected(job_data):
    new_job = Job()
    company_name_temp = job_data.find_next("span", {"class": "t-14 t-normal"}).find_next("span").text
    if company_name_temp.find(' ·')!=-1:
        company_name_temp = company_name_temp.rpartition(' ·')[0]
    new_job.change_company_name(company_name_temp)
    new_job.change_job_name(job_data.find_next("span", {"class": "t-bold mr1"}).find_next("span").text)

    try:
        assert (job_data.find_next("span", {"class": "t-14 t-normal t-black--light"}).find_next("span").text.rpartition(' · ')[0] != '')
        date_temp = job_data.find_next("span", {"class": "t-14 t-normal t-black--light"}).find_next("span").text.rpartition(' · ')[0]
        if date_temp.find('- Present')==-1:
            if date_temp.rpartition(' - ')[0] != '':
                new_job.change_time_beginning(date_temp.rpartition(' - ')[0])
                new_job.change_time_ending(date_temp.rpartition(' - ')[2])
            elif date_temp.rpartition(' - ')[0] == '':
                new_job.change_time_beginning(date_temp)
                new_job.change_time_ending(date_temp)
        elif date_temp.find('- Present')!=-1:
            new_job.change_time_beginning(date_temp.rpartition(' - ')[0])

    except AssertionError:
        print("'data-section' not 'pastPositionsDetails' or 'currentPositionsDetails' -> Not possible")

    return new_job

def Load_job_multi_connected(job_data):
    list_job = list()
    list_div = job_data.find_all("div", {"class": "display-flex flex-column full-width align-self-center"})

    for i in range(1,len(list_div)):

        new_job = Job()

        new_job.change_company_name(job_data.find_next("span", {"class": "t-bold mr1 hoverable-link-text"}).find_next("span").text)
        new_job.change_job_name(list_div[i].find_next("span", {"class": "t-bold mr1 hoverable-link-text"}).find_next("span").text)

        try:
            assert (list_div[i].find_next("span", {"class": "t-14 t-normal t-black--light"}).find_next("span").text.rpartition(' · ')[0] != '')
            date_temp = list_div[i].find_next("span", {"class": "t-14 t-normal t-black--light"}).find_next("span").text.rpartition(' · ')[0]
            if date_temp.find('- Present')==-1:
                new_job.change_time_beginning(date_temp.rpartition(' - ')[0])
                new_job.change_time_ending(date_temp.rpartition(' - ')[2])
            elif date_temp.find('- Present') != -1:
                new_job.change_time_beginning(date_temp.rpartition(' - ')[0])

            list_job.append(new_job)

        except AssertionError:
            print("'data-section' not 'pastPositionsDetails' or 'currentPositionsDetails' -> Not possible")

    return list_job

def Load_education_single_connected(education_data):
    new_education = Study()

    new_education.add_school_name(education_data.find_next("span", {"class": "t-bold mr1 hoverable-link-text"}).find_next("span").text)

    try:
        name_temp = education_data.find_next("span", {"class": "t-14 t-normal"}).find_next("span").text
        if name_temp.find(',')!=-1:
            try:
                new_education.add_type_degree(name_temp.rpartition(', ')[0])
            except AttributeError:
                pass

            try:
                if (name_temp.rpartition(', ')[2] not in (' ', '  ')):
                    new_education.add_name_study(name_temp.rpartition(', ')[2])
            except AttributeError:
                pass

            # except AssertionError:
            #     print("Could not find the right second name for education")


        elif name_temp.find(',')==-1:
            if (name_temp not in (' ', '')):
                new_education.add_name_study(name_temp)

    except ValueError:
        print("Could not find the type of degree and study name")

    try:

        time_education = education_data.find_next("span", {"class": "t-14 t-normal t-black--light"}).find_next("span").text

        if time_education.find('- Present')!=-1:

            new_education.change_time_beginning(time_education.rpartition(' - ')[0][-4:])

        elif time_education.find('- Present') == -1:

            new_education.change_time_beginning(time_education.rpartition(' - ')[0][-4:])

            if time_education.rpartition(' - ')[0][-4:] != time_education.rpartition(' - ')[2][-4:]:
                new_education.change_time_ending(time_education.rpartition(' - ')[2][-4:])

    except ValueError:
        print("Could not find the right time value for education")

    return new_education

def Load_actuary_connected(soup, url):
    ### Data partitioning ###

    # Initialization class Actuary
    new_actuary = Actuary()

    # Set up names and description data

    identity_data = soup.find_all("div", {"class": "mt2 relative"})

    # Set up career data
    temporary_sections = soup.find_all("section", {"class": "artdeco-card ember-view break-words pb3 mt4"},limit=4)

    if temporary_sections[2].find_all("h2",{"class": "pvs-header__title text-heading-large"})[0].find_next("span").text=='Experience':
        my_career_uls = temporary_sections[2].find_all("li", {"class": "artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column"})
    if temporary_sections[3].find_all("h2",{"class": "pvs-header__title text-heading-large"})[0].find_next("span").text=='Experience':
        my_career_uls = temporary_sections[3]

    # Set up education data

    # Education

    if temporary_sections[2].find_all("h2",{"class": "pvs-header__title text-heading-large"})[0].find_next("span").text=='Education':
        my_education_uls = temporary_sections[2].find_all("li", {"class": "artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column"})
    if temporary_sections[3].find_all("h2",{"class": "pvs-header__title text-heading-large"})[0].find_next("span").text=='Education':
        my_education_uls = temporary_sections[3]

    data_study = my_education_uls.find_all("div", {"class": "pvs-entity pvs-entity--padded pvs-list__item--no-padding-when-nested"})

    ### Data extraction ###

    # Name
    new_actuary.add_name(str.strip(identity_data[0].find_next("h1").text))
    # Title
    new_actuary.add_title(str.strip(identity_data[0].find_all("div", {"class": "text-body-medium break-words"})[0].text))
    # Connections
    connections_temp = soup.find_all("ul", {"class": "pv-top-card--list pv-top-card--list-bullet display-flex pb1"})[0].find_next("span").find_next("span").text
    if connections_temp.find(' connections') != -1:
        new_actuary.add_connection(connections_temp)
    elif connections_temp.find(' connections') == -1:
        new_actuary.add_connection(connections_temp + ' connections')
    # Location
    new_actuary.add_location(str.strip(soup.find_all("div", {"class": "pb2 pv-text-details__left-panel"})[0].find_next("span").text))
    # Link
    new_actuary.add_link(url)

    # Add job experience


    for i in range(len(my_career_uls)):
        iter_state = 0
        iter_state = len(my_career_uls[i].find_all("div", {"class": "display-flex flex-row justify-space-between"}))
        if (iter_state > 1):
            update_multi = Load_job_multi_connected(my_career_uls[i])
            for j in range(len(update_multi)):
                new_actuary.add_job(update_multi[j])
            del update_multi
        elif (iter_state == 1):
            update_single = Load_job_single_connected(my_career_uls[i])
            new_actuary.add_job(update_single)
            del update_single

    # Add education

    for k in range(len(data_study)):
        update_single = Load_education_single_connected(data_study[k])
        new_actuary.add_education(update_single)
        del update_single

    # Try to initialize approximated age
    new_actuary.get_birthday_appr()

    return new_actuary