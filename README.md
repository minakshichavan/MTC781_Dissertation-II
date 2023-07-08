# MTC781_Dissertation-II

Dissertation 2 - Secured Package and Data Transmission through DevOps Methodology - POC

# Red Hat Package Manager for Payload Delivery
## _A Dissertation 2 Project PoC by Minakshi Pushpendra Chavan_


## Step 1 - Understanding the base system.
The base system used to create and build the MTC781 package is Red Hat Enterprise Linux 7.9 machine. The `rpm-build` and `rpm-sign` packages are already installed as follows.
```
[minakshichavan@rhel7-basemachine ~]$ whoami
minakshichavan

[minakshichavan@rhel7-basemachine ~]$ date
Sat Jul  8 19:12:25 IST 2023

[minakshichavan@rhel7-basemachine ~]$ sudo rpm -q rpm-build rpm-sign
rpm-build-4.11.3-48.el7_9.x86_64
rpm-sign-4.11.3-48.el7_9.x86_64

[minakshichavan@rhel7-basemachine ~]$ cat /etc/redhat-release 
Red Hat Enterprise Linux Server release 7.9 (Maipo)

[minakshichavan@rhel7-basemachine ~]$ uname -a 
Linux rhel7-basemachine 3.10.0-1160.92.1.el7.x86_64 #1 SMP Thu May 18 11:23:40 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
```

