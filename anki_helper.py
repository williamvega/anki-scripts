import codecs
import re
import os

class AnkiHelper:
  
  def __init__(self):
    self.name = "AnkiHelper"
  
  
  def replace_nth(s, sub, repl, n):
      # from https://stackoverflow.com/questions/35091557/replace-nth-occurrence-of-substring-in-string
      find = s.find(sub)
      # If find is not -1 we have found at least one match for the substring
      i = find != -1
      # loop util we find the nth or we find no match
      while find != -1 and i != n:
          # find + 1 means we start searching from after the last match
          find = s.find(sub, find + 1)
          i += 1
      # If i is equal to n we found nth match so replace
      if i == n:
          return s[:find] + repl + s[find+len(sub):]
      return s

  