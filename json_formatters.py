def sections_json(los):
    for_all = ""
    for section in los:
        formatted = section.json_format()
        for_all = for_all + formatted
    return for_all