def reformat_sheet(df):
    oldterm = df["Academic Period"].tolist()
    course_section_old = df["Course Section"].tolist()
    old_meeting_pattern = df["Meeting Patterns"].tolist()
    locations = df["Locations"].tolist()

    new_terms = []
    for each in oldterm:
        new_term = get_term(each)
        new_terms.append(new_term)

    part1s = []
    part2s = []
    part3s = []

    for each in course_section_old:
        splitup = split_long_names(each)
        first = splitup[0]
        second = splitup[1]
        third = splitup[2]
        part1s.append(first)
        part2s.append(second)
        part3s.append(third)

    df["Term"] = new_terms
    df["Course Code"] = part1s
    df["Course Section new"] = part2s
    df["Description"] = part3s

    depts = []
    for each in part1s:
        dept = each.split(' ')[0]
        depts.append(dept)

    df["Department"] = depts

    days = []
    starts = []
    ends = []
    for each in old_meeting_pattern:
        fixed = setup_days(each)
        days.append(fixed[0])
        starts.append(fixed[1])
        ends.append(fixed[2])

    df["Days"] = days
    df["Start Time"] = starts
    df["End Time"] = ends

    buildings = []
    rooms = []
    for each in locations:
        building, room = split_rooms(each)
        buildings.append(building)
        rooms.append(room)

    df["Building"] = buildings
    df["Room"] = rooms

    df.drop(columns=["Academic Period", "Course Section", "Course Section Owner", "Meeting Patterns", "Locations",
                     "Co-Located Course Sections", "Course Tags"], inplace=True)
    return df

def split_long_names(original_string):
    all_parts = []
    working_string = ""
    for char in original_string:
        if char == "-":
            all_parts.append(working_string)
            working_string = ""
        else:
            working_string = working_string + char
    all_parts.append(working_string)
    return all_parts

def get_term(original_string):
    if original_string == "2021 Fall A Term":
        return "A"
    elif original_string == "2021 Fall B Term":
        return "B"
    elif original_string == "2021 Fall Semester":
        return "AB"

def setup_days(original_string):
    try:
        split = str(original_string).split("|")
        days = remove_dashes(split[0])
        times = split[1]
        split2 = times.split("-")
        start = split2[0]
        end = split2[1]
        strip_start = start.replace(" ", "")
        strip_end = end.replace(" ", "")
        fixed_days = fix_days(days)
    except:
        fixed_days = "?"
        strip_start = "?"
        strip_end = "?"
    return fixed_days, strip_start, strip_end

def remove_dashes(days):
    newstring = ""
    for char in days:
        if char != "-":
            newstring = newstring + char
    return newstring

days_dict = {"M": "mon", "T": "tue", "R": "thu", "F": "fri", "W": "wed"}
def fix_days(days):
    return_string = ""
    for char in days:
        if char in days_dict.keys():
            return_string = return_string + days_dict[char] + ","
    return return_string[:-1]

def split_rooms(room_string):
    try:
        start_digit_index = len(room_string) + 1
        end_digit_index = - (len(room_string) + 1)
        found_end = False
        for i in range(len(room_string)):
            char = room_string[i]
            if char.isdigit():
                start_digit_index = min(start_digit_index, i)
                if not found_end:
                    end_digit_index = max(end_digit_index, i)
            elif i == end_digit_index + 1:
                    found_end = True
        part1 = room_string[:start_digit_index]
        part2 = room_string[start_digit_index : end_digit_index + 1]
    except:
        part1 = room_string
        part2 = " "
    return part1, part2

def get_dept_code(dept_string):
    first_digit_index = None
    for i in range(len(dept_string)):
        char = dept_string[i]
        if char.isdigit():
            first_digit_index = i
            break
    short_dept = dept_string[:first_digit_index]
    return short_dept