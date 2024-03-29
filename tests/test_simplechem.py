# -*- coding: utf-8 -*-
"""
====================================
Markdown Simple Chemistry Extension Tests
====================================
:copyright: Copyright 2016 Dmitry Shintyakov
:license: MIT, see LICENSE for details.
"""
import unittest
from markdown import markdown


class SimplechemTest(unittest.TestCase):
    def test_custom_prefix(self):
        text = 'Without prefix: {C2H5OH} and with: chem{C2H5OH}'
        expected= '<p>Without prefix: {C2H5OH} and with: <span class="simplechem">C<sub>2</sub>H<sub>5</sub>OH</span></p>'
        result = markdown(text,
                          extensions=['mdx_simplechem'],
                          extension_configs={'mdx_simplechem': {'prefix': 'chem'}})
        self.assertEqual(expected, result)

    def test_simple(self):
        text = 'This is sugar: {C6H12O6}'
        expected= '<p>This is sugar: <span class="simplechem">C<sub>6</sub>H<sub>12</sub>O<sub>6</sub></span></p>'
        result = markdown(text, extensions=['mdx_simplechem'])
        self.assertEqual(expected, result)
    def test_config_class(self):
        text = 'This is sugar: {C6H12O6}'
        expected= '<p>This is sugar: <span class="custom">C<sub>6</sub>H<sub>12</sub>O<sub>6</sub></span></p>'
        result = markdown(text, extensions=['mdx_simplechem'],
                          extension_configs={'mdx_simplechem': {'class': 'custom'}})
        self.assertEqual(expected, result)
    def test_smart_subscript_and_special(self):
        text = 'Smart subscript and special chars: {2KOH + H2SO4 -> K2SO4 + H2O}'
        expected= '<p>Smart subscript and special chars: <span class="simplechem">2KOH + H<sub>2</sub>SO<sub>4</sub> → K<sub>2</sub>SO<sub>4</sub> + H<sub>2</sub>O</span></p>'
        result = markdown(text, extensions=['mdx_simplechem'])
        self.assertEqual(expected, result)
    def test_super(self):
        text = 'Superscript: {2K^+ + O^(2-)}'
        expected= '<p>Superscript: <span class="simplechem">2K<sup>+</sup> + O<sup>2-</sup></span></p>'
        result = markdown(text, extensions=['mdx_simplechem'])
        self.assertEqual(expected, result)
    def test_all_special(self):
        text = 'All special chars: {* -> <-> <> hnu}'
        expected= '<p>All special chars: <span class="simplechem">· → ⇄ ⇌ hν</span></p>'
        result = markdown(text, extensions=['mdx_simplechem'])
        self.assertEqual(expected, result)
    def test_fractoins(self):
        text = 'Fractions: {1/2H2 + 0.5Cl2}'
        expected= '<p>Fractions: <span class="simplechem">1/2H<sub>2</sub> + 0.5Cl<sub>2</sub></span></p>'
        result = markdown(text, extensions=['mdx_simplechem'])
        self.assertEqual(expected, result)
    def test_questionmark(self):
        """Single question mark should be treated as a numer too"""
        text = "Question: {?H2O + ?H?O4}"
        expected = '<p>Question: <span class="simplechem">?H<sub>2</sub>O + ?H<sub>?</sub>O<sub>4</sub></span></p>'
        result = markdown(text, extensions=['mdx_simplechem'])
        self.assertEqual(expected, result)
        
        
    
