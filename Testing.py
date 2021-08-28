import unittest
from Sci_Fi import *

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
    def test_sub(self):
        self.assertEqual(sub(3,2),1)
    def test_mul(self):
        self.assertEqual(mul(3,2),6)
    def test_div(self):
        self.assertEqual(div(6,2),3)
    def test_squ(self):
        self.assertEqual(squ(3),9)
    def test_pow(self):
        self.assertEqual(power(2,3),8)
    def test_fac(self):
        self.assertEqual(fac(4),24)
    def test_sqrt(self):
        self.assertEqual(sqrt(9),3)
    def test_ceil(self):
        self.assertEqual(ceil(6.78),7)
    def test_floor(self):
        self.assertEqual(floor(6.78),6)
    def test_log10(self):
        self.assertEqual(log10(5),0.6989700043360189)
    def test_log2(self):
        self.assertEqual(log2(5),2.321928094887362)
    def test_exp(self):
        self.assertEqual(exp(5),148.4131591025766)
    def test_tenpow(self):
        self.assertEqual(tenpow(5),100000)
    def test_sin(self):
        self.assertEqual(sin(100),-0.5063656411097588)
    def test_cos(self):
        self.assertEqual(cos(100),0.8623188722876839)
    def test_tan(self):
        self.assertEqual(tan(100),-0.5872139151569291)
    def test_degree(self):
        self.assertEqual(degrees(15),859.4366926962348)
    def test_radian(self):
        self.assertEqual(radian(15),0.2617993877991494)
    def test_hypt(self):
        self.assertEqual(hypt(3,4),5)
    def test_mean(self):
        self.assertEqual(mean([1,2,3]),2)
    def test_median(self):
        self.assertEqual(median([1,2,3]),2)
    def test_mode(self):
        self.assertEqual(mode([1,2,3,3]),3)
    def test_var(self):
        self.assertEqual(var([1,2,3,4]),1.25)
    def test_stdev(self):
        self.assertEqual(stdev([1,2,3,4]),1.118033988749895)
    def test_discount(self):
        self.assertEqual(discount(100,10),90.0)
    def test_gst(self):
        self.assertEqual(gst(100,18),118)
    def test_si(self):
        self.assertEqual(si(100,10,1),10)
    def test_ci(self):
        self.assertEqual(ci(100,10,3),33.10000000000005)
    def test_permutation(self):
        self.assertEqual(permutation(7,5),2520.0)
    def test_combination(self):
        self.assertEqual(combination(8,2), 28.0)
    def test_quad(self):
        self.assertEqual(quad(1,4,2),[(-3.414213562373095+0j),(-3.414213562373095+0j)])
    def test_and(self):
        self.assertEqual(And(9,3),1)
    def test_or(self):
        self.assertEqual(Or(9,3),11)
    def test_not(self):
        self.assertEqual(Not(9),-10)
    def test_Xor(self):
        self.assertEqual(Xor(9,3),10)
    def test_peri_sq(self):
        self.assertEqual(peri_sq(4),16)
    def test_peri_rect(self):
        self.assertEqual(peri_rect(4,6),20)
    def test_peri_trian(self):
        self.assertEqual(peri_trian(2,3,4),9)
    def test_cir(self):
        self.assertEqual(circum(7),43.982297150257104)
    def test_area_sq(self):
        self.assertEqual(area_sq(4),16)
    def test_area_rect(self):
        self.assertEqual(area_rect(4,5),20)
    def test_area_cir(self):
        self.assertEqual(area_cir(5),78.53981633974483)
    def test_area_tri(self):
        self.assertEqual(area_tri(3,4,5),32.863353450309965)
    def test_cel(self):
        self.assertEqual(cel_to_fah(37),98.60000000000001)
    def test_fah(self):
        self.assertEqual(fah_to_cel(100),38.080000000000005)
    def test_bin(self):
        self.assertEqual(dec_to_bin(24),'0b11000')
    def test_oct(self):
        self.assertEqual(dec_to_oct(24),'0o30')
    def test_hex(self):
        self.assertEqual(dec_to_hex(24),'0x18')
    def test_expression(self):
        self.assertEqual(eval('2+3+7+9-4*2'),13)
        
            

if __name__=="__main__":
    unittest.main()

