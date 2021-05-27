class Department:

    def __init__(self, abbrev, name, courses = []):
        self.abbrev = abbrev
        self.name = name
        self.courses = courses

    def json_format(self):
        start = "<dept"
        tm1 = ' abbrev="' + str(self.abbrev) + '"'
        tm2 = ' name="' + self.name + '"'
        end = "</dept>"
        courses_formatted = self.json_handle_courses()
        final = start + tm1 + tm2 + ">" + courses_formatted + end
        return final

    def json_handle_courses(self):
        for_all = ""
        for course in self.courses:
            formatted = course.json_format()
            for_all = for_all + formatted
        return for_all

class Course:

    def __init__(self, number, name, descript, sections = []):
        self.number = number
        self.name = name
        self.course_desc = descript
        self.mincredits = 1
        self.maxcredits = 1
        self.gradetype = "normal"
        self.sections = sections


    def json_format(self):
        start = "<course"
        tm1 = ' number="' + str(self.number) + '"'
        tm2 = ' name="' + self.name + '"'
        tm3 = ' course_desc="' + self.course_desc + '"'
        tm4 = ' min-credits="' + str(self.mincredits) + '"'
        tm5 = ' max-credits="' + str(self.maxcredits) + '"'
        tm6 = ' grade-type="' + self.gradetype + '"'
        end = "</course>"
        sections_formatted = self.json_handle_sections()
        final = start + tm1 + tm2 + tm3 + tm4 + tm5 + tm6 + ">" + sections_formatted + end
        return final

    def json_handle_sections(self):
        for_all = ""
        for section in self.sections:
            formatted = section.json_format()
            for_all = for_all + formatted
        return for_all

class Section:

    def __init__(self, fake_crn, section_id, total_seats, seats_left,
                 max_waitlist, actual_waitlist, term, part_of_term, periods = []):
        self.crn = fake_crn
        self.number = section_id
        self.seats = total_seats
        self.availableseats = seats_left
        self.max_waitlist = max_waitlist
        self.actual_waitlist = actual_waitlist
        self.term = term
        self.part_of_term = part_of_term
        self.periods = periods

    def json_format(self):
        start = "<section"
        tm1 = ' crn="' + str(self.crn) + '"'
        tm2 = ' number="' + str(self.number) + '"'
        tm3 = ' seats="' + str(self.seats) + '"'
        tm4 = ' availableseats="' + str(self.availableseats) + '"'
        tm5 = ' max_waitlist="' + str(self.max_waitlist) + '"'
        tm6 = ' actual_waitlist="' + str(self.actual_waitlist) + '"'
        tm7 = ' term="' + str(self.term) + '"'
        tm8 = ' part-of-term="' + str(self.part_of_term) + '"'
        end = "</section>"
        periods_formatted = self.json_handle_periods()
        final = start + tm1 + tm2 +tm3 + tm4 + tm5 + tm6 +tm7 + tm8 + ">" + periods_formatted + end
        return final

    def json_handle_periods(self):
        for_all = ""
        for period in self.periods:
            formatted = period.json_format()
            for_all = for_all + formatted
        return for_all

class Period:

    def __init__(self, period_type, professor, days, start, end, bldg, room_and_CRN):
        self.period_type = period_type
        self.professor = professor
        self.professor_sort_name = professor
        self.professor_email = "wouldntyouliketoknow@weatherboy.edu"
        self.days = days
        self.starts = start
        self.ends = end
        self.building = bldg
        self.room = room_and_CRN

    def json_format(self):
        start = "<period"
        tm1 = ' type="' + str(self.period_type) + '"'
        tm2 = ' professor="' + str(self.professor) + '"'
        tm3 = ' professor_sort_name="' + str(self.professor_sort_name) + '"'
        tm4 = ' professor_email="' + str(self.professor_email) + '"'
        tm5 = ' days="' + str(self.days) + '"'
        tm6 = ' starts="' + str(self.starts) + '"'
        tm7 = ' ends="' + str(self.ends) + '"'
        tm8 = ' building="' + str(self.building) + '"'
        tm9 = ' room="' + str(self.room) + '"'
        end = "</period>"
        final = start + tm1 + tm2 +tm3 + tm4 + tm5 + tm6 +tm7 +tm8 + tm9 + ">" + end
        return final