## Step 2 - Gather the MTC781 PoC code
Get the MTC781 PoC code, create a `tar.gz` archive in an appropriate `tree` structure and place it under `~/rpmbuild` directory as follows.
```
[minakshichavan@rhel7-basemachine ~]$ mkdir -p MTC781-1.0.0/{usr,usr/local,usr/local/man/man8,usr/bin,etc,etc/MTC781}
[minakshichavan@rhel7-basemachine ~]$ tree MTC781-1.0.0
MTC781-1.0.0
├── etc
│   └── MTC781
└── usr
    ├── bin
    └── local
        └── man
            └── man8

7 directories, 0 files

Polulate the Data

[minakshichavan@rhel7-basemachine ~]$ tree MTC781-1.0.0/
MTC781-1.0.0/
├── etc
│   └── MTC781
│       └── MTC781.conf
└── usr
    ├── bin
    │   ├── MTC781-ansible_task01
    │   ├── MTC781-ansible_task02
    │   ├── MTC781-ansible_task03
    │   ├── MTC781-ansible_task04
    │   ├── MTC781-ansible_task05
    │   ├── MTC781-ansible_task06
    │   ├── MTC781-ansible_task07
    │   ├── MTC781-ansible_task08
    │   ├── MTC781-ansible_task09
    │   └── MTC781-bin
    └── local
        └── man
            ├── man1
            │   └── MTC781.1.gz
            └── man8

8 directories, 12 files


[minakshichavan@rhel7-basemachine ~]$ tar cvf MTC781-1.0.0.tar.gz MTC781-1.0.0
MTC781-1.0.0/
MTC781-1.0.0/usr/
MTC781-1.0.0/usr/local/
MTC781-1.0.0/usr/local/man/
MTC781-1.0.0/usr/local/man/man8/
MTC781-1.0.0/usr/local/man/man1/
MTC781-1.0.0/usr/local/man/man1/MTC781.1.gz
MTC781-1.0.0/usr/bin/
MTC781-1.0.0/usr/bin/MTC781-bin
MTC781-1.0.0/usr/bin/MTC781-ansible_task01
MTC781-1.0.0/usr/bin/MTC781-ansible_task02
MTC781-1.0.0/usr/bin/MTC781-ansible_task03
MTC781-1.0.0/usr/bin/MTC781-ansible_task04
MTC781-1.0.0/usr/bin/MTC781-ansible_task05
MTC781-1.0.0/usr/bin/MTC781-ansible_task06
MTC781-1.0.0/usr/bin/MTC781-ansible_task07
MTC781-1.0.0/usr/bin/MTC781-ansible_task08
MTC781-1.0.0/usr/bin/MTC781-ansible_task09
MTC781-1.0.0/etc/
MTC781-1.0.0/etc/MTC781/
MTC781-1.0.0/etc/MTC781/MTC781.conf

[minakshichavan@rhel7-basemachine ~]$ tar tvf MTC781-1.0.0.tar.gz 
drwxrwxr-x minakshichavan/minakshichavan 0 2023-07-08 19:28 MTC781-1.0.0/
drwxrwxr-x minakshichavan/minakshichavan 0 2023-07-08 19:28 MTC781-1.0.0/usr/
drwxrwxr-x minakshichavan/minakshichavan 0 2023-07-08 19:28 MTC781-1.0.0/usr/local/
drwxrwxr-x minakshichavan/minakshichavan 0 2023-07-08 19:40 MTC781-1.0.0/usr/local/man/
drwxrwxr-x minakshichavan/minakshichavan 0 2023-07-08 19:28 MTC781-1.0.0/usr/local/man/man8/
drwxrwxr-x minakshichavan/minakshichavan 0 2023-07-08 19:42 MTC781-1.0.0/usr/local/man/man1/
-rwxr-xr-x minakshichavan/minakshichavan 345 2023-07-08 19:42 MTC781-1.0.0/usr/local/man/man1/MTC781.1.gz
drwxrwxr-x minakshichavan/minakshichavan   0 2023-07-08 19:46 MTC781-1.0.0/usr/bin/
-rwxr-xr-x minakshichavan/minakshichavan 1046 2023-07-08 19:45 MTC781-1.0.0/usr/bin/MTC781-bin
-rw-rw-r-- minakshichavan/minakshichavan    0 2023-07-08 19:46 MTC781-1.0.0/usr/bin/MTC781-ansible_task01
-rw-rw-r-- minakshichavan/minakshichavan    0 2023-07-08 19:46 MTC781-1.0.0/usr/bin/MTC781-ansible_task02
-rw-rw-r-- minakshichavan/minakshichavan    0 2023-07-08 19:46 MTC781-1.0.0/usr/bin/MTC781-ansible_task03
-rw-rw-r-- minakshichavan/minakshichavan    0 2023-07-08 19:46 MTC781-1.0.0/usr/bin/MTC781-ansible_task04
-rw-rw-r-- minakshichavan/minakshichavan    0 2023-07-08 19:46 MTC781-1.0.0/usr/bin/MTC781-ansible_task05
-rw-rw-r-- minakshichavan/minakshichavan    0 2023-07-08 19:46 MTC781-1.0.0/usr/bin/MTC781-ansible_task06
-rw-rw-r-- minakshichavan/minakshichavan    0 2023-07-08 19:46 MTC781-1.0.0/usr/bin/MTC781-ansible_task07
-rw-rw-r-- minakshichavan/minakshichavan    0 2023-07-08 19:46 MTC781-1.0.0/usr/bin/MTC781-ansible_task08
-rw-rw-r-- minakshichavan/minakshichavan    0 2023-07-08 19:46 MTC781-1.0.0/usr/bin/MTC781-ansible_task09
drwxrwxr-x minakshichavan/minakshichavan    0 2023-07-08 19:28 MTC781-1.0.0/etc/
drwxrwxr-x minakshichavan/minakshichavan    0 2023-07-08 19:45 MTC781-1.0.0/etc/MTC781/
-rwxr-xr-x root/root                       58 2023-07-08 19:38 MTC781-1.0.0/etc/MTC781/MTC781.conf


[minakshichavan@rhel7-basemachine ~]$ ls -lR rpmbuild/
total 0
drwxrwxr-x. 2 minakshichavan minakshichavan 33 Jul  8 19:48 SOURCES
drwxrwxr-x. 2 minakshichavan minakshichavan 25 Jul  8 19:57 SPECS

rpmbuild/SOURCES:
total 4
-rw-rw-r--. 1 minakshichavan minakshichavan 20480 Jul  8 19:48 MTC781-1.0.0.tar.gz

rpmbuild/SPECS:
total 4
-rw-rw-r--. 1 minakshichavan minakshichavan 2505 Jul  8 19:57 MTC781.spec

minakshichavan@rhel7-basemachine ~]$ file rpmbuild/SOURCES/MTC781-1.0.0.tar.gz rpmbuild/SPECS/MTC781.spec 
rpmbuild/SOURCES/MTC781-1.0.0.tar.gz: POSIX tar archive (GNU)
rpmbuild/SPECS/MTC781.spec:           ASCII text
```
## Step 3 - Create a SPEC file 
The `spec` file is an important part of the build process for an `rpm` package. All necessary fields can be populated in here.
```
[minakshichavan@rhel7-basemachine ~]$ cat rpmbuild/SPECS/MTC781.spec 
Summary: This is a dummy package built by Minakshi Pushpendra Chavan.
Name: MTC781
Version: 1.0.0
Release: 0.el7
Group: Applications/File
Source: MTC781-%{version}.tar.gz
BuildArch: noarch
Requires: bash
Requires: rpm
License: GPLv2+
Vendor: G S Mandal's Maharashtra Institute of Technology, Aurangabad 
Packager: Minakshi Pushpendra Chavan
BuildRoot:  %{_tmppath}/%{name}-buildroot

%description
This is a sample package to deliver the ansible pre-defined tasks as a payload through signed rpm package. This is just a PoC. 

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -m 0755 -d $RPM_BUILD_ROOT/etc/MTC781
install -m 0755 -d $RPM_BUILD_ROOT/usr/bin
install -m 0755 -d $RPM_BUILD_ROOT/usr/local/man/man1
install -m 0755 -d $RPM_BUILD_ROOT/usr/local/man/man8



install -p etc/MTC781/MTC781.conf $RPM_BUILD_ROOT/etc/MTC781/MTC781.conf
install -p usr/bin/MTC781-bin $RPM_BUILD_ROOT/usr/bin/MTC781-bin
install -p usr/bin/MTC781-ansible_task01 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task01
install -p usr/bin/MTC781-ansible_task02 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task02
install -p usr/bin/MTC781-ansible_task03 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task03
install -p usr/bin/MTC781-ansible_task04 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task04
install -p usr/bin/MTC781-ansible_task05 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task05
install -p usr/bin/MTC781-ansible_task06 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task06
install -p usr/bin/MTC781-ansible_task07 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task07
install -p usr/bin/MTC781-ansible_task08 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task08
install -p usr/bin/MTC781-ansible_task09 $RPM_BUILD_ROOT/usr/bin/MTC781-ansible_task09
install -p usr/local/man/man1/MTC781.1.gz $RPM_BUILD_ROOT/usr/local/man/man1/MTC781.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/MTC781-bin
/usr/bin/MTC781-ansible_task01
/usr/bin/MTC781-ansible_task02
/usr/bin/MTC781-ansible_task03
/usr/bin/MTC781-ansible_task04
/usr/bin/MTC781-ansible_task05
/usr/bin/MTC781-ansible_task06
/usr/bin/MTC781-ansible_task07
/usr/bin/MTC781-ansible_task08
/usr/bin/MTC781-ansible_task09
%config /etc/MTC781/MTC781.conf
%doc /usr/local/man/man1/MTC781.1.gz 

%post
echo "Please run "MTC781" command to view deployment !"
echo "Your constructive feedback will be highly appreciated!!!"

%postun

echo "Hope You liked this PoC!"

%changelog
* Sat Jul 08 2023 Minakshi Pushpendra Chavan <shenguleminakshi265@gmail.com> 1.0.0
- Initial version

```

