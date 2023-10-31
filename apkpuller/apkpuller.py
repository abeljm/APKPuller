import os
import subprocess
import argparse
from colorama import Fore

def printError(msg): 
    print(f"{Fore.RED}[-] {msg}{Fore.RESET}")

def printSuccess(msg):
    print(f"{Fore.GREEN}[+] {msg}{Fore.RESET}")

def adb_installed():
    cmd = "adb version"
    try:
        subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        printError("No se encuentra adb instalado. La aplicación se cerrará.")
        exit(1)

def listPackages():
	packages = []
	try:
	    result = subprocess.check_output(["adb", "shell", "pm", "list", "packages"], universal_newlines=True)
	    package_lines = result.split('\n')
	    for line in package_lines:
	    	line = line[8:].strip()
	    	if line:
	    		packages.append(line)
	    return packages
	except subprocess.CalledProcessError as e:
		return null

def checkPackageExists(package_name):
    try:        
        package_lines = listPackages()
        for line in package_lines:
        	if package_name.lower() in line.lower():
        		return True
        return False
    except subprocess.CalledProcessError as e:
    	return False

def getPathAPK(package_name):
    try:
    	packages = []
    	result = subprocess.check_output(["adb", "shell", "pm", "path", package_name], universal_newlines=True)
    	package_lines = result.split('\n')
    	for line in package_lines:
    		line = line[8:].strip()
    		if line:
    			packages.append(line)
    	return packages
    except subprocess.CalledProcessError as e:
    	return null

def getAPKs(apk_paths, user_directory="."):
    for apk_path in apk_paths:
        try:
            apk_filename = os.path.basename(apk_path)

            if user_directory == ".":
                destination_path = os.path.join(os.getcwd(), apk_filename) 
            else:
                destination_path = os.path.join(user_directory, apk_filename)

            subprocess.run(["adb", "pull", apk_path, destination_path], check=True, stdout=subprocess.PIPE)
            printSuccess(f"APK downloaded successfully to directory '{destination_path}'")
        except subprocess.CalledProcessError as e:
            printError(f"Error downloading APK '{apk_path}': {e}")

def main():    
    parser = argparse.ArgumentParser()
    #parser.add_argument('-q', help='Ocultar banner', action='store_true')
    parser.add_argument('-l', '--list', help='list packages', action='store_true')
    parser.add_argument('-c', '--check', help='check if package is on mobile', metavar='')
    parser.add_argument('-g', '--grep', help='search packet in packet list', metavar='')
    parser.add_argument('-v', '--view', help='view paths of the APKs in a package.', metavar='')
    parser.add_argument('-p', '--pull', nargs=2, help='adb extracts APK into directories <package name> <directory>', metavar='')
    
    args = parser.parse_args()

    adb_installed()

    if args.list:
        packages = listPackages()
        if args.grep:
            packages = [package for package in packages if args.grep in package]
        for package in packages:
            printSuccess(package)

    if args.check:
    	if checkPackageExists(args.check):
    		printSuccess(f"{args.check} - package exists")
    	else:
    		printError(f"{args.check} - package does not exist")

    if args.view:
    	apks = getPathAPK(args.view)
    	for apk in apks:
    		printSuccess(apk)

    if args.pull:
    	packagename, directory = args.pull
    	apks = getPathAPK(packagename)
    	getAPKs(apks, directory)

if __name__ == "__main__":
    main()