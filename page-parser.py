import pathlib
import numpy as np

MONTHS = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6, 'july':7, 'august':8, 'september':9, 'october':10, 'november':11, 'december':12}

def is_month(text):
    return text.lower() in MONTHS.keys()

def parse_video_game_page(lines):
    """
    Parameters:
        text - Video game wikipedia page given in plaintext.
    Returns:
        List(date, event_text) - List of events with date.
    """

    # Skip first line, represents columns
    events = []
    lines = lines[1:]
    CURRENT_MONTH = 1
    CURRENT_DAY = 1
    event_spanning_two_months = False
    event_text = None
    for line in lines:
        parts = line.split('\t')
        parts_pointer = 0
        
        if event_spanning_two_months:
            month_string = parts[0]
            day_string = parts[1]
            events.append({'START_DATE': (CURRENT_DAY, CURRENT_MONTH), 'END_DATE': (int(day_string), MONTHS[month_string.lower()]), 'EVENT': event_text})
            CURRENT_MONTH = MONTHS[month_string.lower()]
            event_spanning_two_months = False
        else:
            potential_month = parts[parts_pointer]
            if is_month(potential_month):
                CURRENT_MONTH = MONTHS[potential_month.lower()]
                parts_pointer += 1
            
            potential_day = parts[parts_pointer]
            day_range_line = potential_day.find('â€“')
            if day_range_line != -1:
                start_day = int(potential_day[:day_range_line])
                if day_range_line + 3 == len(potential_day):
                    event_spanning_two_months = True
                    CURRENT_DAY = start_day
                else:
                    end_day = int(potential_day[day_range_line + 3:])
                    CURRENT_DAY = (start_day, end_day)
                parts_pointer += 1
            else:
                if potential_day.isnumeric():
                    CURRENT_DAY = int(potential_day)
                    parts_pointer += 1
            
            event_text = parts[parts_pointer]
            if not event_spanning_two_months:
                if isinstance(CURRENT_DAY, int):
                    events.append({'START_DATE': (CURRENT_DAY, CURRENT_MONTH), 'END_DATE': (CURRENT_DAY, CURRENT_MONTH), 'EVENT': event_text})
                else:
                    events.append({'START_DATE': (CURRENT_DAY[0], CURRENT_MONTH), 'END_DATE': (CURRENT_DAY[1], CURRENT_MONTH), 'EVENT': event_text})
    
    return events
            
            

def main():
    path = pathlib.Path(__file__).resolve().parent.joinpath('topics', 'video-games', '2021.txt').__str__()
    file = open(path, 'r')
    events = parse_video_game_page(list(file.readlines()))
    print(events)
    for event in events:
        print(event)

if __name__ == '__main__':
    main()