## Step 4 - Build an RPM
The `rpmbuild` binary can be utilized to finally build an unsigned `rpm` package along with a source `rpm` as follows.
```
[minakshichavan@rhel7-basemachine ~]$ rpmbuild -ba rpmbuild/SPECS/MTC781.spec 
Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.7otmge
+ umask 022
+ cd /home/minakshichavan/rpmbuild/BUILD
+ cd /home/minakshichavan/rpmbuild/BUILD
+ rm -rf MTC781-1.0.0
+ /usr/bin/tar -xf /home/minakshichavan/rpmbuild/SOURCES/MTC781-1.0.0.tar.gz
+ cd MTC781-1.0.0
+ /usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
+ exit 0
Executing(%build): /bin/sh -e /var/tmp/rpm-tmp.TVPHpy
+ umask 022
+ cd /home/minakshichavan/rpmbuild/BUILD
+ cd MTC781-1.0.0
+ exit 0
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.tMxhzS
+ umask 022
+ cd /home/minakshichavan/rpmbuild/BUILD
+ '[' /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64 '!=' / ']'
+ rm -rf /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64
++ dirname /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64
+ mkdir -p /home/minakshichavan/rpmbuild/BUILDROOT
+ mkdir /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64
+ cd MTC781-1.0.0
+ rm -rf /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64
+ install -m 0755 -d /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64/etc/MTC781
+ install -m 0755 -d /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64/usr/bin
+ install -m 0755 -d /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64/usr/local/man/man1
+ install -m 0755 -d /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64/usr/local/man/man8
+ install -p etc/MTC781/MTC781.conf /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64/etc/MTC781/MTC781.conf
+ install -p usr/bin/MTC781-bin /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64/usr/bin/MTC781-bin
+ install -p usr/bin/MTC781-ansible_task01 /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64/usr/bin/MTC781-ansible_task01
+ install -p usr/bin/MTC781-ansible_task02 /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64/usr/bin/MTC781-ansible_task02
+ install -p usr/bin/MTC781-ansible_task03 /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64/usr/bin/MTC781-ansible_task03
+ install -p usr/bin/MTC781-ansible_task04 /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64/usr/bin/MTC781-ansible_task04
+ install -p usr/bin/MTC781-ansible_task05 /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64/usr/bin/MTC781-ansible_task05
+ install -p usr/bin/MTC781-ansible_task06 /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64/usr/bin/MTC781-ansible_task06
+ install -p usr/bin/MTC781-ansible_task07 /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64/usr/bin/MTC781-ansible_task07
+ install -p usr/bin/MTC781-ansible_task08 /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64/usr/bin/MTC781-ansible_task08
+ install -p usr/bin/MTC781-ansible_task09 /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64/usr/bin/MTC781-ansible_task09
+ install -p usr/local/man/man1/MTC781.1.gz /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64/usr/local/man/man1/MTC781.1.gz
+ /usr/lib/rpm/find-debuginfo.sh --strict-build-id -m --run-dwz --dwz-low-mem-die-limit 10000000 --dwz-max-die-limit 110000000 /home/minakshichavan/rpmbuild/BUILD/MTC781-1.0.0
/usr/lib/rpm/sepdebugcrcfix: Updated 0 CRC32s, 0 CRC32s did match.
+ /usr/lib/rpm/check-buildroot
+ /usr/lib/rpm/redhat/brp-compress
+ /usr/lib/rpm/redhat/brp-strip-static-archive /usr/bin/strip
+ /usr/lib/rpm/brp-python-bytecompile /usr/bin/python 1
+ /usr/lib/rpm/redhat/brp-python-hardlink
+ /usr/lib/rpm/redhat/brp-java-repack-jars
Processing files: MTC781-1.0.0-0.el7.noarch
Provides: MTC781 = 1.0.0-0.el7 config(MTC781) = 1.0.0-0.el7
Requires(interp): /bin/sh /bin/sh
Requires(rpmlib): rpmlib(CompressedFileNames) <= 3.0.4-1 rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires(post): /bin/sh
Requires(postun): /bin/sh
Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64
Wrote: /home/minakshichavan/rpmbuild/SRPMS/MTC781-1.0.0-0.el7.src.rpm
Wrote: /home/minakshichavan/rpmbuild/RPMS/noarch/MTC781-1.0.0-0.el7.noarch.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.7FEFgV
+ umask 022
+ cd /home/minakshichavan/rpmbuild/BUILD
+ cd MTC781-1.0.0
+ rm -rf /home/minakshichavan/rpmbuild/BUILDROOT/MTC781-1.0.0-0.el7.x86_64
+ exit 0
```
See the binary package created at `/home/minakshichavan/rpmbuild/RPMS/noarch/MTC781-1.0.0-0.el7.noarch.rpm` and source package at `/home/minakshichavan/rpmbuild/SRPMS/MTC781-1.0.0-0.el7.src.rpm` respectively. The created `rpm` package is in fact an unsigned package as follows. Observe the `Signature` part which shows as `(none)`, means it needs to get signed now.
```
[minakshichavan@rhel7-basemachine ~]$ sudo rpm -qip /home/minakshichavan/rpmbuild/RPMS/noarch/MTC781-1.0.0-0.el7.noarch.rpm
Name        : MTC781
Version     : 1.0.0
Release     : 0.el7
Architecture: noarch
Install Date: (not installed)
Group       : Applications/File
Size        : 1449
License     : GPLv2+
Signature   : (none)
Source RPM  : MTC781-1.0.0-0.el7.src.rpm
Build Date  : Saturday 08 July 2023 07:57:12 PM IST
Build Host  : rhel7-basemachine
Relocations : (not relocatable)
Packager    : Minakshi Pushpendra Chavan
Vendor      : G S Mandal's Maharashtra Institute of Technology, Aurangabad
Summary     : This is a dummy package built by Minakshi Pushpendra Chavan.
Description :
This is a sample package to deliver the ansible pre-defined tasks as a payload through signed rpm package. This is just a PoC.
```

