import json
from datetime import datetime, timezone
# from simpleaudio-alarm import ring
# import pydub-alarm
from simpleaudio_alarm import ring

print('Deliberate Action - Plan, Do, Reflect - and Learn')
print('.... Refine your mental models ....')

time_allotment = 25
time_unit = 'minutes'

goal = input(f'What do you plan to do in the next {time_allotment} {time_unit}? ')
ring()
starttime = datetime.now(timezone.utc)
session = {}
session['name'] = 'sample'
session['duration_in_millis'] = 1000
planned_sessions = {}

experience = input(f'What happened during the allotted time? ')
difference = input(f'What explains the difference? ')
action = input(f'What action can you take to improve outcomes? ')

report = {
   'start': f'{starttime}',
   'goal' : f'{goal}',
   'experience' : f'{experience}',
   'difference' : f'{difference}',
   'action' : f'{action}'
}

# convert into JSON:
y = json.dumps(report)

# the result is a JSON string:
print(y)
print(json.dumps(session))
