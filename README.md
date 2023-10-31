# APKPuller
Tool extract APKs from device to desktop directories

## Install 
```bash
pip3 install apkpuller
```

## How to use

- Help menu

<p align="left">
<img src="/images/help.png">
</p>
<br>

- List all packages

```bash
apkpuller -l
```
<br>

- Grep the package list

```bash
apkpuller -l -g install
```

<p align="left">
<img src="/images/grepPackage.png">
</p>
<br>

- view paths of the APKs in a package

```bash
apkpuller -v [Package Name]
```

<p align="left">
<img src="/images/grepPackage.png">
</p>
<br>

- ADB extracts APK into directories 

```bash
apkpuller -p <package name> <directory>
```

<p align="left">
<img src="/images/APKPull.png">
</p>