## Step 5 - Generate GPG key to sign the rpm.
To get the package signed, one needs to have a private-public `gpg` keypair generated as follows.
```
[minakshichavan@rhel7-basemachine ~]$ gpg --gen-key
gpg (GnuPG) 2.0.22; Copyright (C) 2013 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
Your selection? 
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048) 
Requested keysize is 2048 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 0
Key does not expire at all
Is this correct? (y/N) y

GnuPG needs to construct a user ID to identify your key.

Real name: Minakshi Chavan
Email address: shenguleminakshi265@gmail.com
Comment: MTC781
You selected this USER-ID:
    "Minakshi Chavan (MTC781) <shenguleminakshi265@gmail.com>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O
You need a Passphrase to protect your secret key.

We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: key 7EEB6B3A marked as ultimately trusted
public and secret key created and signed.

gpg: checking the trustdb
gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
pub   2048R/7EEB6B3A 2023-07-08
      Key fingerprint = 3E38 B193 C8A7 F664 B38E  506B 5992 2E84 7EEB 6B3A
uid                  Minakshi Chavan (MTC781) <shenguleminakshi265@gmail.com>
sub   2048R/F51982A7 2023-07-08


[minakshichavan@rhel7-basemachine ~]$ gpg --list-keys
/home/minakshichavan/.gnupg/pubring.gpg
---------------------------------------
pub   2048R/7EEB6B3A 2023-07-08
uid                  Minakshi Chavan (MTC781) <shenguleminakshi265@gmail.com>
sub   2048R/F51982A7 2023-07-08


[minakshichavan@rhel7-basemachine ~]$ gpg --export -a 'Minakshi Chavan (MTC781)'
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v2.0.22 (GNU/Linux)

mQENBGSpcskBCACzWJxRvnWeWaz4df5P2pV4eD/HMOYWuUrCw2qwPT9+0Txi3q67
+1uh48p+E6SEEs31Sojz2jbas5oh4GrfbZh/YtPV8/0vQACfvLSOmrae22KypyCs
Q5fWcMwZA90QXrVyBrU68rERUoXLO2llKCIadMXsdjtSCpIn0UHxf1mtp6WUec1b
paSidBf3qBgz/eGWAzkSF6NM3GBXWUBHvP1F/peTao63tVhkUzhBNWDNA5RBZDmJ
VUaBB2+D5Z+QvvksjRggbRRFfVQN2KImSBXHEPTxT4hx7/4C2m00jlFdN8TNGlut
95tVyjtm0ABvmv5qRQ2er0JDeE+ddxseVGiTABEBAAG0OE1pbmFrc2hpIENoYXZh
biAoTVRDNzgxKSA8c2hlbmd1bGVtaW5ha3NoaTI2NUBnbWFpbC5jb20+iQE5BBMB
AgAjBQJkqXLJAhsDBwsJCAcDAgEGFQgCCQoLBBYCAwECHgECF4AACgkQWZIuhH7r
azonPgf7BZsftPK5rFx896EnI/72DWodV4z/X/YDm63rnWvoUc0WKw837DJUipQ/
57AzIuRNHdOzwOXH4ShYnUcNZq+BPNgmz6zkNqbb/uJfHWUXqzA+ZkTQGvL+xWeU
ecG87GKhFhxtRg3e8ZeIJ5xneH6ab+js6Fqeiud6y6yK8iW+5LglijTKuefud8VA
DNcRCmzCVNoSsrANhjWrJxNFG0181LAZ2Aqqasv8C9lwBRENmgk+EWH/VN7OiyL/
Wm1hFvVGyc51/l2iDgjub9jNGOJ3bSJJyudSn7Bm5oex0Ts8Y7b+HoUL1dtaC9l9
3SW0fRzOs5L4x714PTfNmMl6Q8gilLkBDQRkqXLJAQgAtMkTkl+uaiYmWrNGiQqB
t1/dwNnX/5kwWE6Fk21eX4wMQx4TOC7bwOmpofPT/ve9jrsMRDQCPRucbjfQG+7x
CBY+3W9t1AhPWikIVTiwi1QqPA9p5thd2yd2My3inUGeqeY74QBpT7QoFU8b195I
0OxshKDGmHEQUU1jzdGzMuudcXzdWHiH8W1w+JOBo2NwDrjTDFMXvn256lcKRz7R
7wT7BJgTP8jMfH4kI1x+sHDUJZu6axid+N2k5Yie20V5toV8nIhoZNMoBN18phO9
N9vLL4VCBESE/FeZnpS4VTn/Dfv2Vrg7QlLTICAImKDHjbUsNgF0qh9mlSMo6qbJ
yQARAQABiQEfBBgBAgAJBQJkqXLJAhsMAAoJEFmSLoR+62s6d7IIAJHGLr1wfWOE
JcDjEhLKXngQBYdNouUwVcyZcH1xCkjHBJCVS3Ssyb/yrU1ODOELtU5ZyFtkyfx9
jUzIGkZUXKtTlfi2nL2SYsWroThfvMZiOfzps/XtwAnhRRI58Wpbsz06JdJTak5n
Fuc5Nu0P3hFP3i5mlEohRFfUfdXqLdre8bKfPAcgQsf/OEacpvibmIkI6CJAq0+J
YIeh4/DgSow3xge6W56ApWq0sJzN5F4t3oK176LTUTpV7hpTlnH3HxSKGSCp4Oye
KJPTb4wro3PcFoT+8vCRt+pboElG3VoyMAYBt91gFCtnFfYrf81UvhtbIy+kFj13
nfOogiIvHgU=
=ivQq
-----END PGP PUBLIC KEY BLOCK-----
```
## Step 6 - Verify existing imported public keys and import a new key
The newly created `public` key can be imported in `rpm` database and to make a trust between vendor and client, it's necessary to import the key, else `yum` will by default won't let the package to get installed.
```

[minakshichavan@rhel7-basemachine ~]$ rpm -q gpg-pubkey --qf '%{name}-%{version}-%{release} --> %{summary}\n'
gpg-pubkey-f7e257e6-490b0e11 --> gpg(Red Hat Help Desk (Internal Signing Key) <helpdesk@redhat.com>)
gpg-pubkey-352c64e5-52ae6884 --> gpg(Fedora EPEL (7) <epel@fedoraproject.org>)
gpg-pubkey-222d23d0-5910b0f0 --> gpg(Sublime HQ Pty Ltd <support@sublimetext.com>)
gpg-pubkey-fd431d51-4ae0493b --> gpg(Red Hat, Inc. (release key 2) <security@redhat.com>)
gpg-pubkey-2fa658e0-45700c69 --> gpg(Red Hat, Inc. (auxiliary key) <security@redhat.com>)
gpg-pubkey-7fac5991-4615767f --> gpg(Google, Inc. Linux Package Signing Key <linux-packages-keymaster@google.com>)
gpg-pubkey-f5cf6c1e-5544f037 --> gpg(RPM Fusion free repository for EL (7) <rpmfusion-buildsys@lists.rpmfusion.org>)
gpg-pubkey-d59097ab-52d46e88 --> gpg(packagecloud ops (production key) <ops@packagecloud.io>)
gpg-pubkey-038651bd-56c6038f --> gpg(https://packagecloud.io/slacktechnologies/slack (https://packagecloud.io/docs#gpg_signing) <support@packagecloud.io>)
gpg-pubkey-fce5d7d6-62f32d09 --> gpg(testusername (test comment) <testusername@gmail.com>)
gpg-pubkey-d38b4796-570c8cd3 --> gpg(Google Inc. (Linux Packages Signing Authority) <linux-packages-keymaster@google.com>)

[minakshichavan@rhel7-basemachine ~]$ gpg --export -a 'Minakshi Chavan (MTC781)' > minakshi-public-key.txt


[minakshichavan@rhel7-basemachine ~]$ sudo rpm --import minakshi-public-key.txt 
[minakshichavan@rhel7-basemachine ~]$ echo $?
0
[minakshichavan@rhel7-basemachine ~]$ rpm -q gpg-pubkey --qf '%{name}-%{version}-%{release} --> %{summary}\n'
gpg-pubkey-f7e257e6-490b0e11 --> gpg(Red Hat Help Desk (Internal Signing Key) <helpdesk@redhat.com>)
gpg-pubkey-352c64e5-52ae6884 --> gpg(Fedora EPEL (7) <epel@fedoraproject.org>)
gpg-pubkey-222d23d0-5910b0f0 --> gpg(Sublime HQ Pty Ltd <support@sublimetext.com>)
gpg-pubkey-fd431d51-4ae0493b --> gpg(Red Hat, Inc. (release key 2) <security@redhat.com>)
gpg-pubkey-2fa658e0-45700c69 --> gpg(Red Hat, Inc. (auxiliary key) <security@redhat.com>)
gpg-pubkey-7fac5991-4615767f --> gpg(Google, Inc. Linux Package Signing Key <linux-packages-keymaster@google.com>)
gpg-pubkey-f5cf6c1e-5544f037 --> gpg(RPM Fusion free repository for EL (7) <rpmfusion-buildsys@lists.rpmfusion.org>)
gpg-pubkey-d59097ab-52d46e88 --> gpg(packagecloud ops (production key) <ops@packagecloud.io>)
gpg-pubkey-038651bd-56c6038f --> gpg(https://packagecloud.io/slacktechnologies/slack (https://packagecloud.io/docs#gpg_signing) <support@packagecloud.io>)
gpg-pubkey-fce5d7d6-62f32d09 --> gpg(testusername (test comment) <testusername@gmail.com>)
gpg-pubkey-d38b4796-570c8cd3 --> gpg(Google Inc. (Linux Packages Signing Authority) <linux-packages-keymaster@google.com>)
gpg-pubkey-7eeb6b3a-64a972c9 --> gpg(Minakshi Chavan (MTC781) <shenguleminakshi265@gmail.com>)
```
Observe the last line in above output which shows that the key is now imported in `rpm database`.

