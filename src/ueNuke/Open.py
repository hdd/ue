import os

import nuke, nukescripts

import ueSpec

import ueCore.AssetUtils as ueAssetUtils
import ueCommon.Open as ueCommonOpen

__ueclasses__          = ["ns"]
__ueclasses_read__     = ["nr", "mr", "cel", "bg", "an", "sb"]
__ueclasses_read_geo__ = ["geo"]
__ueclasses_write__    = ["nr"]

def ueOpen():
    p = nukescripts.registerWidgetAsPanel("ueCommonOpen.Open", "ueOpen",
                                          "ue.panel.ueOpen", create=True)
    p.setMinimumSize(600, 940)
    ueCommonOpen.setClasses(__ueclasses__)

    if p.showModalDialog():
        spec = ueCommonOpen.getValues()
        version = ueAssetUtils.getVersions(spec)[spec.vers-1]
        nuke.scriptOpen(os.path.join(version["path"], version["file_name"]+".nk"))
        nuke.tprint("Opened %s" % spec)

    nukescripts.unregisterPanel("ue.panel.ueOpen", lambda: "return")

def ueOpenRead():
    p = nukescripts.registerWidgetAsPanel("ueCommonOpen.Open", "ueOpen",
                                          "ue.panel.ueOpen", create=True)
    p.setMinimumSize(600, 940)
    ueCommonOpen.setClasses(__ueclasses_read__)

    if p.showModalDialog():
        spec = ueCommonOpen.getValues()
        n = nuke.thisNode()
        n.knob("proj").setValue(spec.proj)
        n.knob("grp").setValue(spec.grp)
        n.knob("asst").setValue(spec.asst)
        n.knob("elclass").setValue(spec.elclass)
        n.knob("eltype").setValue(spec.eltype)
        n.knob("elname").setValue(spec.elname)
        n.knob("vers").setValue(int(spec.vers))
        n.knob("elpass").setValue(spec.elpass)

    nukescripts.unregisterPanel("ue.panel.ueOpen", lambda: "return")

def ueOpenReadGeo():
    p = nukescripts.registerWidgetAsPanel("ueCommonOpen.Open", "ueOpen",
                                          "ue.panel.ueOpen", create=True)
    p.setMinimumSize(600, 940)
    ueCommonOpen.setClasses(__ueclasses_read_geo__)

    if p.showModalDialog():
        spec = ueCommonOpen.getValues()
        n = nuke.thisNode()
        n.knob("proj").setValue(spec.proj)
        n.knob("grp").setValue(spec.grp)
        n.knob("asst").setValue(spec.asst)
        n.knob("elclass").setValue(spec.elclass)
        n.knob("eltype").setValue(spec.eltype)
        n.knob("elname").setValue(spec.elname)
        n.knob("vers").setValue(int(spec.vers))

    nukescripts.unregisterPanel("ue.panel.ueOpen", lambda: "return")

#def ueOpenWrite():
#    p = nukescripts.registerWidgetAsPanel("ueCommonOpen.Open", "ueOpen",
#                                          "ue.panel.ueOpen", create=True)
#    p.setMinimumSize(600, 940)
#    ueCommonOpen.setClasses(__ueclasses_write__)
#
#    if p.showModalDialog():
#        spec = ueCommonOpen.getValues()
#        n = nuke.thisNode()
#        n.knob("proj").setValue(spec.proj)
#        n.knob("grp").setValue(spec.grp)
#        n.knob("asst").setValue(spec.asst)
#        n.knob("elclass").setValue(spec.elclass)
#        n.knob("eltype").setValue(spec.eltype)
#        n.knob("elname").setValue(spec.elname)
#
#    nukescripts.unregisterPanel("ue.panel.ueOpen", lambda: "return")

