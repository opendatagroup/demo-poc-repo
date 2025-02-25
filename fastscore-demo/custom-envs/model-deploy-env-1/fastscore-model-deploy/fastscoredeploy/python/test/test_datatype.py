import json
import unittest

from fastscoredeploy.codec.datatype import *

class TestDataType(unittest.TestCase):
    def test_promote_numbers(self):
        self.assertTrue(AvroInt().accepts(AvroInt()))

        self.assertTrue(AvroInt().accepts(AvroInt()))
        self.assertTrue(AvroLong().accepts(AvroInt()))
        self.assertTrue(AvroFloat().accepts(AvroInt()))
        self.assertTrue(AvroDouble().accepts(AvroInt()))

        self.assertTrue(AvroLong().accepts(AvroLong()))
        self.assertTrue(AvroFloat().accepts(AvroLong()))
        self.assertTrue(AvroDouble().accepts(AvroLong()))

        self.assertTrue(AvroFloat().accepts(AvroFloat()))
        self.assertTrue(AvroDouble().accepts(AvroFloat()))

        self.assertTrue(AvroDouble().accepts(AvroDouble()))

        self.assertFalse(AvroInt().accepts(AvroLong()))
        self.assertFalse(AvroInt().accepts(AvroFloat()))
        self.assertFalse(AvroInt().accepts(AvroDouble()))

        self.assertFalse(AvroLong().accepts(AvroFloat()))
        self.assertFalse(AvroLong().accepts(AvroDouble()))

        self.assertFalse(AvroFloat().accepts(AvroDouble()))

    def test_promote_numbers_type_variant_array(self):
        self.assertTrue(AvroArray(AvroInt()).accepts(AvroArray(AvroInt())))
        self.assertTrue(AvroArray(AvroLong()).accepts(AvroArray(AvroInt())))
        self.assertTrue(AvroArray(AvroFloat()).accepts(AvroArray(AvroInt())))
        self.assertTrue(AvroArray(AvroDouble()).accepts(AvroArray(AvroInt())))

        self.assertTrue(AvroArray(AvroLong()).accepts(AvroArray(AvroLong())))
        self.assertTrue(AvroArray(AvroFloat()).accepts(AvroArray(AvroLong())))
        self.assertTrue(AvroArray(AvroDouble()).accepts(AvroArray(AvroLong())))

        self.assertTrue(AvroArray(AvroFloat()).accepts(AvroArray(AvroFloat())))
        self.assertTrue(AvroArray(AvroDouble()).accepts(AvroArray(AvroFloat())))

        self.assertTrue(AvroArray(AvroDouble()).accepts(AvroArray(AvroDouble())))

        self.assertFalse(AvroArray(AvroInt()).accepts(AvroArray(AvroLong())))
        self.assertFalse(AvroArray(AvroInt()).accepts(AvroArray(AvroFloat())))
        self.assertFalse(AvroArray(AvroInt()).accepts(AvroArray(AvroDouble())))

        self.assertFalse(AvroArray(AvroLong()).accepts(AvroArray(AvroFloat())))
        self.assertFalse(AvroArray(AvroLong()).accepts(AvroArray(AvroDouble())))

        self.assertFalse(AvroArray(AvroFloat()).accepts(AvroArray(AvroDouble())))

    def test_promote_numbers_type_variant_map(self):
        self.assertTrue(AvroMap(AvroInt()).accepts(AvroMap(AvroInt())))
        self.assertTrue(AvroMap(AvroLong()).accepts(AvroMap(AvroInt())))
        self.assertTrue(AvroMap(AvroFloat()).accepts(AvroMap(AvroInt())))
        self.assertTrue(AvroMap(AvroDouble()).accepts(AvroMap(AvroInt())))

        self.assertTrue(AvroMap(AvroLong()).accepts(AvroMap(AvroLong())))
        self.assertTrue(AvroMap(AvroFloat()).accepts(AvroMap(AvroLong())))
        self.assertTrue(AvroMap(AvroDouble()).accepts(AvroMap(AvroLong())))

        self.assertTrue(AvroMap(AvroFloat()).accepts(AvroMap(AvroFloat())))
        self.assertTrue(AvroMap(AvroDouble()).accepts(AvroMap(AvroFloat())))

        self.assertTrue(AvroMap(AvroDouble()).accepts(AvroMap(AvroDouble())))

        self.assertFalse(AvroMap(AvroInt()).accepts(AvroMap(AvroLong())))
        self.assertFalse(AvroMap(AvroInt()).accepts(AvroMap(AvroFloat())))
        self.assertFalse(AvroMap(AvroInt()).accepts(AvroMap(AvroDouble())))

        self.assertFalse(AvroMap(AvroLong()).accepts(AvroMap(AvroFloat())))
        self.assertFalse(AvroMap(AvroLong()).accepts(AvroMap(AvroDouble())))

        self.assertFalse(AvroMap(AvroFloat()).accepts(AvroMap(AvroDouble())))

    def test_promote_numbers_in_record(self):
        self.assertTrue(AvroRecord([AvroField("one", AvroInt())], name="One").accepts(AvroRecord([AvroField("one", AvroInt())], name="One")))
        self.assertTrue(AvroRecord([AvroField("one", AvroLong())], name="One").accepts(AvroRecord([AvroField("one", AvroInt())], name="One")))
        self.assertTrue(AvroRecord([AvroField("one", AvroFloat())], name="One").accepts(AvroRecord([AvroField("one", AvroInt())], name="One")))
        self.assertTrue(AvroRecord([AvroField("one", AvroDouble())], name="One").accepts(AvroRecord([AvroField("one", AvroInt())], name="One")))

        self.assertTrue(AvroRecord([AvroField("one", AvroLong())], name="One").accepts(AvroRecord([AvroField("one", AvroLong())], name="One")))
        self.assertTrue(AvroRecord([AvroField("one", AvroFloat())], name="One").accepts(AvroRecord([AvroField("one", AvroLong())], name="One")))
        self.assertTrue(AvroRecord([AvroField("one", AvroDouble())], name="One").accepts(AvroRecord([AvroField("one", AvroLong())], name="One")))

        self.assertTrue(AvroRecord([AvroField("one", AvroFloat())], name="One").accepts(AvroRecord([AvroField("one", AvroFloat())], name="One")))
        self.assertTrue(AvroRecord([AvroField("one", AvroDouble())], name="One").accepts(AvroRecord([AvroField("one", AvroFloat())], name="One")))

        self.assertTrue(AvroRecord([AvroField("one", AvroDouble())], name="One").accepts(AvroRecord([AvroField("one", AvroDouble())], name="One")))

        self.assertFalse(AvroRecord([AvroField("one", AvroInt())], name="One").accepts(AvroRecord([AvroField("one", AvroLong())], name="One")))
        self.assertFalse(AvroRecord([AvroField("one", AvroInt())], name="One").accepts(AvroRecord([AvroField("one", AvroFloat())], name="One")))
        self.assertFalse(AvroRecord([AvroField("one", AvroInt())], name="One").accepts(AvroRecord([AvroField("one", AvroDouble())], name="One")))

        self.assertFalse(AvroRecord([AvroField("one", AvroLong())], name="One").accepts(AvroRecord([AvroField("one", AvroFloat())], name="One")))
        self.assertFalse(AvroRecord([AvroField("one", AvroLong())], name="One").accepts(AvroRecord([AvroField("one", AvroDouble())], name="One")))

        self.assertFalse(AvroRecord([AvroField("one", AvroFloat())], name="One").accepts(AvroRecord([AvroField("one", AvroDouble())], name="One")))

    def test_have_type_safe_null(self):
        self.assertFalse(AvroNull().accepts(AvroString()))
        self.assertFalse(AvroString().accepts(AvroNull()))

    def test_distinguish_boolean_from_numbers(self):
        self.assertFalse(AvroBoolean().accepts(AvroInt()))
        self.assertFalse(AvroBoolean().accepts(AvroLong()))
        self.assertFalse(AvroBoolean().accepts(AvroFloat()))
        self.assertFalse(AvroBoolean().accepts(AvroDouble()))

        self.assertFalse(AvroInt().accepts(AvroBoolean()))
        self.assertFalse(AvroLong().accepts(AvroBoolean()))
        self.assertFalse(AvroFloat().accepts(AvroBoolean()))
        self.assertFalse(AvroDouble().accepts(AvroBoolean()))

    def test_distinguish_bytes_string_enum_fixed(self):
        self.assertTrue(AvroBytes().accepts(AvroBytes()))
        self.assertFalse(AvroBytes().accepts(AvroString()))
        self.assertFalse(AvroBytes().accepts(AvroEnum(["one", "two", "three"], name="One")))
        self.assertFalse(AvroBytes().accepts(AvroFixed(5, name="One")))

        self.assertFalse(AvroString().accepts(AvroBytes()))
        self.assertTrue(AvroString().accepts(AvroString()))
        self.assertFalse(AvroString().accepts(AvroEnum(["one", "two", "three"], name="One")))
        self.assertFalse(AvroString().accepts(AvroFixed(5, name="One")))

        self.assertFalse(AvroEnum(["one", "two", "three"], name="One").accepts(AvroBytes()))
        self.assertFalse(AvroEnum(["one", "two", "three"], name="One").accepts(AvroString()))
        self.assertTrue(AvroEnum(["one", "two", "three"], name="One").accepts(AvroEnum(["one", "two", "three"], name="One")))
        self.assertFalse(AvroEnum(["one", "two", "three"], name="One").accepts(AvroFixed(5, name="One")))

        self.assertFalse(AvroFixed(5, name="One").accepts(AvroBytes()))
        self.assertFalse(AvroFixed(5, name="One").accepts(AvroString()))
        self.assertFalse(AvroFixed(5, name="One").accepts(AvroEnum(["one", "two", "three"], name="One")))
        self.assertTrue(AvroFixed(5, name="One").accepts(AvroFixed(5, name="One")))

    def test_resolve_unions(self):
        self.assertTrue(AvroUnion([AvroInt(), AvroString()]).accepts(AvroInt()))
        self.assertTrue(AvroUnion([AvroInt(), AvroString()]).accepts(AvroString()))
        self.assertFalse(AvroUnion([AvroInt(), AvroString()]).accepts(AvroDouble()))

        self.assertTrue(AvroUnion([AvroInt(), AvroString(), AvroNull()]).accepts(AvroUnion([AvroInt(), AvroString()])))
        self.assertTrue(AvroUnion([AvroInt(), AvroString(), AvroNull()]).accepts(AvroUnion([AvroInt(), AvroNull()])))

    def doParserTest(self, input, expected):
        found = ForwardDeclarationParser().parse([input])[input]
        self.assertTrue(found.accepts(expected) and expected.accepts(found))

    def test_read_simple_types(self):
        self.doParserTest('''"null"''', AvroNull())
        self.doParserTest('''"boolean"''', AvroBoolean())
        self.doParserTest('''"int"''', AvroInt())
        self.doParserTest('''"long"''', AvroLong())
        self.doParserTest('''"float"''', AvroFloat())
        self.doParserTest('''"double"''', AvroDouble())
        self.doParserTest('''"bytes"''', AvroBytes())
        self.doParserTest('''{"type": "fixed", "name": "Test", "size": 5}''', AvroFixed(5, name="Test"))
        self.doParserTest('''"string"''', AvroString())
        self.doParserTest('''{"type": "enum", "name": "Test", "symbols": ["one", "two", "three"]}''', AvroEnum(["one", "two", "three"], name="Test"))
        self.doParserTest('''{"type": "array", "items": "int"}''', AvroArray(AvroInt()))
        self.doParserTest('''{"type": "map", "values": "int"}''', AvroMap(AvroInt()))
        self.doParserTest('''{"type": "record", "name": "Test", "fields": [{"name": "one", "type": "int"}]}''', AvroRecord([AvroField("one", AvroInt())], name="Test"))
        self.doParserTest('''["string", "null"]''', AvroUnion([AvroString(), AvroNull()]))

    def test_identify_nested_record_definitions(self):
        self.maxDiff = None

        self.doParserTest(
          '''{"type": "record", "name": "Outer", "fields": [{"name": "child", "type": {"type": "record", "name": "Inner", "fields": [{"name": "child", "type": "int"}]}}]}''',
          AvroRecord([AvroField("child", AvroRecord([AvroField("child", AvroInt())], name="Inner"))], name="Outer"))

    def test_resolve_dependent_records_in_any_order(self):
        record1 = '''{"type": "record", "name": "Outer", "fields": [{"name": "child", "type": "Inner"}]}'''
        record2 = '''{"type": "record", "name": "Inner", "fields": [{"name": "child", "type": "int"}]}'''

        expected1 = AvroRecord([AvroField("child", AvroRecord([AvroField("child", AvroInt())], name="Inner"))], name="Outer")
        expected2 = AvroRecord([AvroField("child", AvroInt())], name="Inner")

        found = ForwardDeclarationParser().parse([record1, record2])
        self.assertTrue(found[record1].accepts(expected1) and expected1.accepts(found[record1]))
        self.assertTrue(found[record2].accepts(expected2) and expected2.accepts(found[record2]))

        found = ForwardDeclarationParser().parse([record2, record1])
        self.assertTrue(found[record1].accepts(expected1) and expected1.accepts(found[record1]))
        self.assertTrue(found[record2].accepts(expected2) and expected2.accepts(found[record2]))

    def test_resolve_dependent_records_with_namespaces(self):
        record1 = '''{"type": "record", "name": "Outer", "namespace": "com.wowie", "fields": [{"name": "child", "type": "Inner"}]}'''
        record2 = '''{"type": "record", "name": "Inner", "namespace": "com.wowie", "fields": [{"name": "child", "type": "int"}]}'''

        expected1 = AvroRecord([AvroField("child", AvroRecord([AvroField("child", AvroInt())], name="Inner", namespace="com.wowie"))], name="Outer", namespace="com.wowie")
        expected2 = AvroRecord([AvroField("child", AvroInt())], name="Inner", namespace="com.wowie")

        found = ForwardDeclarationParser().parse([record1, record2])
        self.assertTrue(found[record1].accepts(expected1) and expected1.accepts(found[record1]))
        self.assertTrue(found[record2].accepts(expected2) and expected2.accepts(found[record2]))

        found = ForwardDeclarationParser().parse([record2, record1])
        self.assertTrue(found[record1].accepts(expected1) and expected1.accepts(found[record1]))
        self.assertTrue(found[record2].accepts(expected2) and expected2.accepts(found[record2]))

    def test_resolve_recursively_defined_records(self):
        record1 = '''{"type": "record", "name": "Recursive", "fields": [{"name": "child", "type": ["null", "Recursive"]}]}'''
        result = ForwardDeclarationParser().parse([record1])[record1]

        x = result.field("child").avroType
        y = AvroUnion([AvroNull(), result])
        self.assertTrue(x.accepts(y) and y.accepts(x))

    def test_re_callable_and_accumulate_types(self):
        forwardDeclarationParser = ForwardDeclarationParser()

        record1 = '''{"type": "record", "name": "Outer", "fields": [{"name": "child", "type": "Inner"}]}'''
        record2 = '''{"type": "record", "name": "Inner", "fields": [{"name": "child", "type": "int"}]}'''
        record3 = '''{"type": "record", "name": "Another", "fields": [{"name": "innerChild", "type": "Inner"}]}'''

        type1 = AvroRecord([AvroField("child", AvroRecord([AvroField("child", AvroInt())], name="Inner"))], name="Outer")
        type2 = AvroRecord([AvroField("child", AvroInt())], name="Inner")
        type3 = AvroRecord([AvroField("innerChild", AvroRecord([AvroField("child", AvroInt())], name="Inner"))], name="Another")

        result1 = forwardDeclarationParser.parse([record1, record2])
        self.assertTrue(result1[record1].accepts(type1) and type1.accepts(result1[record1]))
        self.assertTrue(result1[record2].accepts(type2) and type2.accepts(result1[record2]))

        result2 = forwardDeclarationParser.parse([record3])
        self.assertTrue(result2[record3].accepts(type3) and type3.accepts(result2[record3]))

        def equivalent(x, y):
            return x.accepts(y) and y.accepts(x)

        self.assertTrue(equivalent(forwardDeclarationParser.getAvroType("Outer"), type1))
        self.assertTrue(equivalent(forwardDeclarationParser.getAvroType("Inner"), type2))
        self.assertTrue(equivalent(forwardDeclarationParser.getAvroType("Another"), type3))
        # forwardDeclarationParser.getAvroType('''"Outer"''') should be (Some(type1))
        # forwardDeclarationParser.getAvroType('''{"type": "Outer"}''') should be (Some(type1))
        # forwardDeclarationParser.getAvroType('''{"type": "array", "items": "Outer"}''') should be (Some(AvroArray(type1)))
        # forwardDeclarationParser.getAvroType('''{"type": "array", "items": "int"}''') should be (Some(AvroArray(AvroInt())))

    # --- Decoder tests --------------------------------------------------------
    def test_json_decoder(self):
        int_sch = jsonToAvroType('''{"type":"int"}''')
        self.assertEqual(jsonDecoder(int_sch, '3'), 3)
        self.assertEqual(jsonDecoder(int_sch, '-3'), -3)
        int_sch2 = jsonToAvroType('''"int"''')
        self.assertEqual(jsonDecoder(int_sch2, '5'), 5)
        self.assertEqual(jsonDecoder(int_sch2, '-5'), -5)
        double_sch = jsonToAvroType('''{"type":"double"}''')
        self.assertEqual(jsonDecoder(double_sch, '5.5'), 5.5)
        self.assertEqual(jsonDecoder(double_sch, '-5.5'), -5.5)

if __name__ == "__main__":
    unittest.main()