## Step 7 - Sign the rpm package
To sign the `rpm` package, one need to create `.rpmmacros` with the contents below.
```
[minakshichavan@rhel7-basemachine ~]$ vi .rpmmacros
[minakshichavan@rhel7-basemachine ~]$ cat .rpmmacros
%_signature gpg
%_gpg_name Minakshi Chavan (MTC781)
```
And finally to get the package signed, here are the steps.
```
[minakshichavan@rhel7-basemachine ~]$ rpm --addsign /home/minakshichavan/rpmbuild/RPMS/noarch/MTC781-1.0.0-0.el7.noarch.rpm
Enter pass phrase: 
Pass phrase is good.
/home/minakshichavan/rpmbuild/RPMS/noarch/MTC781-1.0.0-0.el7.noarch.rpm:
[minakshichavan@rhel7-basemachine ~]$ echo $?
0
```
Verify the signed package.
```
[minakshichavan@rhel7-basemachine ~]$ rpm -qip rpmbuild/
BUILD/     BUILDROOT/ RPMS/      SOURCES/   SPECS/     SRPMS/     
[minakshichavan@rhel7-basemachine ~]$ rpm -qip rpmbuild/RPMS/noarch/MTC781-1.0.0-0.el7.noarch.rpm 
Name        : MTC781
Version     : 1.0.0
Release     : 0.el7
Architecture: noarch
Install Date: (not installed)
Group       : Applications/File
Size        : 1449
License     : GPLv2+
Signature   : RSA/SHA1, Saturday 08 July 2023 08:02:52 PM IST, Key ID 59922e847eeb6b3a
Source RPM  : MTC781-1.0.0-0.el7.src.rpm
Build Date  : Saturday 08 July 2023 07:57:12 PM IST
Build Host  : rhel7-basemachine
Relocations : (not relocatable)
Packager    : Minakshi Pushpendra Chavan
Vendor      : G S Mandal's Maharashtra Institute of Technology, Aurangabad
Summary     : This is a dummy package built by Minakshi Pushpendra Chavan.
Description :
This is a sample package to deliver the ansible pre-defined tasks as a payload through signed rpm package. This is just a PoC.

```
Observe the line `Signature` now, it shows `RSA/SHA1, Tuesday 09 August 2022 04:37:00 PM IST, Key ID e25cb92b3df5524b` as it's value. Means the package is now signed with an appropriate key. And that can also be verified by rpm command as follows.
```
[minakshichavan@rhel7-basemachine ~]$ rpm -K /home/minakshichavan/rpmbuild/RPMS/noarch/MTC781-1.0.0-0.el7.noarch.rpm
/home/minakshichavan/rpmbuild/RPMS/noarch/MTC781-1.0.0-0.el7.noarch.rpm: rsa sha1 (md5) pgp md5 OK
```
## Step 8 - Install the rpm package.
Installation of signed package is possible as follows. Verify the files deployed by the package as well as dummy man page.
```
[minakshichavan@rhel7-basemachine ~]$ sudo rpm -ivh /home/minakshichavan/rpmbuild/RPMS/noarch/MTC781-1.0.0-0.el7.noarch.rpm
Preparing...                          ################################# [100%]
Updating / installing...
   1:MTC781-1.0.0-0.el7               ################################# [100%]
Please run MTC781 command to view deployment !
Your constructive feedback will be highly appreciated!!!
[minakshichavan@rhel7-basemachine ~]$ echo $?
0


[minakshichavan@rhel7-basemachine ~]$ sudo rpm -qa | grep MTC781
MTC781-1.0.0-0.el7.noarch
[minakshichavan@rhel7-basemachine ~]$ sudo rpm -ql MTC781-1.0.0-0.el7.noarch
/etc/MTC781/MTC781.conf
/usr/bin/MTC781-ansible_task01
/usr/bin/MTC781-ansible_task02
/usr/bin/MTC781-ansible_task03
/usr/bin/MTC781-ansible_task04
/usr/bin/MTC781-ansible_task05
/usr/bin/MTC781-ansible_task06
/usr/bin/MTC781-ansible_task07
/usr/bin/MTC781-ansible_task08
/usr/bin/MTC781-ansible_task09
/usr/bin/MTC781-bin
/usr/local/man/man1/MTC781.1.gz


[minakshichavan@rhel7-basemachine ~]$ MTC781-bin 
 This is a POC binary execution which will just check the presence of the files deployed by the MTC781 package, nothing else!
 Configuration File : /etc/MTC781/MTC781.conf is present
 Binary Exe File : /usr/bin/MTC781-bin is present
 Manual Page File	: /usr/local/man/man1/MTC781.1.gz is present


[minakshichavan@rhel7-basemachine ~]$ man MTC781 > manpage
[minakshichavan@rhel7-basemachine ~]$ cat manpage 
MTC781(1)                                                                                  General Commands Manual                                                                                  MTC781(1)



NAME
       MTC781-bin - Built by Minakshi Pushpendra Chavan - MTech CST

SYNOPSIS
       G S Mandal's Maharashtra Institute of Technology, Chh. Sambhajinagar (Formerly known as Aurangabad) - An Autonomous Institute [ h ] [ b ]

DESCRIPTION
       Option1 This is actually a Proof of Concept and dummy man page to be created as a part of minor project for the submission and completion of subject MTC781

OPTIONS
       h      Option 1

       b      Option 2

```
In this way, the dummay package is built in order to delivery the dummy payload using Red Hat Package Manager.

