def grades(*data, situation=False):
    """
    Analyzes the grades of multiple students.

    :param data: receives all entered grades
    :param situation: (optional) defines if the class average is BAD, GOOD or AVERAGE.
    :return: dictionary if data is provided; otherwise, returns that there is no data
    """
    class_data = dict()
    if len(data) == 0:
        return 'No data to analyze.'
    else:
        class_data = {
            'total': len(data),
            'highest': max(data),
            'lowest': min(data),
            'average': round(sum(data) / len(data), 2)
        }

        if situation:
            if class_data['average'] < 5:
                class_data['situation'] = 'BAD'
            elif class_data['average'] > 7:
                class_data['situation'] = 'GOOD'
            else:
                class_data['situation'] = 'AVERAGE'

        return class_data


class_analysis = grades(5, 4, 2, 5, 9, 5.5)
class_analysis2 = grades(5, 4, 2, 5, 9, 5.5, situation=True)
class_analysis3 = grades()
print(class_analysis)
print(class_analysis2)
print(class_analysis3)
help(grades)

