## This script creates selects a zoom layer, legend, color ramp, and title for a shapefile and exports a jpg##
## Inputs: shapefiles ##
## Output: jpegs ##
## Author Adam D. Griffith and Alexander Hohl, 1 FEB 2018.  adamdgriffith@gmail.com ##

import arcpy
arcpy.env.workspace = 'C:\\Users\\agriff73\\Desktop\\UNCCCourses\\ResearchProjects\\H4H\\BC_Land_value_sf'
arcpy.env.overwriteOutput = True

imageFolder = 'C:\\Users\\agriff73\\Desktop\\UNCCCourses\\ResearchProjects\\H4H\\images'
mxdPath = 'C:\\Users\\agriff73\\Desktop\\UNCCCourses\\ResearchProjects\H4H\\H4Hwest.mxd'
mxd = arcpy.mapping.MapDocument(mxdPath)
df = arcpy.mapping.ListDataFrames(mxd)[0]
print df
lyrlist = arcpy.mapping.ListLayers(mxd, "", df)
for lyr in lyrlist:
#    lyr.visible = True
#    arcpy.mapping.ExportToJPEG(mxd, imageFolder + '\\' + str(lyr.name) + ".jpg")
#    print lyr.name

    lyr.visible = True
    year_text = arcpy.mapping.ListLayoutElements (mxd, "TEXT_ELEMENT")
    year_text [0].text = lyr.name
    arcpy.mapping.ExportToJPEG(mxd, imageFolder + '\\' + str(lyr.name) + ".jpg")    
    lyr.visible = False


#lyrFolder = path to folder of physical layer files on disk

# Execute AddField new field LanValSf
#for i in range (2006, 2019):
#    print('C:\\Users\\agriff73\\Desktop\\UNCCCourses\\ResearchProjects\\H4H\\BC_Land_value_sf\\property_' + str(i) + '.shp')
