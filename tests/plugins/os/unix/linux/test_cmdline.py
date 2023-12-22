from dissect.target.filesystem import VirtualFilesystem
from dissect.target.plugins.os.unix.linux.proc import ProcPlugin
from dissect.target.target import Target


def test_cmdline(target_linux_users: Target, fs_linux_proc: VirtualFilesystem):
    target_linux_users.add_plugin(ProcPlugin)
    results = list(target_linux_users.cmdline())
    assert len(results) == 4