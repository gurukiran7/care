from plugs.manager import PlugManager
from plugs.plug import Plug

plugs = [
    Plug(
        name="hrm",
        package_name="git+https://github.com/gurukiran7/care_hrm_be.git",
        version="",
        configs={},
    ),
]

manager = PlugManager(plugs)