## Step 9 - Create a dummy repository and host it on an internet public location for test purpose.

The single package can be a part of an existing repository or a standalone single and independent repository and can be done as follows.
```
[minakshichavan@rhel7-basemachine ~]$ mkdir /tmp/minakshi-mtc781
[minakshichavan@rhel7-basemachine ~]$ cp rpmbuild/RPMS/noarch/MTC781-1.0.0-0.el7.noarch.rpm /tmp/minakshi-mtc781
[minakshichavan@rhel7-basemachine ~]$ ls -l /tmp/minakshi-mtc781
total 8
-rw-rw-r--. 1 minakshichavan minakshichavan 6080 Jul  8 20:05 MTC781-1.0.0-0.el7.noarch.rpm
[minakshichavan@rhel7-basemachine ~]$ sudo createrepo -v /tmp/minakshi-mtc781
Spawning worker 0 with 1 pkgs
Spawning worker 1 with 0 pkgs
Spawning worker 2 with 0 pkgs
Spawning worker 3 with 0 pkgs
Spawning worker 4 with 0 pkgs
Spawning worker 5 with 0 pkgs
Spawning worker 6 with 0 pkgs
Spawning worker 7 with 0 pkgs
Worker 0: reading MTC781-1.0.0-0.el7.noarch.rpm
Workers Finished
Saving Primary metadata
Saving file lists metadata
Saving other metadata
Generating sqlite DBs
Starting other db creation: Sat Jul  8 20:06:05 2023
Ending other db creation: Sat Jul  8 20:06:05 2023
Starting filelists db creation: Sat Jul  8 20:06:05 2023
Ending filelists db creation: Sat Jul  8 20:06:05 2023
Starting primary db creation: Sat Jul  8 20:06:05 2023
Ending primary db creation: Sat Jul  8 20:06:05 2023
Sqlite DBs complete
[minakshichavan@rhel7-basemachine ~]$ cp minakshi-public-key.txt /tmp/minakshi-mtc781/
[minakshichavan@rhel7-basemachine ~]$ cat /tmp/minakshi-mtc781/minakshi-public-key.txt 
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v2.0.22 (GNU/Linux)

mQENBGSpcskBCACzWJxRvnWeWaz4df5P2pV4eD/HMOYWuUrCw2qwPT9+0Txi3q67
+1uh48p+E6SEEs31Sojz2jbas5oh4GrfbZh/YtPV8/0vQACfvLSOmrae22KypyCs
Q5fWcMwZA90QXrVyBrU68rERUoXLO2llKCIadMXsdjtSCpIn0UHxf1mtp6WUec1b
paSidBf3qBgz/eGWAzkSF6NM3GBXWUBHvP1F/peTao63tVhkUzhBNWDNA5RBZDmJ
VUaBB2+D5Z+QvvksjRggbRRFfVQN2KImSBXHEPTxT4hx7/4C2m00jlFdN8TNGlut
95tVyjtm0ABvmv5qRQ2er0JDeE+ddxseVGiTABEBAAG0OE1pbmFrc2hpIENoYXZh
biAoTVRDNzgxKSA8c2hlbmd1bGVtaW5ha3NoaTI2NUBnbWFpbC5jb20+iQE5BBMB
AgAjBQJkqXLJAhsDBwsJCAcDAgEGFQgCCQoLBBYCAwECHgECF4AACgkQWZIuhH7r
azonPgf7BZsftPK5rFx896EnI/72DWodV4z/X/YDm63rnWvoUc0WKw837DJUipQ/
57AzIuRNHdOzwOXH4ShYnUcNZq+BPNgmz6zkNqbb/uJfHWUXqzA+ZkTQGvL+xWeU
ecG87GKhFhxtRg3e8ZeIJ5xneH6ab+js6Fqeiud6y6yK8iW+5LglijTKuefud8VA
DNcRCmzCVNoSsrANhjWrJxNFG0181LAZ2Aqqasv8C9lwBRENmgk+EWH/VN7OiyL/
Wm1hFvVGyc51/l2iDgjub9jNGOJ3bSJJyudSn7Bm5oex0Ts8Y7b+HoUL1dtaC9l9
3SW0fRzOs5L4x714PTfNmMl6Q8gilLkBDQRkqXLJAQgAtMkTkl+uaiYmWrNGiQqB
t1/dwNnX/5kwWE6Fk21eX4wMQx4TOC7bwOmpofPT/ve9jrsMRDQCPRucbjfQG+7x
CBY+3W9t1AhPWikIVTiwi1QqPA9p5thd2yd2My3inUGeqeY74QBpT7QoFU8b195I
0OxshKDGmHEQUU1jzdGzMuudcXzdWHiH8W1w+JOBo2NwDrjTDFMXvn256lcKRz7R
7wT7BJgTP8jMfH4kI1x+sHDUJZu6axid+N2k5Yie20V5toV8nIhoZNMoBN18phO9
N9vLL4VCBESE/FeZnpS4VTn/Dfv2Vrg7QlLTICAImKDHjbUsNgF0qh9mlSMo6qbJ
yQARAQABiQEfBBgBAgAJBQJkqXLJAhsMAAoJEFmSLoR+62s6d7IIAJHGLr1wfWOE
JcDjEhLKXngQBYdNouUwVcyZcH1xCkjHBJCVS3Ssyb/yrU1ODOELtU5ZyFtkyfx9
jUzIGkZUXKtTlfi2nL2SYsWroThfvMZiOfzps/XtwAnhRRI58Wpbsz06JdJTak5n
Fuc5Nu0P3hFP3i5mlEohRFfUfdXqLdre8bKfPAcgQsf/OEacpvibmIkI6CJAq0+J
YIeh4/DgSow3xge6W56ApWq0sJzN5F4t3oK176LTUTpV7hpTlnH3HxSKGSCp4Oye
KJPTb4wro3PcFoT+8vCRt+pboElG3VoyMAYBt91gFCtnFfYrf81UvhtbIy+kFj13
nfOogiIvHgU=
=ivQq
-----END PGP PUBLIC KEY BLOCK-----

[minakshichavan@rhel7-basemachine ~]$ tree /tmp/minakshi-mtc781/
/tmp/minakshi-mtc781/
├── minakshi-public-key.txt
├── MTC781-1.0.0-0.el7.noarch.rpm
└── repodata
    ├── 09a6ec0060c6c5ab2d3dfbd9032c4695968a343574c63f475f774166c0faed4f-filelists.sqlite.bz2
    ├── 4a31001911c96cd0ba8558f8cd17b08b10875e6ae0da23a1478f6a5f60b6777d-primary.sqlite.bz2
    ├── a72c216f6e50fd08376ed66585c51a2cd84b818bae2cb1860b38ec58a4f2dd92-primary.xml.gz
    ├── a743ea5a43957dea36b0e64405a86c0ab28912d8b162a88e5f63be87cd81ab5c-other.xml.gz
    ├── cd547a6fc70c52e020c9816335debb91a905da44070890672360cfac0e4eedf8-other.sqlite.bz2
    ├── d1b620e3a1ac667c8a195a089a2c137f54d2ffa1745130b8acb101e1d6c53b11-filelists.xml.gz
    └── repomd.xml

1 directory, 9 files

```
Hosted this entire directory `/tmp/minakshi-mtc781` at http://pushpendrachavan/minakshi-mtc781 along with the public key and `yum` package `metadata`

