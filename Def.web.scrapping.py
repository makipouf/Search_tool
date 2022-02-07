
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

test = Load_job_single(text.single[0])
