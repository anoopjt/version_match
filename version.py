#author: Anoop Jacob Thomas
#license: GPL v3

class Version:
    """This class implements version checking of a package
Usage:
version = Version(package, required_package_version
                  [, package_name, version_string])
print(version)
version.verify()"""
    def __init__(self, package, required_package_version,
                 package_name = "", version_string = ""):
        if package_name == "":
            self.package = package
            self.package_name = package.__name__
        else:
            self.package_name = package_name
        if version_string == "":
            self.package_version_string = package.__version__
        else:
            self.package_version_string = version_string
        self.required_package_version = required_package_version
        
    def __str__(self):
        prefix = "%s version %s" % (self.package_name, "%s")
        return (prefix % ("\033[0;32mmatch\033[0;0m" if self.verify()
                          else "\033[1;31mmismatch\033[0;0m"))

    def verify(self):
        return (True if (self.package_version_string.startswith(
            self.required_package_version)) else False)

if __name__ == "__main__":
    import os
    import sys
    
    try:
        import pandas as pd
    except ImportError:
        os.system('pip3 install pandas==0.23.4')
        import pandas as pd
    try:
        import numpy as np
    except ImportError:
        os.system("pip3 install numpy==1.15.2")
        import numpy as np

    pandas_version = Version(pd, '0.23.4')
    numpy_version = Version(np, '1.15.2')
    python_version = Version(sys, '3.7.0', 'python', sys.version)

    print(python_version)
    print(pandas_version)
    if(not pandas_version.verify()):
        print("Install correct pandas version")
        print("\tUsing: pip3 install pandas==0.23.4")
    print(numpy_version)
    if(not numpy_version.verify()):
        print("Install correct numpy version")
        print("\tUsing: pip3 install numpy==1.15.2")
