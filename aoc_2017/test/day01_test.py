import aoc_2017.day01 as day01
import unittest

MY_INPUT_RAW = """
8239366453455812726956773185134594918346411298443937426725535444391263143998467732348455355933553489
3149949618483958211881768917194863586442785221532542143371745897577136952213876624822596324216865897
5326354785415252974294317138511141826226866364555761117178764543435899886711426319675443679829181257
4969662194358316215655196679898987258366396266816458217148614431418934276723847167327658848447724333
7479818595574131111636589965983363423793887818136731721863553966735736429575474482959584296277352458
4225427969467467611641591834876769829719248136613147351298534885563144114336211961674392912181735773
8516342982274541578852417691568117876118973499653314742172234611768966432429753972278596965544929969
3723542327254934834952855943221452155165697113685997223285412626234938125442459734887444773654572226
1957871275935756764184378994167427983811716675476257858556464755677478725146588747147857375293675711
5757471324717279337735125713684673861519665685989646313314288697621518536343623569357512981218492814
4212879651766348239122617425639551516636151444262494418125595212452481526886413196915143388872121359
5267927325759562132732586252438456569556992685896517565257787464673718221817783929691626876446423134
3317493273223675714325328572352143642214717694816671181177293264295563575724213337985171689978631519
2728141823849179197539935739349475191315521986239995964699342892187879811921567554884784547799483674
4929918954159722827194721564121532315459611433157384994543332773796862165243183378464731546787498174
8447817811395719842722358728668862758799449213299597363152967339813136439565769568517621492755219491
7799198823652947537359521766511243472774423578985285276567518934275369537721937479154855478667147373
3124951946779531847479755363363288448281622183736545494372344785112312749694167483996738384351293899
1491368577285459774427634897996934923195497733286269188747183876978782357441544916779223175189526874
3965596247773455923275562494364496622797361778818221362189957939132439938614642342726287443799257957
3858589183571854577861459758534348533553925167947139351819511798829977371215856637215221838924612644
785498936263849489519896548811254628976642391428413984281758771868781714266261781359762798
"""
MY_INPUT = MY_INPUT_RAW.replace("\n", "")

class Day01Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(day01.day1_1("1122"), 3)
        self.assertEqual(day01.day1_1("1111"), 4)
        self.assertEqual(day01.day1_1("1234"), 0)
        self.assertEqual(day01.day1_1("91212129"), 9)
        self.assertEqual(day01.day1_1(MY_INPUT), 1144)
    def test2(self):
        self.assertEqual(day01.day1_2("1212"), 6)
        self.assertEqual(day01.day1_2("1221"), 0)
        self.assertEqual(day01.day1_2("123425"), 4)
        self.assertEqual(day01.day1_2("123123"), 12)
        self.assertEqual(day01.day1_2("12131415"), 4)
        self.assertEqual(day01.day1_2(MY_INPUT), 1194)

if __name__ == '__main__':
    unittest.main()