## Step 10 - Create a `repo` file on any Red Hat Enterprise Linux/CentOS/Fedora Linux/Scientic Linux/Oracle Linux pointing out to the onlie repository as follows.
Create a repo file as follows.
```
[minakshi@rhel7-basemachine ~]$ sudo cat /etc/yum.repos.d/minakshichavan.repo 
[minakshichavan]
Name=Minakshi Chavan Dummy Repo
baseurl=http://pushpendrachavan.in/minakshi-mtc781/
enabled=1
gpgcheck=1
gpgkey=https://pushpendrachavan.in/minakshi-mtc781/minakshichavan-key.txt
```
As as additional step, you can also import `rpm` key manually as follows.
```
[minakshi@rhel7-basemachine ~]$ sudo rpm --import https://pushpendrachavan.in/minaksh-mtc781/minakshi-public-key.txt
```
And verify the package being fetched.
```
[minakshi@rhel7-basemachine ~]$ yum repolist minakshichavan
Loaded plugins: langpacks, product-id, search-disabled-repos, subscription-manager
google-chrome                                                                                                                                 3/3
slack                                                                                                                                       37/37
repo id                                                         repo name                                                                   status
minakshichavan                                                  Minakshi Chavan Dummy Repo                                                  1
repolist: 1

[root@rhel7-basemachine ~]# yum info MTC781
Loaded plugins: langpacks, product-id, search-disabled-repos, subscription-manager
Available Packages
Name        : MTC781
Arch        : noarch
Version     : 1.0.0
Release     : 0.el7
Size        : 5.9 k
Repo        : minakshichavan-MTC781
Summary     : This is a dummy package built by Minakshi Pushpendra Chavan.
License     : GPLv2+
Description : This is a sample package to deliver the ansible pre-defined tasks as a payload through signed rpm package. This is just a PoC.
```

