MarkdownSimplechem
==================
Simple chemical formula extension for Markdown.

Formats chemical equations, written in simple text form, automatically detecting when the number is subscript or not. It also supports superscripts, though with less readable syntax.

Syntax
------
Equation must be enclosed in {}.

### Subscripts:
Detected automatically. In {3H2O}, only '2' is turned to subscript.

Only number-like strings are rendered to subsripts. NUmber-like strings are:

* Strings, composed of numbers 0-9 and decimal point.
* Single question mark

### Superscripts
^(text) or ^char

### Special characters
Additionally, following special characters are available:
* *    middle dot "·"
* ->   right arrow "→"
* <->  pair of arrows "⇄"
* <>   equilibrium arrow "⇌" 
* hnu  hν


Examples
--------

	>>> import markdown
	>>> md = markdown.Markdown(extensions=['mdx_simplechem'])
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
