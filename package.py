name = "yamlcpp"

version = "0.8.0"

authors = [
    "Jesse Beder"
]

description = \
    """
    yaml-cpp is a YAML parser and emitter in C++ matching the YAML 1.2 spec.
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
]

uuid = "repository.yaml-cpp"

def pre_build_commands():

    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        command("source /opt/rh/devtoolset-6/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass

def commands():
    env.YAMLCPP_ROOT_DIR = "{root}"
    env.LIBRARY_PATH.append("{root}/lib64")  # yaml-cpp is built as static lib, so LIBRARY_PATH
