from __future__ import absolute_import
from __future__ import print_function
import os
from mojo.extensions import ExtensionBundle


basePath = os.path.dirname(__file__)
extensionPath = os.path.join(basePath, "word-o-mat.roboFontExt")
libPath = os.path.join(basePath, "lib")
htmlPath = os.path.join(basePath, "html")
resourcesPath = os.path.join(basePath, "resources")

B = ExtensionBundle()

B.name = "word-o-mat"
B.version = "2.2.7"
B.developer = "Nina Stoessinger"
B.developerURL = 'www.ninastoessinger.com'

B.launchAtStartUp = False
B.addToMenu = [
    {
        'path' : 'wordomat.py',
        'preferredName': 'word-o-mat',
        'shortKey' : '',
    }]
    
B.requiresVersionMajor = '3'
B.requiresVersionMinor = '1'
B.infoDictionary["html"] = True

B.save(extensionPath, libPath=libPath, htmlPath=htmlPath, resourcesPath=resourcesPath, pycOnly=False)

print("Done")