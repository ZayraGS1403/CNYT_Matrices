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

if __name__ == '__main__':
    unittest.main()
