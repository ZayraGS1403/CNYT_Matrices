import Lib2matrces as mat
import unittest

class TestMatrizOperations(unittest.TestCase):

    def test_sumavec(self):
        self.assertEqual(mat.sumavec([2j, 4, 6-7j,5],[8j, 4-10j, 4+2j, 55j]),([10j, 8-10j, 10-5j, 5+55j]))
    def test_sumavec(self):
        self.assertEqual(mat.sumavec([-4,8.3],[0.6,6]),([-3.4,14.3]))

    def test_inverso(self):
        self.assertEqual(mat.inverso([4j, -2+15j]),([-4j,2-15j]))
    def test_inverso(self):
        self.assertEqual(mat.inverso([12,-2.1]),([-12,2.1]))

    def test_multliescalar(self):
        self.assertEqual(mat.multliescalar(2,[12, -2.1]), ([24, -4.2]))
    def test_multliescalar(self):
        self.assertEqual(mat.multliescalar(2j, [31j, 0, 1+8j]), ([(-62+0j), 0j, (-16+2j)]))

    def test_sumatriz(self):
        self.assertEqual(mat.sumatriz([[-4,8.3],[12,0]],[[0.6,6],[1,2]]),([[-3.4,14.3],[13,2]]))
    def test_sumatriz(self):
        self.assertEqual(mat.sumatriz([[2,7.9],[21,1]],[[3.6,9]]),("Tamaños de matrices diferentes"))

    def test_inversamatriz(self):
        self.assertEqual(mat.inversamatriz([[1,21],[2,0]]),([[-1,-21],[-2,0]]))
    def test_inversamatriz(self):
        self.assertEqual(mat.inversamatriz([[-13+8j, 39+14j, 9j], [-15-4j, 7+7j, -1+5j]]),([[13-8j, -39-14j, -9j], [15+4j, -7-7j, 1-5j]]))

    def test_multi_escalar_matriz(self):
        self.assertEqual(mat.multi_escalar_matriz(2,[[9,-1],[0,11.3]]),([[18,-2],[0,22.6]]))
    def test_multi_escalar_matriz(self):
        self.assertEqual(mat.multi_escalar_matriz(64 - 7j,[[2,7.9],[21,1]]),([[(128-14j), (505.6-55.300000000000004j)], [(1344-147j), (64-7j)]]))

    def test_transpuesta(self):
        self.assertEqual(mat.transpuesta([[6+2j, 4-1j], [-2j, 6-14j], [7-8j, 3j]],[[6+2j, -2j, 7-8j], [4-1j, 6-14j, 3j]]))
    def test_transpuesta(self):
        self.assertEqual(mat.transpuesta([[-4, 8.3,7], [12, 0,1],[-8,7,0]]), ([[-4, 12, -8], [8.3, 0, 7], [7, 1, 0]]))

    def test_conjugada(self):
        self.assertEqual(mat.conjugada([[-4,8.3],[12,0]]),([[-4, 8.3], [12, 0]]))

    def test_adjunta(self):
        self.assertEqual(mat.adjunta([[-4,8.3],[12,0]]),([[-4, 12], [8.3, 0]]))
    def test_adjunta(self):
        self.assertEqual(mat.adjunta([[9+1j, 16-9j], [-1j, 7+7j]]),([[(9-1j), (-0+1j)], [(16+9j), (7-7j)]]))

    def test_prod_interno(self):
        v1 = [-9 + 3j, 50+6j, 8, 3j]
        v2= [3j, 17 - 9j, 8j, 1j]
        esperada = 808-515j
        actual  = mat.prod_interno(v1, v2)
        self.assertEqual(actual, esperada)

    def test_prod_de_matriz(self):
        m1 = [[9,-1],[0,11.3]]
        m2 = [[-3.4,14.3],[13,2]]
        esperada = [[-43.599999999999994, 22.6], [-43.599999999999994, 22.6]]
        actual = mat.prod_de_matz(m1, m2)
        self.assertEqual(actual, esperada)

    def test_vectornormal(self):
        v1 = [-9 + 3j, 50+6j, 8, 3j]
        esperada = 51.95
        actual = mat.vectornormal(v1)
        self.assertEqual(actual, esperada)

    def test_unitaria(self):
        m1 = [[2 / 3, (-2 + 1j) / 3], [(2 + 1j) / 3, 2 / 3]]
        esperada = "La matriz es unitaria"
        actual = mat.unitario(m1)
        self.assertEqual(actual, esperada)

    def test_distancia(self):
        v1 = [8j, 4-10j, 4+2j, 55j]
        v2 = [2j, 4, 6-7j,5]
        esperada = 57.19
        actual = mat.distancia(v1,v2)
        self.assertEqual(actual, esperada)

    def test_tensor(self):
        m1 = [[2, 3], [1, 4]]
        m2 = [[5, 3, 2], [1, 0, 2], [-2, 5, 6]]
        esperada = [[10, 6, 4, 15, 9, 6], [2, 0, 4, 3, 0, 6], [-4, 10, 12, -6, 15, 18], [5, 3, 2, 20, 12, 8],
                    [1, 0, 2, 4, 0, 8], [-2, 5, 6, -8, 20, 24]]
        actual = mat.tensor(m1, m2)
        self.assertEqual(actual, esperada)

    def test_vectores_prop(self):
        m1 =[[-4,8.3],[12,0]]
        esperada = "valores: [-12.18   8.18]. vectores: [-0.71230502  0.70187005]"
        actual = mat. vectores_prop(m1)
        self.assertEqual(actual, esperada)

    def test_hermitiana(self):
        m1 = [[3, 2 - 1j, -5j], [2 + 1j, 0, 9 - 5j], [5j, 9 + 5j, 6]]
        esperada = "La matriz es hermitiana"
        actual = mat.hermitiana(m1)
        self.assertEqual(actual, esperada)

if __name__ == '__main__':
    unittest.main()
