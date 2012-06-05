#!/bin/python
import re, json, sys

strip_entities = True

def strip_items(str, start_pos, end_pos):
  return str[0:start_pos]+str[end_pos:]

for itm in sys.stdin:
  line = itm.strip()
  try:
    data = json.loads(line)
  except:
		# can't always convert the raw data to json. silently fail and move on
    continue
  txt=data['text']

  # using the start and end positions supplied by twitter, 
  # remove any entities from the tweet (hashtags/urls/@mentions)
  # using the start/end positions should be faster than a regex
  # grab the start/end position of each entitiy and then add to
  # the list tostrip
  # the entity positions can arrive in any order.
  if strip_entities:
    to_strip=[]
    entities=data['entities']
    for k,v in entities.iteritems():
      for ent in v: 
        try:
          (start_pos,end_pos)=ent['indices']
          tostrip.append((start_pos,end_pos))

        except KeyError:
          # no entities/indicies. pass
          pass
    
    # reverse sort the list so that we're working backwards
    # on the original tweet. remove items from the tweet
    # by using simple string slicing

    for x in sorted(to_strip, reverse=True):
      txt = strip_items(txt, *x)
  
  # using a regex, extract numbers from the tweet text. iterate
  # through the numbers, cast as a long (to strip multiple leading zeros)
  # and print to stdout.
  
  numbers = re.findall(r'\b\d+\b', txt)
  for number in numbers:
    number = long(number)
    print number


      
