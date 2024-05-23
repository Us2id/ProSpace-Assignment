import win32com.client as wc
import math

def draw_sketch(radius, angle_rad, height):
    oApp = wc.GetActiveObject('Inventor.Application')

    oPartDoc = oApp.Documents.Add(12290, oApp.FileManager.GetTemplateFile(12290, 8962))

    oSketch = oPartDoc.ComponentDefinition.Sketches.Add(oPartDoc.ComponentDefinition.WorkPlanes.Item(3))

    oTG = oApp.TransientGeometry

    oSkPnts = oSketch.SketchPoints
    oSkPnts.Add(oTG.CreatePoint2d(0, 0), False)
    oSkPnts.Add(oTG.CreatePoint2d(radius, 0), False)
    oSkPnts.Add(oTG.CreatePoint2d(radius * math.cos(angle_rad), radius * math.sin(angle_rad)), False)

    oLines = oSketch.SketchLines
    oLine1 = oLines.AddByTwoPoints(oSkPnts(1), oSkPnts(2))
    oLine2 = oLines.AddByTwoPoints(oSkPnts(3), oSkPnts(1))

    oArc = oSketch.SketchArcs
    oArc1 = oArc.AddByCenterStartEndPoint(oSkPnts(1), oSkPnts(2), oSkPnts(3))

    oApp.ActiveView.GoHome()

    oProfile = oSketch.Profiles.AddForSolid()

    oExtFeature = oPartDoc.ComponentDefinition.Features.ExtrudeFeatures.AddByDistanceExtent(oProfile, height, 20995, 20481)
    oApp.ActiveView.Fit

radius_input = float(input("Enter radius: "))
height_input = float(input("Enter height: "))
angle_input = math.radians(float(input("Enter angle (0-360 degrees): ")))

draw_sketch(radius_input, angle_input, height_input)