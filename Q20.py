dictionary = {"merry":"god", "christmas":"jul", "and":"och", 
"happy":"gott", "new":"nytt", "year":"ar"}

def translate(lst):
  return [dictionary[w.lower()] for w in lst if w.lower() in dictionary]
if __name__ == '__main__':
    print(translate(['Merry', 'christmas', 'and', 'happy', 'new', 'year', 'mom']))