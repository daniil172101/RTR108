<Qucs Schematic 0.0.18>
<Properties>
  <View=0,-60,800,980,1,0,180>
  <Grid=10,10,1>
  <DataSet=02.dat>
  <DataDisplay=02.dpl>
  <OpenDisplay=1>
  <Script=02.m>
  <RunScript=0>
  <showFrame=0>
  <FrameText0=Title>
  <FrameText1=Drawn By:>
  <FrameText2=Date:>
  <FrameText3=Revision:>
</Properties>
<Symbol>
</Symbol>
<Components>
  <Vdc V1 1 140 390 18 -26 0 1 "1 V" 1>
  <R R1 1 270 360 -26 15 0 0 "50 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "european" 0>
  <GND * 1 400 460 0 0 0 0>
  <GND * 1 140 460 0 0 0 0>
  <.DC DC1 1 190 450 0 46 0 0 "26.85" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "no" 0 "150" 0 "no" 0 "none" 0 "CroutLU" 0>
  <R R2 1 400 390 15 -26 0 1 "x" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "european" 0>
  <.SW SW1 1 540 320 0 77 0 0 "DC1" 1 "lin" 1 "x" 1 "5 Ohm" 1 "50 Ohm" 1 "10" 1>
</Components>
<Wires>
  <140 360 240 360 "" 0 0 0 "">
  <300 360 400 360 "izeja" 390 310 69 "">
  <140 420 140 460 "" 0 0 0 "">
  <400 420 400 460 "" 0 0 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
