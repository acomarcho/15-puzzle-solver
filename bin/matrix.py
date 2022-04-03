import numpy as np

class Matrix:
  def __init__(self, arr = [], stepsBefore = [], steps = 0, _g = -1, loc = -1):
    '''
      Konstruktor untuk matriks
    '''
    self.arr = arr
    self.stepsBefore = stepsBefore
    self.steps = steps
    self.locationMap = {}
    self.kurangMap = {}
    self.kurangSum = 0
    self._g = _g
    self.loc = loc
    if (self._g == -1):
      self.fillLocationMap()
  def id(self):
    '''
      Mengembalikan ID unik untuk matriks
    '''
    return self.arr.tobytes()
  def __lt__(self, other):
    '''
      Menentukan matriks mana yang costnya lebih kecil.
      Apabila cost matriks sama, matriks yang lebih dalam (f lebih besar) dianggap lebih kecil.
    '''
    return self.f() >= other.f() if self.c() == other.c() else self.c() < other.c()
  def fillLocationMap(self):
    '''
      Mengisi locationMap
    '''
    self._g = 0
    for i in range(16):
      self.locationMap[self.arr[i]] = i
      if (self.arr[i] - 1 != i and self.arr[i] != 16):
        self._g += 1
    self.loc = self.locationMap[16]
  def countAllKurang(self):
    '''
      Menghitung Kurang(i) untuk setiap i
      serta mencetaknya ke layar
    '''
    for i in range(1, 17):
      # Iterasi dari [1 ... 16]
      kurang = 0
      for j in range(1, i):
        # Iterasi dari [1 ... i - 1]
        if self.locationMap[j] > self.locationMap[i]:
          kurang += 1
      self.kurangSum += kurang
      self.kurangMap[i] = kurang
  def getXValue(self):
    '''
      Menghitung nilai dari X
    '''
    pos = self.locationMap[16]
    if pos == 1 or pos == 3 or pos == 4 or pos == 6 or pos == 9 or pos == 11 or pos == 12 or pos == 14:
      return 1
    else:
      return 0
  def getKurangPlusX(self):
    '''
      Mengembalikan nilai sum Kurang(i) + X
    '''
    return self.kurangSum + self.getXValue()
  def isGoalReachable(self):
    '''
      Mengecek apakah nilai sum Kurang(i) + X genap
    '''
    return self.getKurangPlusX() % 2 == 0
  def f(self):
    '''
      Menghitung nilai taksiran f
    '''
    return self.steps
  def g(self):
    '''
      Menghitung nilai taksiran g
    '''
    return self._g
  def c(self):
    '''
      Menghitung nilai taksiran c
    '''
    return self.f() + self.g()
  def isSolved(self):
    '''
      Menentukan apakah taksiran g = 0
    '''
    return self.g() == 0
  def canMoveUp(self):
    '''
      Menentukan apakah petak kosong bisa bergerak ke atas
    '''
    pos = self.loc
    return not (pos >= 0 and pos <= 3)
  def canMoveDown(self):
    '''
      Menentukan apakah petak kosong bisa bergerak ke bawah
    '''
    pos = self.loc
    return not (pos >= 12 and pos <= 15)
  def canMoveRight(self):
    '''
      Menentukan apakah petak kosong bisa bergerak ke kanan
    '''
    pos = self.loc
    return not (pos == 3 or pos == 7 or pos == 11 or pos == 15)
  def canMoveLeft(self):
    '''
      Menentukan apakah petak kosong bisa bergerak ke kanan
    '''
    pos = self.loc
    return not (pos == 0 or pos == 4 or pos == 8 or pos == 12)
  def createMoveUp(self):
    '''
      Mengembalikan matriks yang petak kosongnya digeser satu ke atas
    '''
    # Copy matriks lama
    newArr = np.copy(self.arr)
    pos = self.loc
    # Hitung nilai g baru
    newG = self.g()
    if (newArr[pos - 4] - 1 == pos):
      newG -= 1
    elif (newArr[pos - 4] - 1 == pos - 4):
      newG += 1
    # Swap newArr[pos] dengan newArr[pos - 4]
    newArr[pos], newArr[pos - 4] = newArr[pos - 4], newArr[pos]
    # Update pos
    pos -= 4
    return Matrix(newArr, self.stepsBefore + ["up"], self.steps + 1, newG, pos)
  def createMoveDown(self):
    '''
      Mengembalikan matriks yang petak kosongnya digeser satu ke bawah
    '''
    # Copy matriks lama
    newArr = np.copy(self.arr)
    pos = self.loc
    # Hitung nilai g baru
    newG = self.g()
    if (newArr[pos + 4] - 1 == pos):
      newG -= 1
    elif (newArr[pos + 4] - 1 == pos + 4):
      newG += 1
    # Swap newArr[pos] dengan newArr[pos + 4]
    newArr[pos], newArr[pos + 4] = newArr[pos + 4], newArr[pos]
    # Update pos
    pos += 4
    return Matrix(newArr, self.stepsBefore + ["down"], self.steps + 1, newG, pos)
  def createMoveRight(self):
    '''
      Mengembalikan matriks yang petak kosongnya digeser satu ke kanan
    '''
    # Copy matriks lama
    newArr = np.copy(self.arr)
    pos = self.loc
    # Hitung nilai g baru
    newG = self.g()
    if (newArr[pos + 1] - 1 == pos):
      newG -= 1
    elif (newArr[pos + 1] - 1 == pos + 1):
      newG += 1
    # Swap newArr[pos] dengan newArr[pos + 1]
    newArr[pos], newArr[pos + 1] = newArr[pos + 1], newArr[pos]
    # Update pos
    pos += 1
    return Matrix(newArr, self.stepsBefore + ["right"], self.steps + 1, newG, pos)
  def createMoveLeft(self):
    '''
      Mengembalikan matriks yang petak kosongnya digeser satu ke kiri
    '''
    # Copy matriks lama
    newArr = np.copy(self.arr)
    pos = self.loc
    # Hitung nilai g baru
    newG = self.g()
    if (newArr[pos - 1] - 1 == pos):
      newG -= 1
    elif (newArr[pos - 1] - 1 == pos - 1):
      newG += 1
    # Swap newArr[pos] dengan newArr[pos - 1]
    newArr[pos], newArr[pos - 1] = newArr[pos - 1], newArr[pos]
    # Update pos
    pos -= 1
    return Matrix(newArr, self.stepsBefore + ["left"], self.steps + 1, newG, pos)