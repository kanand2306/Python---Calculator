from tabulate import tabulate

def consts():
    d=[["speed of light in vacuum","299792458 m⋅s−1"],
       ["Planck constant","6.62607015×10−34 J⋅Hz−1"],
       ["reduced Planck constant","1.054571817...×10−34 J⋅s"],
       ["Newtonian constant of gravitation","6.67430(15)×10−11 m3⋅kg−1⋅s−2"],
       ["vacuum electric permittivity","8.8541878128(13)×10−12 F⋅m−1"],
       ["vacuum magnetic permeability","1.25663706212(19)×10−6 N⋅A−2"],
       ["characteristic impedance of vacuum","376.730313668(57) Ω"],
       ["elementary charge","1.602176634×10−19 C"],
       ["hyperfine transition frequency of 133Cs","9192631770 Hz"],
       ["Avogadro constant","6.02214076×1023 mol−1"],
       ["Boltzmann constant","1.380649×10−23 J⋅K−1"],
       ["conductance quantum","7.748091729...×10−5 S"],
       ["Josephson constant","483597.8484...×109 Hz⋅V−1"],
       ["Coulomb constant","8.9875517923(14)×109 kg⋅m3⋅s−2⋅C−2"],
       ["von Klitzing constant","25812.80745... Ω"],
       ["magnetic flux quantum","2.067833848...×10−15 Wb"],
       ["inverse conductance quantum","12906.40372... Ω"],
       ["Bohr magneton","9.2740100783(28)×10−24 J⋅T−1"],
       ["nuclear magneton","5.0507837461(15)×10−27 J⋅T−1"],
       ["fine-structure constant","7.2973525693(11)×10−3"],
       ["inverse fine-structure constant","137.035999084(21)"],
       ["electron mass","9.1093837015(28)×10−31 kg"],
       ["proton mass","1.67262192369(51)×10−27 kg"],
       ["neutron mass","1.67492749804(95)×10−27 kg"],
       ["Bohr radius","5.29177210903(80)×10−11 m"],
       ["classical electron radius","2.8179403262(13)×10−15 m"],
       ["electron g-factor","−2.00231930436256(35)"],
       ["Fermi coupling constant","1.1663787(6)×10−5 GeV−2"],
       ["Hartree energy","4.3597447222071(85)×10−18 J"],
       ["quantum of circulation","3.6369475516(11)×10−4 m2⋅s−1"],
       ["Rydberg constant","10973731.568160(21) m−1"],
       ["Thomson cross section","6.6524587321(60)×10−29 m2"],
       ["W-to-Z mass ratio","0.88153(17)"],
       ["weak mixing angle","0.22290(30)"],
       ["atomic mass constant","1.66053906660(50)×10−27 kg"],
       ["Faraday constant","96485.33212... C⋅mol−1"],
       ["molar gas constant","8.314462618... J⋅mol−1⋅K−1"],
       ["molar mass constant","0.99999999965(30)×10−3 kg⋅mol−1"],
       ["Stefan–Boltzmann constant","5.670374419...×10−8 W⋅m−2⋅K−4"],
       ["first radiation constant","3.741771852...×10−16 W⋅m2"],
       ["first radiation constant for spectral radiance","1.191042972...×10−16 W⋅m2⋅sr−1"],
       ["molar mass of carbon-12","11.9999999958(36)×10−3 kg⋅mol−1"],
       ["molar Planck constant","3.990312712...×10−10 J⋅Hz−1⋅mol−1"],
       ["second radiation constant","1.438776877...×10−2 m⋅K"],
       ["Wien wavelength displacement law constant","2.897771955...×10−3 m⋅K"],
       ["Wien frequency displacement law constant","5.878925757...×1010 Hz⋅K−1"],
       ["Wien entropy displacement law constant","3.002916077...×10−3 m⋅K"]]
    print(tabulate(d,headers=["Quantity","Value"]))





    
   
   
