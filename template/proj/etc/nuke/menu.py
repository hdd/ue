import os, glob

import ueNuke
import ueNuke.Save as ueNukeSave
import ueNuke.Open as ueNukeOpen
import ueNuke.Read as ueNukeRead
import ueNuke.Load as ueNukeLoad
import ueNuke.Checker as ueNukeChecker
import ueNuke.NodeTools as ueNukeNodeTools

checker = ueNuke.checker

# Utilities
def getReadPath():
    return ueNuke.getReadPath()

def ueRead():
    ueReadPanel.show()

def ueChecker():
    # The following two lines are a bit of a hack to make sure the
    # script checker gets updated every time its opened.
    # Else, when you open a new script, the panel doesn't get redrawn
    # and it 'saves' the info from then previous script.
    # Un-registering and regstering the widget seems to do the trick.
    nukescripts.unregisterPanel("ue.panel.ueChecker", None)
    ueCheckerPanel = nukescripts.registerWidgetAsPanel("ueNukeChecker.CheckerPanel", "ueChecker", "ue.panel.ueChecker", create=True)
    ueCheckerPanel.show()

def getReadPath():
    return ueNuke.getReadPath()

def nukeChecker():
    checks = checker["nuke"]

    for check in checks:
        c = checks[check]
        if (lambda: eval(c["eval"]))():
            ueChecker()
            break

# Menus
ueMenu = "ue&Tools"
nuke.menu("Nuke").addCommand(ueMenu+"/&Open",
                             ueNukeOpen.ueOpen, "Ctrl+o")
nuke.menu("Nuke").addCommand(ueMenu+"/&Save",
                             ueNukeSave.ueSave, "Ctrl+s")
nuke.menu("Nuke").addCommand(ueMenu+"/Save &As...",
                             ueNukeSave.ueSaveAs, "Ctrl+Shift+s")
nuke.menu("Nuke").addCommand(ueMenu+"/Save New &Version",
                             ueNukeSave.ueSaveVers, "Ctrl+Alt+s")
nuke.menu("Nuke").addCommand(ueMenu+"/-", "", "")
ueNukeLoad.addGizmos()
nuke.menu("Nuke").addCommand(ueMenu+"/-", "", "")
nuke.menu("Nuke").addCommand(ueMenu+"/ueRead", ueRead)
nuke.menu("Nuke").addCommand(ueMenu+"/ueChecker", ueChecker)

# Favorites
nuke.addFavoriteDir("asst root",
                    os.getenv("ASST_ROOT"),
                    nuke.ALL)
nuke.addFavoriteDir("render",
                    os.path.join(os.getenv("ASST_ROOT"), "render"),
                    nuke.IMAGE)

# Auto-run
nuke.addOnUserCreate(ueNuke.ueNewScriptSetup, nodeClass="Root")
nuke.addOnScriptLoad(nukeChecker)
nuke.addBeforeRender(ueNuke.render, nodeClass="Write")

#nuke.addOnUserCreate(ueNukeNodeTools.initElementsKnob)
#nuke.addKnobChanged(ueNukeNodeTools.updateElementsKnob)

# Register panels
ueReadPanel = nukescripts.registerWidgetAsPanel("ueNukeRead.ReadPanel", "ueRead", "ue.panel.ueRead", create=True)
ueCheckerPanel = nukescripts.registerWidgetAsPanel("ueNukeChecker.CheckerPanel", "ueChecker", "ue.panel.ueChecker", create=True)

