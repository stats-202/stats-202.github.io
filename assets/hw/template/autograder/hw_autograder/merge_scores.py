import collections
import json
from typing import Any, Dict, Text

import numpy as np

PYTHON_SCORES_FILE = './results-python.json'
R_SCORES_FILE = './results-R.json'
PRECISION = 2

# Load results
def load_scores(filename):
  """Loads json files."""
  with open(filename) as f:
    scores = json.load(f)
    if not 'tests' in scores:
      raise AttributeError("'tests' key not in: %s" % filename)

  return scores

# Merge results
def get_exercise_number(result: Dict[Text, Any]) -> Text:
  """Returns the exercise number."""
  first_three_values = []
  name = result.get('name', '')
  if name:
    first_three_values = name.split(':')[0].split('.')[:3]
  return '.'.join(first_three_values)

def group_scores_python(scores):
  """Groups individual python tests into exercise scores."""
  grouped_results = {}
  for result in scores.get('tests'):
    section = get_exercise_number(result)
    if not section == 'Check submitted files':
      if section not in grouped_results:
        grouped_results[section] = {'score': 0, 'max_score': 0,
                                    'output': ''}
      grouped_results[section]['score'] += result.get('score')
      grouped_results[section]['max_score'] += result.get('max_score')
      grouped_results[section]['output'] += result.get('output', '')
      grouped_results[section]['visibility'] = result.get('visibility')

  return grouped_results

def group_scores_r(scores):
  """Groups individual R tests into exercise scores."""
  grouped_results = {}
  for result in scores.get('tests'):
    section = get_exercise_number(result)
    if section not in grouped_results:
      grouped_results[section] = {'percent': []}
    grouped_results[section]['percent'].append(result.get('percent'))

  return grouped_results

def merge_scores(grouped_scores_r, grouped_scores_python, scores_python):
  """Merges R and python results."""
  joint_keys = (set(grouped_scores_r.keys()) |
                set(grouped_scores_python.keys()))
  merged_results = {'tests': []}
  for key in joint_keys:
    result_python = grouped_scores_python.get(key)
    result_r = grouped_scores_r.get(key)
    result = collections.OrderedDict()
    result['name'] = key
    for value in ['score', 'max_score', 'visibility']:
      if value in ['score', 'max_score']:
        result[value] = round(result_python.get(value), PRECISION)
      else:
        result[value] = result_python.get(value)

    r_score = round(np.mean(result_r.get('percent')) *
                    result_python.get('max_score'), PRECISION)
    result['score'] = max(result['score'], r_score)
    merged_results['tests'].append(dict(result))

  for key, value in scores_python.items():
    if not key in ['tests', 'score']:
      merged_results[key] = scores_python.get(key)
      merged_results[key] = scores_python.get(key)
      merged_results[key] = scores_python.get(key)

  merged_results['score'] = 0.0
  for test in merged_results['tests']:
    merged_results['score'] += test.get('score')

  return merged_results

def main():
  scores_python = load_scores(PYTHON_SCORES_FILE)
  grouped_scores_python = group_scores_python(scores_python)

  scores_r = load_scores(R_SCORES_FILE)
  grouped_scores_r = group_scores_r(scores_r)

  merged_results = merge_scores(grouped_scores_r, grouped_scores_python,
                                scores_python)

  return merged_results


if __name__ == '__main__':
    merged_results = main()
    print(json.dumps(merged_results, indent=4))
