#!/bin/python
import re, json, sys
debug = False
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
  tostrip=[]
  entities=data['entities']
  for k,v in entities.iteritems():
    for ent in v: 
      try:
        (start_pos,end_pos)=ent['indices']
        tostrip.append((start_pos,end_pos))

      except KeyError:
        # no entities/indicies. pass
        print "error hre"
        pass

  for x in sorted(tostrip, reverse=True):
    txt = strip_items(txt, *x)
  
  if debug:
    print 'original tweet: %s' % data['text']
    print 'modified tweet: %s' % txt  
  numbers = re.findall(r'\b\d+\b', txt)
  for number in numbers:
    number = long(number)
    print number


      
