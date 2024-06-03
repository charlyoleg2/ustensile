# freecad-python generated by Parametrix
# run the script with:
# freecad.cmd myScript.py

import FreeCAD as App
import Part

#print(sys.argv)
outFileName = "spiral"
if (len(sys.argv) == 3):
    outFileName = sys.argv[2]
print(f"outFileName: {outFileName}")

def ctr_face_spiral_faceTop_Fa0_Ctr0():
	P000 = App.Vector(-30.0000, 0.0000, 0)
	P001 = App.Vector(-35.0000, 5.0000, 0)
	P002 = App.Vector(-40.0000, 0.0000, 0)
	S000 = Part.Arc(P000, P001, P002)
	P003 = App.Vector(-28.2843, -28.2843, 0)
	P004 = App.Vector(-0.0000, -40.0000, 0)
	S001 = Part.Arc(P002, P003, P004)
	P005 = App.Vector(30.9359, -27.1859, 0)
	P006 = App.Vector(43.7500, 3.7500, 0)
	S002 = Part.Arc(P004, P005, P006)
	P007 = App.Vector(29.8376, 37.3376, 0)
	P008 = App.Vector(-3.7500, 51.2500, 0)
	S003 = Part.Arc(P006, P007, P008)
	P009 = App.Vector(-39.9892, 36.2392, 0)
	P010 = App.Vector(-55.0000, 0.0000, 0)
	S004 = Part.Arc(P008, P009, P010)
	P011 = App.Vector(-38.8909, -38.8909, 0)
	P012 = App.Vector(-0.0000, -55.0000, 0)
	S005 = Part.Arc(P010, P011, P012)
	P013 = App.Vector(41.5425, -37.7925, 0)
	P014 = App.Vector(58.7500, 3.7500, 0)
	S006 = Part.Arc(P012, P013, P014)
	P015 = App.Vector(40.4442, 47.9442, 0)
	P016 = App.Vector(-3.7500, 66.2500, 0)
	S007 = Part.Arc(P014, P015, P016)
	P017 = App.Vector(-50.5958, 46.8458, 0)
	P018 = App.Vector(-70.0000, 0.0000, 0)
	S008 = Part.Arc(P016, P017, P018)
	P019 = App.Vector(-49.4975, -49.4975, 0)
	P020 = App.Vector(-0.0000, -70.0000, 0)
	S009 = Part.Arc(P018, P019, P020)
	P021 = App.Vector(5.0000, -65.0000, 0)
	P022 = App.Vector(-0.0000, -60.0000, 0)
	S010 = Part.Arc(P020, P021, P022)
	P023 = App.Vector(-42.4264, -42.4264, 0)
	P024 = App.Vector(-60.0000, 0.0000, 0)
	S011 = Part.Arc(P022, P023, P024)
	P025 = App.Vector(-43.5248, 39.7748, 0)
	P026 = App.Vector(-3.7500, 56.2500, 0)
	S012 = Part.Arc(P024, P025, P026)
	P027 = App.Vector(33.3731, 40.8731, 0)
	P028 = App.Vector(48.7500, 3.7500, 0)
	S013 = Part.Arc(P026, P027, P028)
	P029 = App.Vector(34.4715, -30.7215, 0)
	P030 = App.Vector(-0.0000, -45.0000, 0)
	S014 = Part.Arc(P028, P029, P030)
	P031 = App.Vector(-31.8198, -31.8198, 0)
	P032 = App.Vector(-45.0000, 0.0000, 0)
	S015 = Part.Arc(P030, P031, P032)
	P033 = App.Vector(-32.9182, 29.1682, 0)
	P034 = App.Vector(-3.7500, 41.2500, 0)
	S016 = Part.Arc(P032, P033, P034)
	P035 = App.Vector(22.7665, 30.2665, 0)
	P036 = App.Vector(33.7500, 3.7500, 0)
	S017 = Part.Arc(P034, P035, P036)
	P037 = App.Vector(23.8649, -20.1149, 0)
	P038 = App.Vector(-0.0000, -30.0000, 0)
	S018 = Part.Arc(P036, P037, P038)
	P039 = App.Vector(-21.2132, -21.2132, 0)
	P040 = App.Vector(-30.0000, 0.0000, 0)
	S019 = Part.Arc(P038, P039, P040)
	aShape = Part.Shape([S000, S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_spiral_faceTop_Fa0():
	FC000 = ctr_face_spiral_faceTop_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def spiral_faceTop():
	FA000 = face_spiral_faceTop_Fa0()
	rOneFig = FA000
	rOneFig.check()
	return rOneFig

def ctr_face_spiral_faceSide_Fa0_Ctr0():
	P000 = App.Vector(-40.0000, 0.0000, 0)
	P001 = App.Vector(-30.0000, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-30.0000, 50.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-40.0000, 50.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-40.0000, 0.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_spiral_faceSide_Fa0():
	FC000 = ctr_face_spiral_faceSide_Fa0_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_spiral_faceSide_Fa1_Ctr0():
	P000 = App.Vector(33.7500, 0.0000, 0)
	P001 = App.Vector(43.7500, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(43.7500, 50.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(33.7500, 50.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(33.7500, 0.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_spiral_faceSide_Fa1():
	FC000 = ctr_face_spiral_faceSide_Fa1_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_spiral_faceSide_Fa2_Ctr0():
	P000 = App.Vector(-55.0000, 0.0000, 0)
	P001 = App.Vector(-45.0000, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-45.0000, 50.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-55.0000, 50.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-55.0000, 0.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_spiral_faceSide_Fa2():
	FC000 = ctr_face_spiral_faceSide_Fa2_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_spiral_faceSide_Fa3_Ctr0():
	P000 = App.Vector(48.7500, 0.0000, 0)
	P001 = App.Vector(58.7500, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(58.7500, 50.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(48.7500, 50.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(48.7500, 0.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_spiral_faceSide_Fa3():
	FC000 = ctr_face_spiral_faceSide_Fa3_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def ctr_face_spiral_faceSide_Fa4_Ctr0():
	P000 = App.Vector(-70.0000, 0.0000, 0)
	P001 = App.Vector(-60.0000, 0.0000, 0)
	S000 = Part.LineSegment(P000, P001)
	P002 = App.Vector(-60.0000, 50.0000, 0)
	S001 = Part.LineSegment(P001, P002)
	P003 = App.Vector(-70.0000, 50.0000, 0)
	S002 = Part.LineSegment(P002, P003)
	P004 = App.Vector(-70.0000, 0.0000, 0)
	S003 = Part.LineSegment(P003, P004)
	aShape = Part.Shape([S000, S001, S002, S003])
	aWire = Part.Wire(aShape.Edges)
	subFace = Part.Face(aWire)
	subFace.check()
	return subFace

def face_spiral_faceSide_Fa4():
	FC000 = ctr_face_spiral_faceSide_Fa4_Ctr0()
	rOneFace = FC000
	rOneFace.check()
	return rOneFace

def spiral_faceSide():
	FA000 = face_spiral_faceSide_Fa0()
	FA001 = face_spiral_faceSide_Fa1()
	FA002 = face_spiral_faceSide_Fa2()
	FA003 = face_spiral_faceSide_Fa3()
	FA004 = face_spiral_faceSide_Fa4()
	rOneFig = FA000.fuse([FA001, FA002, FA003, FA004])
	rOneFig.check()
	return rOneFig

def fex_subpax_spiral():
	FIG = spiral_faceTop()
	VEX = FIG.extrude(App.Vector(0, 0, 50))
	VR1 = VEX.rotate(App.Vector(0, 0, 0), App.Vector(1, 0, 0), 0)
	VR2 = VR1.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 0)
	VR3 = VR2.rotate(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 0)
	VFP = VR3.translate(App.Vector(0, 0, 0))
	return VFP
subpax_spiral = fex_subpax_spiral()

pax_spiral = subpax_spiral

pax_spiral.check()
#pax_spiral.exportBrep(f"{outFileName}.brep")
#pax_spiral.exportIges(f"{outFileName}.igs")
#pax_spiral.exportStep(f"{outFileName}.stp")
pax_spiral.exportStl(f"{outFileName}.stl")

