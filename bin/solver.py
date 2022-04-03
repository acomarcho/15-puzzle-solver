from queue import PriorityQueue
import numpy as np
import timeit
from matrix import Matrix
import eel
    
if __name__ == '__main__':
  matrix = None
  pq = None
  visitedMap = None
  nodeCount = None
  sol = None
  matrices = None
  currentStep = None

  @eel.expose
  def reinitialize():
    '''
      Menginisialisasi ulang semua global variable
    '''
    global matrix
    global pq
    global visitedMap
    global nodeCount
    global sol
    global matrices
    global currentStep
    matrix = None
    pq = None
    visitedMap = None
    sol = None
    nodeCount = None
    matrices = None
    currentStep = None
    eel.go_to("home.html")

  def startSolver():
    '''
      Mulai GUI
    '''
    eel.init("web")
    eel.start("home.html", size = (640, 640))

  @eel.expose
  def pyOpenTC(tc):
    '''
      Buka TC yang sesuai
    '''
    global matrix
    f = open(f'./test/tc{tc}.txt')
    mat = []
    for i in range(4):
      mat += map(int, f.readline().strip().split())
    matrix = Matrix(np.array(mat))
    f.close()
    # Buka halaman baru yang menunjukkan kondisi matriks
    eel.go_to("matrix.html")

  @eel.expose
  def updateMatrixPreviewGrid():
    '''
      Memperbarui matrix pada matrix.html
    '''
    global matrix
    eel.updateGrid(matrix.arr.tolist())

  @eel.expose
  def showMatrixStats():
    '''
      Menunjukkan kurang.html
    '''
    eel.go_to("kurang.html")

  @eel.expose
  def updateKurang():
    '''
      Memperbarui kurang.html
    '''
    global matrix
    matrix.countAllKurang()
    eel.updateKurangLabels(matrix.kurangMap, matrix.getKurangPlusX())

  @eel.expose
  def solveMatrix():
    '''
      Mengecek apakah matrix solvable atau tidak
    '''
    global matrix
    if (not matrix.isGoalReachable()):
      eel.showErrorMessage()
      reinitialize()
    else:
      eel.go_to("solved.html")

  @eel.expose
  def solveGrid():
    '''
      Core programnya: Menyelesaikan grid yang diberikan oleh user.
      Hanya ditampilkan solusi pertama saja (tidak mencari semua solusi)
    '''
    global matrix
    global visitedMap
    global nodeCount
    global sol
    global matrices
    global currentStep
    # Menyelesaikan matriks
    pq = PriorityQueue()
    visitedMap = {}
    pq.put((matrix.c(), matrix))
    visitedMap[matrix.id()] = True
    nodeCount = 1
    sol = []
    matrices = []
    start = timeit.default_timer()
    # DFS dengan priority queue
    while not pq.empty():
      head = pq.get()[1]
      if head.isSolved():
        sol = head.stepsBefore
        break
      else:
        if head.canMoveUp():
          newMatrix = head.createMoveUp()
          s = newMatrix.id()
          if s not in visitedMap:
            visitedMap[s] = True
            pq.put((newMatrix.c(), newMatrix))
            nodeCount += 1
        if head.canMoveRight():
          newMatrix = head.createMoveRight()
          s = newMatrix.id()
          if s not in visitedMap:
            visitedMap[s] = True
            pq.put((newMatrix.c(), newMatrix))
            nodeCount += 1
        if head.canMoveDown():
          newMatrix = head.createMoveDown()
          s = newMatrix.id()
          if s not in visitedMap:
            visitedMap[s] = True
            pq.put((newMatrix.c(), newMatrix))
            nodeCount += 1
        if head.canMoveLeft():
          newMatrix = head.createMoveLeft()
          s = newMatrix.id()
          if s not in visitedMap:
            visitedMap[s] = True
            pq.put((newMatrix.c(), newMatrix))
            nodeCount += 1
    time = timeit.default_timer() - start
    # Bentuk solusi jawaban
    matrices.append(matrix)
    for i in range(len(sol)):
      if sol[i] == 'up':
        matrix = matrix.createMoveUp()
      elif sol[i] == 'down':
        matrix = matrix.createMoveDown()
      elif sol[i] == 'right':
        matrix = matrix.createMoveRight()
      elif sol[i] == 'left':
        matrix = matrix.createMoveLeft()
      matrices.append(matrix)
    currentStep = 0
    # Update GUI
    eel.setUpGrid(matrices[0].arr.tolist(), currentStep, len(matrices) - 1, time, nodeCount) 

  @eel.expose 
  def prevPage():
    '''
      Menunjukkan step sebelumnya pada solved.html
    '''
    global matrices
    global currentStep
    if (currentStep > 0):
      currentStep -= 1
      eel.updateGrid(matrices[currentStep].arr.tolist(), currentStep, len(matrices) - 1)
  
  @eel.expose
  def nextPage():
    '''
      Menunjukkan step berikutnya pada solved.html
    '''
    global matrices
    global currentStep
    if (currentStep < len(matrices) - 1):
      currentStep += 1
      eel.updateGrid(matrices[currentStep].arr.tolist(), currentStep, len(matrices) - 1)

  startSolver()