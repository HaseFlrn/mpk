def any_of(a, f):
  '''Erwartet ein Array a und eine Funktion f.
      Liefert True, wenn f(el) == True für irgend ein el in a gilt.
  '''
  return any(map(f,a))


def even(x):
  '''Liefert True, falls x eine gerade Zahl ist.'''
  return x % 2 == 0


def test_any_of():
  a1 = [1,3,5,7,9]
  a2 = [1,2,3,4,5]
  assert(any_of(a1,even) == False)
  assert(any_of(a2,even) == True)

if __name__ == "__main__":
  test_any_of()
  