# -*- coding: utf-8 -*-
"""
Simple chemical formula extension for Markdown. 

It formats chemical equations, written in simple text form, automatically detecting when the number is subscript or not. It also supports superscripts, though with less readable syntax. Equation must be enclosed in {}.

Subscripts:
  Detected automatically. In {3H2O}, only '2' is turned to subsscript.

Superscripts:
 ^(text) or ^char
 
Additionally, following special characters are available:
 *    middle dot "·"
 ->   right arrow "→"
 <->  pair of arrows "⇄"
 <>   equilibrium arrow "⇌" 
 hnu  hν

Examples:
>>> import markdown
>>> md = markdown.Markdown(extensions=['simplechem'])
>>> md.convert('This is sugar: {C6H12O6}')
'<p>This is sugar: <span class="simplechem">C<sub>6</sub>H<sub>12</sub>O<sub>6</sub></span></p>'

>>> md.convert('Smart subscript and special chars: {2KOH + H2SO4 -> K2SO4 + H2O}')
'<p>Smart subscript and special chars: <span class="simplechem">2KOH + H<sub>2</sub>SO<sub>4</sub> → K<sub>2</sub>SO<sub>4</sub> + H<sub>2</sub>O</span></p>'

>>> md.convert('Superscript: {2K^+ + O^(2-)}')
'<p>Superscript: <span class="simplechem">2K<sup>+</sup> + O<sup>2-</sup></span></p>'

>>> md.convert('All special chars: {* -> <-> <> hnu}')
'<p>All special chars: <span class="simplechem">· → ⇄ ⇌ hν</span></p>'

>>> md.convert('Fractions: {1/2H2 + 0.5Cl2}')
'<p>Fractions: <span class="simplechem">1/2H<sub>2</sub> + 0.5Cl<sub>2</sub></span></p>'
"""
from markdown.extensions import Extension
from  markdown.inlinepatterns import Pattern
import re
import xml.etree.ElementTree as etree

class SimpleChem(Pattern):
    def __init__(self, *args, **kwargs):
        super(SimpleChem, self).__init__( "\\{([^}]*)\\}", *args, **kwargs)
        self.spanClass = kwargs.get("spanClass", "simplechem")
    def handleMatch(self, m):
        tag = parseFormula(m.group(2))
        if self.spanClass is not None:
            tag.attrib['class'] = self.spanClass
        return tag
    
class SimpleChemExtension(Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(SimpleChem(), 'simplechem', 175)
        
def makeExtension(**kwargs): return SimpleChemExtension(**kwargs)

TOK_NAME = 1
TOK_NUM = 2
TOK_SUPER = 3
TOK_BRACE = 4
TOK_CHAR = 5

#Tokenizer rules: (token regexp,  group number, token type)
formulaTokens = \
[ (r"[0-9\.][0-9\./]*",    0, TOK_NUM),
  (r"\?",                  0, TOK_NUM), #single question mark is a numer
  (r"[a-zA-Z]+",   0, TOK_NAME),
  (r"\^\((.+?)\)", 1, TOK_SUPER),
  (r"\^(\S)",      1, TOK_SUPER), #superscript with single character
  (r"[\[\]\(\)]",  0, TOK_BRACE),
  (r"->",  0, TOK_CHAR),
  (r"<->", 0, TOK_CHAR),
  (r"<>",  0, TOK_CHAR),
  (r".",   0, TOK_CHAR) ] #allow any character

#Key must be a whole token
specialCharacters = \
{ '->' :"→",
  '*'  :"·",
  '<>' :"⇌",
  'hnu':"hν",  #parsed as TOK_NAME
  '<->':"⇄" }

compiledFormulaTokens = [ (re.compile(t),g, n) for t,g,n in formulaTokens ]

def getToken( text, pos, compiledFormulaTokens ):
    for tokRe, groupNumber, tokenClass in compiledFormulaTokens:
        match = tokRe.match(text, pos)
        if match:
            return match.group(groupNumber), tokenClass, match.end()
    raise ValueError("No matching token, string starts as:"+text[pos:pos+20])

def tokenize( text, compiledFormulaTokens):
    pos = 0
    endPos = len(text)
    while pos != endPos:
        formulaPart, tokenClass, pos = getToken( text, pos, compiledFormulaTokens )
        yield formulaPart, tokenClass
        
def parseFormula( text ):
    """Parse chemical equation and return elementtree for its HTML representation"""
    root = etree.Element('span')

    def appendPlain( text ):
        if len(root) == 0:
            root.text = text
        else:
            root[-1].tail = text
            
    #buffer to accumulate text fragments
    textBuffer = []
    def flushTextBuffer():
        if textBuffer:
            appendPlain("".join(textBuffer))
            del textBuffer[:]

    def appendText(text, tag=None):
        if tag is None:
            textBuffer.append(text)
        else:
            flushTextBuffer()
            elem = etree.Element(tag)
            elem.text = text
            root.append(elem)
    #Core procedure.
    prevTokenClass = -1
    for tokenText, tokenClass in tokenize( text, compiledFormulaTokens ):
        tokenText = specialCharacters.get(tokenText, tokenText)
        #possible token types: num, name, brace, super, char
        tag = None
        if tokenClass == TOK_NUM:
            #For numbers, apply smart rules when to make it subscript
            if prevTokenClass in (TOK_NAME, TOK_BRACE, TOK_SUPER):
                tag = 'sub'
        elif tokenClass == TOK_SUPER:
            tag = 'sup'
        appendText(tokenText, tag)
        prevTokenClass = tokenClass
    #write last fragment, if present
    flushTextBuffer()
    return root

if __name__=="__main__":
    import doctest
    doctest.testmod()
