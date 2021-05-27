from objects import Department, Course, Section, Period

def make_all_objects(formatted_df, depts_ref, locations_ref):
    dept_objects = {}
    all_depts = depts_ref["Department Code"].tolist()
    long_names = depts_ref["Long Name"]
    for i in range(len(all_depts)):
        dept = all_depts[i]
        long_name = long_names[i]
        dept_obj = Department(dept, long_name)
        dept_objects[dept] = dept_obj
    return dept_objects

def make_dept_objects_dict(depts_ref):
    dept_objects = {}
    all_depts = depts_ref["Department Code"].tolist()
    long_names = depts_ref["Long Name"]
    for i in range(len(all_depts)):
        dept = all_depts[i]
        long_name = long_names[i]
        dept_obj = Department(dept, long_name)
        dept_objects[dept] = dept_obj
    return dept_objects

def populate_courses(formatted_df, depts_dict):
    departments = formatted_df["Department"].tolist()
    codes = formatted_df["Course Code"].tolist()
    descripts = formatted_df["Description"].tolist()
    enroll = formatted_df["Enrollment Count"].tolist()
    capacity = formatted_df["Section Capacity"].tolist()
    waitlist = formatted_df["Waitlist Count"].tolist()
    waitlist_cap = formatted_df["Wait List Capacity"].tolist()
    numbers = formatted_df["Course Section new"].tolist()
    terms = formatted_df["Term"].tolist()
    period_types = formatted_df["Instructional Format"].tolist()
    professors = formatted_df["Instructors"].tolist()
    days = formatted_df["Days"].tolist()
    starts = formatted_df["Start Time"].tolist()
    ends = formatted_df["End Time"].tolist()
    bldgs = formatted_df["Building"].tolist()
    rooms = formatted_df["Room"].tolist()

    fake_CRN = 12345
    for i in range(len(departments)):
        dept = departments[i]
        coursecode = codes[i]
        num = get_coursenum(dept, coursecode)
        name = descripts[i]
        course_obj = Course(num, name, name)

        fake_CRN = fake_CRN + 1
        number = numbers[i][:-1]
        seats = capacity[i]
        avail = capacity[i] - enroll[i]
        max_waitlist = waitlist_cap[i]
        actual_waitlist = waitlist[i]
        term, part_term = format_term(terms[i])
        section = Section(fake_CRN, number, seats, avail, max_waitlist, actual_waitlist, term, part_term )

        period_type = period_types[i]
        professor = professors[i]
        day = days[i]
        start = starts[i]
        end = ends[i]
        bldg = bldgs[i]
        room = rooms[i]
        period = Period(period_type, professor, day, start, end, bldg, room)

        section.periods = [period]
        course_obj.sections = [section]

        dept_obj = depts_dict[dept]
        newlist = dept_obj.courses + [course_obj]
        dept_obj.courses = newlist
    return depts_dict

def get_coursenum(dept, coursecode):
    new = coursecode.replace(dept + " ", "")
    return new

def format_term(term):
    if "A" in term or "B" in term:
        semester = 202101
    else:
        semester = 202202
    part_term = ""
    for letter in term:
        part_term = part_term + letter + " Term,"
    new_part_term = part_term[:-1]
    return semester, new_part_term