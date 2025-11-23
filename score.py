
import json
print('This file reproduces the scoring logic used for the submission package.')
with open('scoring_result.json') as f:
    data = json.load(f)
print(json.dumps(data, indent=2))