## Step 11 - Install the package on any client online through internet.
The package now can be installed on any system in the world just by following step 10 and 11 as follows.
```
[root@rhel7-basemachine ~]# yum install MTC781
Loaded plugins: langpacks, product-id, search-disabled-repos, subscription-manager
Resolving Dependencies
--> Running transaction check
---> Package MTC781.noarch 0:1.0.0-0.el7 will be installed
--> Finished Dependency Resolution
epel/x86_64/group_gz                                                                                                                                                                        |  99 kB  00:00:00     

Dependencies Resolved

===================================================================================================================================================================================================================
 Package                                       Arch                                          Version                                            Repository                                                    Size
===================================================================================================================================================================================================================
Installing:
 MTC781                                        noarch                                        1.0.0-0.el7                                        minakshichavan-MTC781                                        5.9 k

Transaction Summary
===================================================================================================================================================================================================================
Install  1 Package

Total download size: 5.9 k
Installed size: 1.4 k
Is this ok [y/d/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
Warning: RPMDB altered outside of yum.
  Installing : MTC781-1.0.0-0.el7.noarch                                                                                                                                                                       1/1 
Please run MTC781 command to view deployment !
Your constructive feedback will be highly appreciated!!!
  Verifying  : MTC781-1.0.0-0.el7.noarch                                                                                                                                                                       1/1 

Installed:
  MTC781.noarch 0:1.0.0-0.el7                                                                                                                                                                                      

Complete!
[root@rhel7-basemachine ~]# rpm -q MTC781
MTC781-1.0.0-0.el7.noarch
[root@rhel7-basemachine ~]# rpm -ql MTC781
/etc/MTC781/MTC781.conf
/usr/bin/MTC781-ansible_task01
/usr/bin/MTC781-ansible_task02
/usr/bin/MTC781-ansible_task03
/usr/bin/MTC781-ansible_task04
/usr/bin/MTC781-ansible_task05
/usr/bin/MTC781-ansible_task06
/usr/bin/MTC781-ansible_task07
/usr/bin/MTC781-ansible_task08
/usr/bin/MTC781-ansible_task09
/usr/bin/MTC781-bin
/usr/local/man/man1/MTC781.1.gz
[root@rhel7-basemachine ~]# MTC781-bin 
 This is a POC binary execution which will just check the presence of the files deployed by the MTC781 package, nothing else!
 Configuration File : /etc/MTC781/MTC781.conf is present
 Binary Exe File : /usr/bin/MTC781-bin is present
 Manual Page File	: /usr/local/man/man1/MTC781.1.gz is present

[root@rhel7-basemachine ~]# rpm -qi MTC781
Name        : MTC781
Version     : 1.0.0
Release     : 0.el7
Architecture: noarch
Install Date: Saturday 08 July 2023 08:43:20 PM IST
Group       : Applications/File
Size        : 1449
License     : GPLv2+
Signature   : RSA/SHA1, Saturday 08 July 2023 08:02:52 PM IST, Key ID 59922e847eeb6b3a
Source RPM  : MTC781-1.0.0-0.el7.src.rpm
Build Date  : Saturday 08 July 2023 07:57:12 PM IST
Build Host  : rhel7-basemachine
Relocations : (not relocatable)
Packager    : Minakshi Pushpendra Chavan
Vendor      : G S Mandal's Maharashtra Institute of Technology, Aurangabad
Summary     : This is a dummy package built by Minakshi Pushpendra Chavan.
Description :
This is a sample package to deliver the ansible pre-defined tasks as a payload through signed rpm package. This is just a PoC.

```

On any RHEL client to implement the package deployment test, please repeat only step 10 and 11.
A Quick test can be done online on a CentOS workstation which is available at https://www.onworks.net/os-distributions/rpm-based/free-centos-workstation-online
