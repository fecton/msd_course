# MODULES
# =================================
from json import loads
# =================================

# VARIANT 5
# =================================
X = 200
Y = 100
X_percents = [60,70,80]
# =================================


class Program:
    def __init__(self):
        # Initialized graphs from file
        with open("graph.json") as f:
            self.graph = loads(f.read())
        self.point_c    = 0
        self.edge_c     = 0

        self.graph_amount = 0

    @staticmethod
    def Set_XY(self, x: int, y: int):
        # Метод задания XY-координат вершин графа
        global X,Y
        X = x
        Y = y

    def method_Kraskala(self):
        # Метод Краскала
        # Метод определения МОД алгоритмом Краскала (метод, возвращает список ребер МОД)
        raise NotImplementedError
    
    def method_Prima(self):
        # Метод Прима
        # Метод определения МОД алгоритмом Прима (метод возвращает список ребер МОД)
        raise NotImplementedError

    def matrix_of_lengths_graph():
        # Матриця дллин ребер полносвязного графа
        raise NotImplementedError

    def gen_graph(n, m):
        # Метод генерации случайного связного графа на n веришнах и m ребрах
        raise NotImplementedError

    def matrix_len_edges():
        # Матриця длин ребер сгенерированого графа
        raise NotImplementedError
    
    def matrix_contiguity_of_graph():
        # Матриця смежности графа (или/и) любая другая структура для представления графа
        raise NotImplementedError
    
    def queue_by_priority_of_len_gen_graphs():
        # Очередь по приоритетам длин ребер сгенерированного графа (простейший вариант) - возвращает из оставшихся ребер ребро минимальной длиньі
        raise NotImplementedError
    
    def info_about_graph():
        # Метод, вьіводящий информацию о графе - число вершин, число ребер, матрица длин ребер, матрица смежности, матрица списка ребер и т.д.
        raise NotImplementedError
    
    def check_contiguity():
        # Метод проверки связности графа
        raise NotImplementedError

    def is_cyclicity():
        # Метод проверки ацикличности графа
        raise NotImplementedError
    
    def define_secured_inserted_edge_for_Kraskala():
        # Метод определения безопасности вставляемого ребра для алгоритма Краскала
        raise NotImplementedError
    
    def define_secured_inserted_edge_for_Prima():
        # Метод определения безопасности вставляемого ребра для алгоритма Прима
        raise NotImplementedError
    
    def define_length_MOD_based_on_a_list_of_edges_of_MOD():
        # Метод определения длиньі МОД на основании списка ребер МОД
        raise NotImplementedError

    def info_about_MOD():
        # Метод, вьіводящий информацию о МОД - число вершин, список ребер МОД, список длин ребер МОД. длина МОД
        raise NotImplementedError


def menu():
    print("""Menu
0. Menu
1. Method Kraskala
2. Method Prima 
3. Exit
""")
    

m = Program()

exit()
op = 0
while True:
    match op:
        case 0:
            menu()
        case 1:
            m.method_Kraskala()
        case 2:
            m.method_Prima()
        case 3:
            exit()
        case _:
            print("[-] Invalid operations")
    op = int(input("[OP] >> "))





