import json
from datetime import datetime, timezone

print('Deliberate Action - Plan, Do, Reflect - and Learn')
print('.... Refine your mental models ....')

time_allotment = 25
time_unit = 'minutes'

goal = input(f'What do you plan to do in the next {time_allotment} {time_unit}? ')
starttime = datetime.now(timezone.utc)

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
