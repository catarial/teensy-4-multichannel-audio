from os.path import join, isfile, isdir
from os import remove

Import("env")

FRAMEWORK_DIR = env.PioPlatform().get_package_dir("framework-arduinoteensy")
patchflag_path = join(FRAMEWORK_DIR, ".patching-done")

def undo_patch(*args, **kwargs):
    if isfile(join(FRAMEWORK_DIR, ".patching-done")):
        original_file = FRAMEWORK_DIR
        patched_file = join("patches", "core.patch")

        assert isdir(original_file) and isfile(patched_file)

        env.Execute("patch -R -d %s -p1 < %s" % (original_file, patched_file))
        # env.Execute("touch " + patchflag_path)

        remove(patchflag_path)

env.AddCustomTarget("undo_patch", None, undo_patch)

