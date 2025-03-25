"""
Circuit Diagrams using Python
-----------------------------
Schemdraw is a python package for producing high-quality electrical circuit
schematic diagrams. Included are symbols for basic electrical components
(resistors, capacitors, diodes, transistors, etc.), opamps and
signal processing elements.
Additionally, Schemdraw can produce digital timing diagrams, state machine diagrams,
and flowcharts.
"""
import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing(color="red") as d:
    elm.Resistor().label('100KΩ')
    elm.Capacitor().down().label('0.1μF', loc='bottom')
    elm.Line().left()
    elm.Ground()
    elm.SourceV().up().label('10V')
